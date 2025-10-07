import math

# Fungsi iterasi g1A dan g2B (sesuai NIMx = 1)
def g1A(x, y):
    val = 10 - x * y
    if val < 0:
        raise ValueError(f"Error: nilai di bawah akar negatif untuk g1A: 10 - {x}*{y} = {val}")
    return math.sqrt(val)

def g2B(x, y):
    val = (57 - y) / (3 * x) if x != 0 else 0
    if val < 0:
        raise ValueError(f"Error: nilai di bawah akar negatif untuk g2B: (57 - {y}) / (3*{x}) = {val}")
    return math.sqrt(val)

# Iterasi Jacobi
def iterasi_jacobi(x0, y0, epsilon):
    print("Iterasi Jacobi:")
    iterasi = 0
    max_iter = 100
    while True:
        iterasi += 1
        x1 = g1A(x0, y0)
        y1 = g2B(x0, y0)
        print(f"Iterasi ke-{iterasi}: x = {x1:.6f}, y = {y1:.6f}")

        if abs(x1 - x0) < epsilon and abs(y1 - y0) < epsilon:
            break
        if iterasi > max_iter:
            raise RuntimeError("Jacobi: Tidak konvergen setelah 100 iterasi")

        x0, y0 = x1, y1

    return x1, y1

# Iterasi Gauss-Seidel
def iterasi_seidel(x0, y0, epsilon):
    print("Iterasi Seidel:")
    iterasi = 0
    max_iter = 100
    while True:
        iterasi += 1
        x1 = g1A(x0, y0)
        y1 = g2B(x1, y0)  # gunakan x1 terbaru
        print(f"Iterasi ke-{iterasi}: x = {x1:.6f}, y = {y1:.6f}")

        if abs(x1 - x0) < epsilon and abs(y1 - y0) < epsilon:
            break
        if iterasi > max_iter:
            raise RuntimeError("Seidel: Tidak konvergen setelah 100 iterasi")

        x0, y0 = x1, y1

    return x1, y1
