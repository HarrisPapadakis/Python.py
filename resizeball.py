import pygame
import sys

pygame.init()

# Διαστάσεις παραθύρου
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Μπάλα που μεγαλώνει")

# Χρώματα
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ήχος
growth_sound = pygame.mixer.Sound("pop.wav")  # Φρόντισε να υπάρχει αυτό το αρχείο

# Ιδιότητες μπάλας
ball_radius = 20
MAX_RADIUS = 100
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5

# Σημείο αύξησης
grow_point = pygame.Rect(100, 100, 30, 30)

# Ρολόι
clock = pygame.time.Clock()

# Παιχνίδι loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Κινήσεις
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    # Σύγκρουση
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    if ball_rect.colliderect(grow_point):
        if ball_radius < MAX_RADIUS:
            ball_radius += 5  # Μεγαλώνει πιο γρήγορα
            growth_sound.play()
        # Μετακίνηση νέου σημείου
        grow_point.x = pygame.mouse.get_pos()[0]
        grow_point.y = pygame.mouse.get_pos()[1]

    # Σχεδίαση
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, BLUE, grow_point)
    pygame.display.flip()
    clock.tick(60)
