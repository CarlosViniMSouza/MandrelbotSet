from mandelbrot import MandelbrotSet
from dataclasses import dataclass
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c


print(z(2, 4))
# Output: 20

for n in range(10):
    print(f"z({n}) = {z(n, c=1)}")


def sequence(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c


for n, z in enumerate(sequence(c=1)):
    print(f"z({n}) = {z}")
    if n >= 9:
        break


def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c
        return z


print(sequence(c=4, z=0))


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


print(complex_matrix(2, 8, 3, 6, 0.5))


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2


print(is_stable(4, 10))


def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


np.warnings.filterwarnings("ignore")


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
image = Image.fromarray(~is_stable(c, num_iterations=20))
image.show()

img = Image.effect_mandelbrot((512, 512), (-3, -2.5, 2, 2.5), 100).show()


def is_stable(c, max_iterations):
    z = 0
    for _ in range(max_iterations):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True


is_stable(0.26, max_iterations=20)

is_stable(0.26, max_iterations=30)


@dataclass
class MandelbrotSet:
    max_iterations: int

    def __contains__(self, c: complex) -> bool:
        z = 0
        for _ in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                return False
        return True


mandelbrot_set = MandelbrotSet(max_iterations=30)
0.26 in mandelbrot_set
0.26 not in mandelbrot_set
