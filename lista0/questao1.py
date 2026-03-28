import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

A = np.array([
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [8, 4, 2, 1],
    [27, 9, 3, 1]
])

B = np.array([
    1, 0, -1, 2
])

coefficients = np.linalg.solve(A, B)
fracoes = [Fraction(c).limit_denominator() for c in coefficients]
a_frac,b_frac,c_frac,d_frac = fracoes

print(coefficients)

print("System solution:")
print(f"a = {a_frac}")
print(f"b = {b_frac}")
print(f"c = {c_frac}")
print(f"d = {d_frac}")
print(f"\nThe polynomial is: f(x) = {a_frac}x³ + {b_frac}x² + {c_frac}x + {d_frac}")

a,b,c,d = coefficients
x_curve = np.linspace(-0.5, 3.5, 100)
y_curve = a * x_curve**3 + b * x_curve**2 + c * x_curve + d

x_points = [0, 1, 2, 3]
y_points = [1, 0, -1, 2]

plt.figure(figsize=(8, 6))
plt.plot(x_curve, y_curve, color='blue', label='Interpolating Polynomial')
plt.scatter(x_points, y_points, color='red', zorder=5, label='Points P_i')

plt.title('Cubic Polynomial Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.savefig('lista0/images/graph.png', dpi=300, bbox_inches='tight')
