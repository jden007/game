import pygame

# เริ่มต้น Pygame
pygame.init()

# ตั้งค่าหน้าจอ
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("เกมตัวละครขยับได้")

# ตั้งค่าสี
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# สร้างตัวละคร (เป็นสี่เหลี่ยม)
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# ลูปหลักของเกม
running = True
while running:
    pygame.time.delay(30)  # หน่วงเวลาเล็กน้อยเพื่อให้เกมไม่เร็วเกินไป

    # เช็กเหตุการณ์ (event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # คีย์บอร์ดควบคุม
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # ล้างหน้าจอ
    screen.fill(WHITE)

    # วาดตัวละคร
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # อัปเดตหน้าจอ
    pygame.display.update()

# ปิดเกม
pygame.quit()
