import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection  # Import LineCollection

def get_colormap():
    from matplotlib.colors import LinearSegmentedColormap

    color_min = "firebrick" #"#ff0342"
    color_center = "silver"
    color_max = "aqua" #"#4203ff"
    cmap = LinearSegmentedColormap.from_list(
        "cmap_name",
        [color_min, color_center, color_max]
    )
    return cmap

def generate_circular_wave(x, y, t, amplitude, wavelength, velocity, attenuation_factor):
    """
    Generates a circular wave with attenuation at a given time t.

    Args:
      x: A 1D array of x coordinates.
      y: A 1D array of y coordinates.
      t: The time at which to evaluate the wave.
      amplitude: The initial amplitude of the wave.
      wavelength: The wavelength of the wave.
      velocity: The velocity of the wave.
      attenuation_factor: The factor by which the amplitude decreases with distance.

    Returns:
      A 2D array representing the wave.
    """
    distance = np.sqrt(x**2 + y**2)
    attenuation = np.exp(-attenuation_factor * distance)
    wave = amplitude * attenuation * np.sin(2 * np.pi * (distance / wavelength - velocity * t))
    return wave

# Update the plot for each frame of the animation
def update_plot(frame, axs, x, y, amplitude, wavelength, velocity, attenuation_factor, norm, cmap):
    """
    Updates the plot for each frame of the animation.

    Args:
      frame: The current frame number.
      axs: The axes objects to plot on.
      x: A 1D array of x coordinates.
      y: A 1D array of y coordinates.
      amplitude: The initial amplitude of the wave.
      wavelength: The wavelength of the wave.
      velocity: The velocity of the wave.
      attenuation_factor: The factor by which the amplitude decreases with distance.
      norm: Normalization instance for the colormap.
      cmap: The colormap to use.
    """
    axs[0].clear()
    axs[1].clear()

    timePeriod = wavelength / velocity
    wave = generate_circular_wave(x, y, frame/10, amplitude, wavelength, velocity, attenuation_factor)

    #axs[0].imshow(wave, cmap=cmap, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', norm=norm)
    #axs[0].clim(-10, 10)
    axs[0].imshow(wave, cmap=cmap, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', norm=norm)
    axs[0].plot([0,5],[0,0],'k-')
    axs[0].set_title(f"2D Wave Propagation (Time: {frame/100:.2f}s)")
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].set_xticks([-5, 0, 5])
    axs[0].set_yticks([-5, 0, 5])

    # Use the colormap for the 1D plot (Corrected with LineCollection)
    points = np.array([x[100,:], wave[100,:]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(wave[100,:])
    axs[1].add_collection(lc)

    axs[1].set_title(f"1D Wave Propagation (Time: {frame/100:.2f}s)")
    axs[1].set_xlabel('Radius')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_ylim([-amplitude, amplitude])
    axs[1].set_ylim([-5, 5])
    axs[1].set_xlim([0, 5])
    axs[1].set_xticks([axs[1].get_xticks()[0], axs[1].get_xticks()[-1]])
    axs[1].set_yticks([-5, 0, 5])


def create2D1DWaves(amplitude, wavelength, velocity, attenuation_factor, filename="wave_plot.png"):
    # Set up the x and y coordinates
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    x, y = np.meshgrid(x, y)

    timePeriod = wavelength/velocity

    # Create the initial plot
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Create the colormap and normalization
    cmap = plt.get_cmap('RdBu')
    cmap = get_colormap()
    norm = Normalize(vmin=-amplitude, vmax=amplitude)
    #Fixing colormap range
    #norm = Normalize(vmin=-5, vmax=5)

    # Create the animation
    wave_ani = FuncAnimation(fig, update_plot, frames=100*int(timePeriod), fargs=(axs, x, y, amplitude, wavelength, velocity, attenuation_factor, norm, cmap), interval=50)

    cir_plot = axs[0].imshow(generate_circular_wave(x, y, 0, amplitude, wavelength, velocity, attenuation_factor), cmap=cmap, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', norm=norm)
    fig.colorbar(cir_plot, ax=axs[1])
    # Save the animation in a png file
    #wave_ani.save(filename, savefig_kwargs={'bbox_inches':'tight', 'pad_inches':0})

    # Display the animation
    plt.show()


