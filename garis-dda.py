import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritma DDA untuk Menggambar Garis")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fungsi Algoritma DDA
def dda_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1

    # Menentukan jumlah langkah yang dibutuhkan
    steps = max(abs(dx), abs(dy))

    # Hitung peningkatan x dan y per langkah
    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x1, y1
    for _ in range(int(steps) + 1):
        points.append((round(x), round(y)))  # Menyimpan titik-titik pada garis
        x += x_increment
        y += y_increment
    return points

# Ambil input dari pengguna
try:
    x1 = int(input("Masukkan x1: "))
    y1 = int(input("Masukkan y1: "))
    x2 = int(input("Masukkan x2: "))
    y2 = int(input("Masukkan y2: "))
except ValueError:
    print("Masukkan angka yang valid.")
    sys.exit()

# Jalankan aplikasi
running = True
while running:
    screen.fill(WHITE)

    # Gambarkan garis menggunakan algoritma DDA
    for point in dda_line(x1, y1, x2, y2):
        if 0 <= point[0] < WIDTH and 0 <= point[1] < HEIGHT:
            screen.set_at(point, BLACK)

    # Tampilkan perubahan
    pygame.display.flip()

    # Periksa event untuk keluar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keluar dari pygame
pygame.quit()
sys.exit()
