import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritma Brute Force untuk Menggambar Garis")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fungsi Algoritma Brute Force
def brute_force_line(x1, y1, x2, y2):
    points = []
    if x1 == x2:  # Garis vertikal
        y_min, y_max = min(y1, y2), max(y1, y2)
        for y in range(y_min, y_max + 1):
            points.append((x1, y))
    elif y1 == y2:  # Garis horizontal
        x_min, x_max = min(x1, x2), max(x1, x2)
        for x in range(x_min, x_max + 1):
            points.append((x, y1))
    else:
        # Menghitung kemiringan (slope)
        m = (y2 - y1) / (x2 - x1)
        # Menggambar dari x1 ke x2
        if abs(x2 - x1) > abs(y2 - y1):  # Berdasarkan perbedaan x
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1  # Pastikan x1 < x2
            for x in range(x1, x2 + 1):
                y = y1 + round(m * (x - x1))
                points.append((x, y))
        else:  # Berdasarkan perbedaan y
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1  # Pastikan y1 < y2
            for y in range(y1, y2 + 1):
                x = x1 + round((y - y1) / m)
                points.append((x, y))
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

    # Gambarkan garis menggunakan algoritma brute force
    for point in brute_force_line(x1, y1, x2, y2):
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
