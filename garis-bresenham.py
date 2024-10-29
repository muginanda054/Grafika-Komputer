import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritma Bresenham untuk Menggambar Garis")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fungsi Algoritma Bresenham
def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
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

    # Gambarkan garis menggunakan algoritma Bresenham
    for point in bresenham_line(x1, y1, x2, y2):
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
