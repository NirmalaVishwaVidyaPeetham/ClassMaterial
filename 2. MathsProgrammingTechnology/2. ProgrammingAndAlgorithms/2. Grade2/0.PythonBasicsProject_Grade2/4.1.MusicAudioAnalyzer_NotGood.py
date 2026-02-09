import sys
import numpy as np
import pyaudio
import librosa
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from scipy.fft import rfft, rfftfreq


class AudioVisualizer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Audio Configuration ---
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 2048
        self.pa = pyaudio.PyAudio()
        self.stream = None

        # --- Visualization Data ---
        self.history_length = 50  # X-axis progression
        self.freq_bins = 0
        self.z_data = None
        self.frequencies = None

        # Pitch tracking data for 2D
        self.pitch_history = np.zeros(200)
        self.time_axis_2d = np.arange(200)

        self.init_ui()

        # Timer for updates
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)

    def init_ui(self):
        self.setWindowTitle("Pro Audio Visualizer: 3D Spectrogram & 2D Pitch Monitor")
        self.resize(1200, 800)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # --- Controls Area ---
        controls = QtWidgets.QHBoxLayout()
        self.btn_mic = QtWidgets.QPushButton("Start Microphone")
        self.btn_mic.clicked.connect(self.toggle_mic)
        self.btn_file = QtWidgets.QPushButton("Open Audio File")
        self.btn_file.clicked.connect(self.open_file)
        self.label_status = QtWidgets.QLabel("Status: Idle")

        controls.addWidget(self.btn_mic)
        controls.addWidget(self.btn_file)
        controls.addStretch()
        controls.addWidget(self.label_status)
        layout.addLayout(controls)

        # --- Visualization Tabs ---
        self.tabs = QtWidgets.QTabWidget()
        layout.addWidget(self.tabs)

        # Tab 1: 3D Visualization
        self.view_3d = gl.GLViewWidget()
        self.view_3d.setCameraPosition(distance=60, elevation=30, azimuth=45)
        self.tabs.addTab(self.view_3d, "3D Frequency Progression")

        # Fixed Axes with Sizes
        self.axes = gl.GLAxisItem()
        self.axes.setSize(x=30, y=30, z=15)
        self.view_3d.addItem(self.axes)

        # Labels for 3D Axes using GLTextItem
        self.label_time = gl.GLTextItem(pos=(32, 0, 0), text='Time (X)', color=(255, 100, 100, 255))
        self.label_freq = gl.GLTextItem(pos=(0, 32, 0), text='Freq (Y)', color=(100, 255, 100, 255))
        self.label_amp = gl.GLTextItem(pos=(0, 0, 16), text='Amp (Z)', color=(100, 100, 255, 255))
        self.view_3d.addItem(self.label_time)
        self.view_3d.addItem(self.label_freq)
        self.view_3d.addItem(self.label_amp)

        # 3D Surface Item
        # Switching back to 'heightColor' shader. This is the most stable
        # for real-time vertex updates and avoids the setData color error.
        self.surface = gl.GLSurfacePlotItem(shader='heightColor', computeNormals=False, smooth=False)
        self.view_3d.addItem(self.surface)

        # Tab 2: 2D Pitch Monitor
        self.plot_2d = pg.PlotWidget()
        self.plot_2d.setBackground('k')
        self.plot_2d.setLabel('left', 'Musical Note (Pitch)')
        self.plot_2d.setLabel('bottom', 'Time (Frames)')
        self.plot_2d.showGrid(x=True, y=True, alpha=0.3)
        self.tabs.addTab(self.plot_2d, "2D Pitch Monitor")

        self.setup_piano_axis()
        self.pitch_curve = self.plot_2d.plot(pen=pg.mkPen('c', width=2))

    def setup_piano_axis(self):
        """Maps frequency index to musical notes for the Y axis in 2D view"""
        values = []
        for n in range(24, 108):
            note_name = librosa.midi_to_note(n)
            values.append((n, note_name))

        ay = self.plot_2d.getAxis('left')
        ay.setTicks([values[::3]])
        self.plot_2d.setYRange(24, 108)

    def freq_to_midi(self, freq):
        if freq <= 0: return 0
        return 12 * np.log2(freq / 440.0) + 69

    def toggle_mic(self):
        if self.stream is None:
            try:
                self.stream = self.pa.open(
                    format=self.FORMAT, channels=self.CHANNELS,
                    rate=self.RATE, input=True, frames_per_buffer=self.CHUNK
                )
                self.timer.start(30)
                self.btn_mic.setText("Stop Microphone")
                self.label_status.setText("Status: Streaming Microphone...")
            except Exception as e:
                self.label_status.setText(f"Mic Error: {str(e)}")
        else:
            self.timer.stop()
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
            self.btn_mic.setText("Start Microphone")
            self.label_status.setText("Status: Idle")

    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3)")
        if file_path:
            try:
                self.label_status.setText(f"Status: Loading {file_path}...")
                y, sr = librosa.load(file_path, sr=self.RATE)
                self.file_data = y
                self.file_ptr = 0
                self.is_playing_file = True
                self.timer.start(30)
                self.label_status.setText("Status: Playing File...")
            except Exception as e:
                self.label_status.setText(f"Error: {str(e)}")

    def update_frame(self):
        if self.stream:
            try:
                raw_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                data = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32)
            except:
                return
        elif hasattr(self, 'is_playing_file') and self.is_playing_file:
            start = self.file_ptr
            end = start + self.CHUNK
            if end > len(self.file_data):
                self.timer.stop()
                self.is_playing_file = False
                return
            data = self.file_data[start:end]
            self.file_ptr = end
        else:
            return

        # FFT Analysis
        fft_data = rfft(data)
        freqs = rfftfreq(len(data), 1 / self.RATE)
        magnitude = np.abs(fft_data)
        magnitude = 20 * np.log10(magnitude + 1e-6)
        magnitude = np.clip(magnitude, 0, 80)

        # Focus range for frequency visualization (50Hz to 3500Hz)
        idx = np.where((freqs > 50) & (freqs < 3500))[0]
        current_slice = magnitude[idx]

        if self.z_data is None:
            self.freq_bins = len(idx)
            self.z_data = np.zeros((self.history_length, self.freq_bins))
            self.frequencies = freqs[idx]

            # Reset surface scaling to ensure visualization fits the fixed axis frame
            self.surface.resetTransform()
            # Scale X to match axis length (30 units), Y to match axis length, Z for visual height
            self.surface.scale(30 / self.history_length, 30 / self.freq_bins, 0.15)

            # Roll data for temporal progression
        self.z_data = np.roll(self.z_data, -1, axis=0)
        self.z_data[-1, :] = current_slice

        # Update 3D Surface
        x = np.arange(self.history_length)
        y = np.arange(self.freq_bins)

        try:
            # setData is now used without the 'colors' argument to avoid the drawing error
            self.surface.setData(x=x, y=y, z=self.z_data)
        except Exception as e:
            pass

        # 2D Pitch Tracking
        peak_idx = np.argmax(magnitude[idx])
        dominant_freq = self.frequencies[peak_idx]

        if magnitude[idx][peak_idx] > 35:
            midi_note = self.freq_to_midi(dominant_freq)
        else:
            midi_note = 0

        self.pitch_history = np.roll(self.pitch_history, -1)
        self.pitch_history[-1] = midi_note
        self.pitch_curve.setData(self.time_axis_2d, self.pitch_history)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AudioVisualizer()
    window.show()
    sys.exit(app.exec_())