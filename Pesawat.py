import pygame
import random

# Inisialisasi
pygame.init()

# Ukuran layar
width = 600
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Tembak Pesawat")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(275, 600, 50, 50)
player_speed = 7

# Peluru
bullets = []
bullet_speed = 10

# Musuh
enemies = []
enemy_speed = 3

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True

# ======================
# GAME LOOP
# ======================
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x + 20, player.y, 10, 20))

    # Gerakan player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < width - 50:
        player.x += player_speed

    # Spawn musuh
    if random.randint(1, 30) == 1:
        enemies.append(pygame.Rect(random.randint(0, width-40), 0, 40, 40))

    # Gerakan peluru
    for bullet in bullets:
        bullet.y -= bullet_speed

    # Gerakan musuh
    for enemy in enemies:
        enemy.y += enemy_speed

    # Deteksi tabrakan
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Hapus objek keluar layar
    bullets = [b for b in bullets if b.y > 0]
    enemies = [e for e in enemies if e.y < height]

    # Gambar player
    pygame.draw.rect(screen, WHITE, player)

    # Gambar peluru
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)

    # Gambar musuh
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)

    # Tampilkan skor
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()