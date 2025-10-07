# Definisi fungsi sistem
def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

# Metode Secant untuk sistem dua variabel
def secant_method(f1, f2, x0, y0, x1, y1, epsilon):
    iterasi = 0

    while True:
        f1x0, f2x0 = f1(x0, y0), f2(x0, y0)
        f1x1, f2x1 = f1(x1, y1), f2(x1, y1)

        # Hitung perubahan tiap variabel
        dx = (x1 - x0) * f1x1 / (f1x1 - f1x0)
        dy = (y1 - y0) * f2x1 / (f2x1 - f2x0)

        # Update nilai baru
        x2, y2 = x1 - dx, y1 - dy
        iterasi += 1

        # Cek konvergensi
        if abs(x2 - x1) < epsilon and abs(y2 - y1) < epsilon:
            break

        x0, y0, x1, y1 = x1, y1, x2, y2

    return x2, y2, iterasi
