import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def plot_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    image = np.zeros((width, height))
    fig, ax = plt.subplots()
    im = ax.imshow(image, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar(im)
    plt.show(block=False)  # No bloquear la ejecución para permitir la visualización gradual

    for x in range(width):
        for y in range(height):
            re = xmin + (xmax - xmin) * x / width
            im_parte_imaginaria = ymin + (ymax - ymin) * y / height
            c = re + 1j * im_parte_imaginaria
            n = mandelbrot(c, max_iter)
            color = n / max_iter
            image[x, y] = color
        im.set_data(image)
        plt.draw()
        plt.pause(0.001)  # Pausa para ver la actualización gradual del fractal

    plt.show()

# Parámetros del fractal
xmin, xmax = -2.5, 1.5
ymin, ymax = -2, 2
width, height = 800, 800
max_iter = 1200

# Dibujar el fractal de Mandelbrot
plot_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
