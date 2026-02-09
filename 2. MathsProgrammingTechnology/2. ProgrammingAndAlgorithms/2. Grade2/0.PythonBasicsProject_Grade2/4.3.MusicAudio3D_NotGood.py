import sys
import numpy as np
import pyaudio
import librosa
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from scipy.fft import rfft, rfftfreq
from collections import deque


class AudioVisualizer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Audio Settings ---
        self.RATE = 44100
        self.CHUNK = 2048
        self.FFT_SIZE = 16384  # Matches high-res 2D version
        self.pa = pyaudio.PyAudio()
        self.stream = None

        # --- Data Buffers ---
        self.history_len = 80
        self.freq_range = (50, 2500)  # Matches 2D version DISPLAY_FMAX
        self.audio_buffer = np.zeros(self.FFT_SIZE, dtype=np.float32)
        self.z_history = None
        self.pitch_history = deque([(0, 0)] * self.history_len, maxlen=self.history_len)

        # Consistent DB Limits
        self.DB_MIN = -80
        self.DB_MAX = 0

        self.init_ui()

        # Timer for updates (30 FPS for smooth animation)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)

    def init_ui(self):
        self.setWindowTitle("Pro Piano Spectrum: 2D/3D Dual Monitor")
        self.resize(1280, 800)
        self.setStyleSheet("background-color: #121212; color: white;")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # --- Top Header ---
        header = QtWidgets.QHBoxLayout()
        self.btn_toggle = QtWidgets.QPushButton("START MICROPHONE")
        self.btn_toggle.setFixedWidth(200)
        self.btn_toggle.setMinimumHeight(45)
        self.btn_toggle.setStyleSheet("""
            QPushButton { background-color: #00FFCC; color: black; font-weight: bold; border-radius: 5px; }
            QPushButton:hover { background-color: #00CCAA; }
        """)
        self.btn_toggle.clicked.connect(self.toggle_audio)

        self.label_note = QtWidgets.QLabel("Note: ---")
        self.label_note.setStyleSheet("font-size: 26px; font-weight: bold; color: #FFFF00; padding-right: 20px;")

        header.addWidget(self.btn_toggle)
        header.addStretch()
        header.addWidget(self.label_note)
        main_layout.addLayout(header)

        # --- Tabs ---
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #333; }
            QTabBar::tab { background: #222; color: #888; padding: 12px 30px; border-top-left-radius: 4px; border-top-right-radius: 4px; }
            QTabBar::tab:selected { background: #333; color: #00FFCC; border-bottom: 2px solid #00FFCC; }
        """)
        main_layout.addWidget(self.tabs)

        # --- 2D View Setup ---
        self.view_2d = pg.PlotWidget()
        self.view_2d.setBackground('#000000')
        self.view_2d.setLabel('left', 'Magnitude', units='dB')
        self.view_2d.setLabel('bottom', 'Frequency', units='Hz')
        self.view_2d.setLogMode(x=True, y=False)
        self.view_2d.showGrid(x=False, y=True, alpha=0.1)
        self.tabs.addTab(self.view_2d, "2D Spectrum Monitor")

        # Spectrum Curve with Fill
        self.curve_2d = self.view_2d.plot(
            pen=pg.mkPen('#00FFCC', width=1.5),
            fillLevel=self.DB_MIN,
            fillBrush=(0, 255, 204, 35)
        )

        # Peak Tracking Elements
        self.peak_line_2d = self.view_2d.addLine(x=0, pen=pg.mkPen('#FFFF00', width=1.8, style=QtCore.Qt.DashLine))
        self.peak_label_2d = pg.TextItem(color='#FFFF00', anchor=(0.5, 1))
        self.view_2d.addItem(self.peak_label_2d)

        # Grid and Piano Axis Setup
        self.setup_2d_note_ui()

        # --- 3D View Setup ---
        self.view_3d = gl.GLViewWidget()
        self.view_3d.setCameraPosition(distance=65, elevation=35, azimuth=45)
        self.tabs.addTab(self.view_3d, "3D Temporal Waterfall")

        self.axes_3d = gl.GLAxisItem()
        self.axes_3d.setSize(x=40, y=40, z=20)
        self.view_3d.addItem(self.axes_3d)

        self.view_3d.addItem(gl.GLTextItem(pos=(42, 0, 0), text='Time (X)', color=(255, 100, 100, 255)))
        self.view_3d.addItem(gl.GLTextItem(pos=(0, 42, 0), text='Frequency (Y)', color=(100, 255, 100, 255)))
        self.view_3d.addItem(gl.GLTextItem(pos=(0, 0, 21), text='0 dB', color=(100, 100, 255, 255)))

        self.surface = gl.GLSurfacePlotItem(shader='heightColor', computeNormals=False, smooth=False)
        self.view_3d.addItem(self.surface)

        self.pitch_line_3d = gl.GLLinePlotItem(width=5, color=(255, 255, 0, 255), antialias=True)
        self.view_3d.addItem(self.pitch_line_3d)

    def setup_2d_note_ui(self):
        """Replicates the grid and top axis labels from the 2D monitor"""
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        tick_labels = []

        for m in range(21, 108):
            f = 440.0 * (2 ** ((m - 69) / 12.0))
            if self.freq_range[0] <= f <= self.freq_range[1]:
                log_f = np.log10(f)

                # Full grid lines for every semitone
                line = self.view_2d.addLine(x=log_f, pen=pg.mkPen(255, 255, 255, 12), movable=False)
                line.setZValue(-10)

                # Note Labels
                if m % 12 == 0 or m == 69:
                    label = f"{notes[m % 12]}{(m // 12) - 1}"
                    tick_labels.append((log_f, label))

        ax_top = self.view_2d.getPlotItem().getAxis('top')
        self.view_2d.getPlotItem().layout.addItem(ax_top, 1, 1)
        ax_top.setTicks([tick_labels])

        self.view_2d.setXRange(np.log10(self.freq_range[0]), np.log10(self.freq_range[1]), padding=0)
        self.view_2d.setYRange(self.DB_MIN, self.DB_MAX, padding=0)

    def yin_pitch(self, sig, sr, threshold=0.15):
        tau_min = int(sr / 4500)
        tau_max = int(sr / 25)

        diff = np.zeros(tau_max)
        for tau in range(1, tau_max):
            delta = sig[:-tau] - sig[tau:]
            diff[tau] = np.sum(delta ** 2)

        cmndf = np.zeros(tau_max)
        cmndf[0] = 1
        rs = 0
        for tau in range(1, tau_max):
            rs += diff[tau]
            cmndf[tau] = diff[tau] / ((1 / tau) * rs + 1e-10)

        tau_found = -1
        for tau in range(tau_min, tau_max - 1):
            if cmndf[tau] < threshold:
                if cmndf[tau] < cmndf[tau - 1] and cmndf[tau] < cmndf[tau + 1]:
                    tau_found = tau
                    break
        if tau_found == -1: return None

        y1, y2, y3 = cmndf[tau_found - 1], cmndf[tau_found], cmndf[tau_found + 1]
        denom = y1 - 2 * y2 + y3
        if abs(denom) > 1e-10:
            tau_found += 0.5 * (y1 - y3) / denom

        return sr / tau_found

    def toggle_audio(self):
        if self.stream is None:
            self.stream = self.pa.open(format=pyaudio.paInt16, channels=1, rate=self.RATE,
                                       input=True, frames_per_buffer=self.CHUNK)
            self.timer.start(30)
            self.btn_toggle.setText("STOP MICROPHONE")
            self.btn_toggle.setStyleSheet(
                "background-color: #FF5555; color: white; font-weight: bold; border-radius: 5px;")
        else:
            self.timer.stop()
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            self.btn_toggle.setText("START MICROPHONE")
            self.btn_toggle.setStyleSheet(
                "background-color: #00FFCC; color: black; font-weight: bold; border-radius: 5px;")

    def update_frame(self):
        try:
            raw = self.stream.read(self.CHUNK, exception_on_overflow=False)
            data = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
        except:
            return

        self.audio_buffer = np.roll(self.audio_buffer, -self.CHUNK)
        self.audio_buffer[-self.CHUNK:] = data

        # Spectrum Calculation
        windowed = self.audio_buffer * np.blackman(self.FFT_SIZE)
        fft_res = np.abs(rfft(windowed)) / (self.FFT_SIZE / 2.0)
        all_freqs = rfftfreq(self.FFT_SIZE, 1 / self.RATE)

        mask = (all_freqs >= self.freq_range[0]) & (all_freqs <= self.freq_range[1])
        mag_db = 20 * np.log10(fft_res[mask] + 1e-9)
        mag_db = np.clip(mag_db, self.DB_MIN, self.DB_MAX)

        # Update 2D Curve
        self.curve_2d.setData(all_freqs[mask], mag_db)

        # YIN Fundamental Pitch Detection
        f0 = self.yin_pitch(self.audio_buffer, self.RATE)
        rms = np.sqrt(np.mean(data ** 2))

        curr_midi = 0
        if f0 and rms > 0.005:
            curr_midi = 12 * np.log2(f0 / 440.0) + 69
            name = librosa.midi_to_note(int(round(curr_midi)))
            self.label_note.setText(f"Note: {name}")

            # Update 2D Tracker
            log_f0 = np.log10(f0)
            self.peak_line_2d.setPos(log_f0)
            self.peak_line_2d.show()
            self.peak_label_2d.setText(f"{name}\n{f0:.1f}Hz")
            self.peak_label_2d.setPos(log_f0, -5)
        else:
            self.label_note.setText("Note: ---")
            self.peak_line_2d.hide()
            self.peak_label_2d.setText("")

        self.pitch_history.append((f0, curr_midi) if curr_midi > 0 else (0, 0))

        # 3D Waterfall Update
        if self.z_history is None:
            self.freq_bins = len(mag_db)
            self.z_history = np.zeros((self.history_len, self.freq_bins))
            # Sync Z-Scale: Total range is 80dB. Axis height is 20 units.
            # Scale = 20 / 80 = 0.25
            self.surface.scale(40 / self.history_len, 40 / self.freq_bins, 0.25)

        self.z_history = np.roll(self.z_history, -1, axis=0)
        # Shift data so self.DB_MIN (-80) becomes 0 and self.DB_MAX (0) becomes 80
        self.z_history[-1, :] = mag_db - self.DB_MIN

        self.surface.setData(x=np.arange(self.history_len),
                             y=np.arange(self.freq_bins),
                             z=self.z_history)

        # 3D Pitch Path (Yellow Line)
        pts = []
        for i, (pf, mid) in enumerate(self.pitch_history):
            if pf and self.freq_range[0] <= pf <= self.freq_range[1]:
                y_bin = np.searchsorted(all_freqs[mask], pf)
                px = i * (40 / self.history_len)
                py = y_bin * (40 / self.freq_bins)
                # Position Z using the same 0.25 scaling
                pz = self.z_history[i, min(y_bin, self.freq_bins - 1)] * 0.25 + 1.0
                pts.append([px, py, pz])

        if pts:
            self.pitch_line_3d.setData(pos=np.array(pts))
        else:
            self.pitch_line_3d.setData(pos=np.empty((0, 3)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AudioVisualizer()
    window.show()
    sys.exit(app.exec_())