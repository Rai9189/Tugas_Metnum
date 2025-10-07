import numpy as np

# Definisi fungsi
def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

# Newton-Raphson untuk sistem dua variabel
def newton_raphson(x0, y0, epsilon):
    iterasi = 0

    while True:
        # Matriks Jacobian
        J = np.array([
            [2*x0 + y0, x0],
            [3*y0**2, 1 + 6*x0*y0]
        ])

        # Vektor fungsi
        F = np.array([f1(x0, y0), f2(x0, y0)])

        # Pecahkan sistem linear J * delta = -F
        delta = np.linalg.solve(J, -F)

        # Update nilai x dan y
        x1, y1 = x0 + delta[0], y0 + delta[1]
        iterasi += 1

        # Cek konvergensi
        if max(abs(delta)) < epsilon:
            break

        x0, y0 = x1, y1

    return x1, y1, iterasi
