## TODO: Make the waves circular arising from a stone dropped in water

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1D Wave
def wave1d(x, t, A=1, k=1, w=1):
    return A * np.sin(k * x - w * t)

# 2D Wave
def wave2d(x, y, t, A=1, kx=1, ky=1, w=1):
    return A * np.sin(kx * x + ky * y - w * t)

# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 1D Wave Visualization
x = np.linspace(0, 10, 100)
line, = axs[0].plot(x, wave1d(x, 0))
axs[0].set_title('1D Wave')

# 2D Wave Visualization
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
img = axs[1].imshow(wave2d(X, Y, 0), cmap='coolwarm', extent=[0, 10, 0, 10])
axs[1].set_title('2D Wave')

# Animation Function
def animate(i):
    line.set_ydata(wave1d(x, i/10))
    img.set_data(wave2d(X, Y, i/10))
    return line, img

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()