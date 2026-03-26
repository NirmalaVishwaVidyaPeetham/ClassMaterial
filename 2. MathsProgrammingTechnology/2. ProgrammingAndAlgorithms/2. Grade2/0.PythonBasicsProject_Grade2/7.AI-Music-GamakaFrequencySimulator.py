import numpy as np
import matplotlib.pyplot as plt


def generate_all_gamakas(base_freq, duration=1.0, fs=1000):
    """
    Simulates the frequency paths of the 15 Panchadasa Gamakas and Pratyaghata.
    """
    t = np.linspace(0, duration, int(fs * duration))
    mid = len(t) // 2

    # Frequency ratios based on 12-tone equal temperament for simplicity
    # Sa=1.0, Ri=1.12, Ga=1.2, Ma=1.33, Pa=1.5
    f_ri = base_freq * 1.122
    f_ga = base_freq * 1.189
    f_pa = base_freq * 1.5

    gamakas = {}

    # 1. KAMPITA (Vibrato) - Trembling on the note
    gamakas['1. Kampita'] = base_freq + (base_freq * 0.02) * np.sin(2 * np.pi * 12 * t)

    # 2. LINA (Merge) - Merging softly into the next note
    # Logistic curve for a "soft" merge
    gamakas['2. Lina'] = base_freq + (f_ri - base_freq) / (1 + np.exp(-15 * (t - duration / 2)))

    # 3. ANDOLITA (Swing) - Rhythmic oscillation between two notes
    gamakas['3. Andolita'] = ((base_freq + f_ri) / 2) + ((f_ri - base_freq) / 2) * np.sin(2 * np.pi * 3 * t)

    # 4. PLAVITA (Deep Swing) - Longer/wider variation of Andolita
    gamakas['4. Plavita'] = ((base_freq + f_ga) / 2) + ((f_ga - base_freq) / 2) * np.sin(2 * np.pi * 1.5 * t)

    # 5. SPHURITA (Accent) - Stressing the second note in a pair
    sphurita = np.full_like(t, base_freq)
    sphurita[mid:] = f_ri  # Jump to second note
    sphurita[mid:mid + 100] += (base_freq * 0.08)  # The "stress/kick"
    gamakas['5. Sphurita'] = sphurita

    # 6. TIRUPAMA (Squeeze) - Pressure/nervous tension on a note
    gamakas['6. Tirupama'] = base_freq + (base_freq * 0.03) * np.abs(np.sin(2 * np.pi * 8 * t))

    # 7. AHATA (Rava) - Touching the upper note quickly
    ahata = np.full_like(t, base_freq)
    for i in range(1, 4):
        pos = int(i * len(t) / 4)
        ahata[pos:pos + 50] = f_ri  # Quick flick to Ri
    gamakas['7. Ahata (Rava)'] = ahata

    # 8. VALI (Spiral) - Circular movement (Veena style)
    # Represented as a frequency "curl"
    gamakas['8. Vali'] = base_freq + (base_freq * 0.05) * np.sin(2 * np.pi * 5 * t) * (t / duration)

    # 9. ULLASITA (Glide/Jaru) - Smooth transition
    gamakas['9. Ullasita'] = np.linspace(base_freq, f_pa, len(t))

    # 10. HUMPITA (Aspirated Accent) - Hum-like aspirated pressure
    humpita = np.full_like(t, base_freq)
    humpita[mid - 50:mid + 50] += (base_freq * 0.1) * np.exp(-((t[mid - 50:mid + 50] - t[mid]) ** 2) / (2 * 0.01 ** 2))
    gamakas['10. Humpita'] = humpita

    # 11. KURULA (Curl/Swing) - "Odugu" style swing
    gamakas['11. Kurula'] = base_freq + (base_freq * 0.06) * np.sin(2 * np.pi * 4 * t + np.pi / 4)

    # 12. TRIBHINNA (Three-fold) - Three strings/notes at once (represented as a triad)
    # We plot the primary and two ghost lines
    gamakas['12. Tribhinna'] = [base_freq, f_ga, f_pa]

    # 13. MUDRITA (Muffled Hum) - Humming with closed lips
    gamakas['13. Mudrita'] = base_freq + (base_freq * 0.01) * np.sin(2 * np.pi * 20 * t)  # Tight, small vibration

    # 14. NAMITA (Modulation) - Thinning/modulating the sound
    gamakas['14. Namita'] = base_freq * (1 - 0.05 * t / duration)  # Tapering frequency/intensity feel

    # 15. MISHRITA (Mixed) - Combination (e.g., Kampita + Jaru)
    gamakas['15. Mishrita'] = np.linspace(base_freq, f_ri, len(t)) + (base_freq * 0.02) * np.sin(2 * np.pi * 10 * t)

    # 16. PRATYAGHATA (Descending Accent) - Inverse of Sphurita
    pratya = np.full_like(t, f_ri)
    pratya[mid:] = base_freq
    pratya[mid:mid + 100] -= (base_freq * 0.08)  # Downward kick
    gamakas['16. Pratyaghata'] = pratya

    return t, gamakas


def plot_all_gamakas():
    base_sa = 240.0
    t, gamakas = generate_all_gamakas(base_sa)

    fig, axes = plt.subplots(4, 4, figsize=(18, 14))
    axes = axes.flatten()

    for i, (name, data) in enumerate(gamakas.items()):
        ax = axes[i]
        if name == '12. Tribhinna':
            # Special case for multi-note representation
            ax.axhline(y=data[0], color='blue', alpha=0.8)
            ax.axhline(y=data[1], color='blue', alpha=0.5, linestyle='--')
            ax.axhline(y=data[2], color='blue', alpha=0.3, linestyle=':')
        else:
            ax.plot(t, data, color='teal', linewidth=2)

        ax.set_title(name, fontsize=10, fontweight='bold')
        ax.set_ylim(base_sa * 0.8, base_sa * 1.6)
        ax.grid(True, alpha=0.3)
        if i >= 12: ax.set_xlabel('Time (s)')
        if i % 4 == 0: ax.set_ylabel('Freq (Hz)')

    plt.suptitle('Frequency Visualization of the 15 Panchadasa Gamakas (+ Pratyaghata)', fontsize=16, y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    plot_all_gamakas()