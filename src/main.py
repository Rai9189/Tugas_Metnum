from iterasi_titik_tetap import iterasi_jacobi, iterasi_seidel
from newton_raphson import newton_raphson
from secant import secant_method, f1, f2

def main():
    epsilon = 1e-6
    # Tebakan awal aman
    x0, y0 = 1.0, 2.0

    print("=== Iterasi Titik Tetap (Jacobi) ===")
    try:
        hasil_jacobi = iterasi_jacobi(x0, y0, epsilon)
        print(f"Solusi Jacobi: x = {hasil_jacobi[0]:.6f}, y = {hasil_jacobi[1]:.6f}\n")
    except ValueError as e:
        print(f"Jacobi error: {e}\n")

    print("=== Iterasi Titik Tetap (Seidel) ===")
    try:
        hasil_seidel = iterasi_seidel(x0, y0, epsilon)
        print(f"Solusi Seidel: x = {hasil_seidel[0]:.6f}, y = {hasil_seidel[1]:.6f}\n")
    except ValueError as e:
        print(f"Seidel error: {e}\n")

    print("=== Newton-Raphson ===")
    hasil_newton = newton_raphson(x0, y0, epsilon)
    print(f"Solusi Newton-Raphson: x = {hasil_newton[0]:.6f}, y = {hasil_newton[1]:.6f}\n")

    print("=== Secant ===")
    # Tebakan awal untuk Secant: x0,y0 dan x1,y1 sedikit berbeda
    hasil_secant = secant_method(f1, f2, 1.0, 2.0, 1.1, 2.1, epsilon)
    print(f"Solusi Secant: x = {hasil_secant[0]:.6f}, y = {hasil_secant[1]:.6f}\n")

if __name__ == "__main__":
    main()
