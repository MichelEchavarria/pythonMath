import numpy as np
import matplotlib.pyplot as plt

# AUN EN DESARROLLO. NO LOGRO LEVANTAR EL FRACTAL MALDITO!!!!!!!1

def f(z):
    return z**3 - 1

def f_prime(z):
    return 3 * z**2

def newton_method(z):
    iterations = 0
    while iterations < 100:
        z = z - f(z) / f_prime(z)
        iterations += 1
    return z

xmin, xmax = -2, 2
ymin, ymax = -2, 2
n_points = 1000

x = np.linspace(xmin, xmax, n_points)
y = np.linspace(ymin, ymax, n_points)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

Z_newton = np.zeros_like(Z, dtype=np.complex128)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z_newton[i, j] = newton_method(Z[i, j])

roots = [1, np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3)]

mask = np.zeros_like(Z_newton, dtype=bool)
for root in roots:
    mask |= np.isclose(Z_newton, root, atol=1e-3)

plt.imshow(mask.T, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
plt.colorbar(label='Convergencia')
plt.title('Fractal del Conjunto de Newton')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()