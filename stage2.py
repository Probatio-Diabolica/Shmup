import pygame
import math

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Homing Bullet Test_1")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SQUARE_SIZE = 40
square = pygame.Rect(WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE)

BULLET_SIZE = 5
BULLET_SPEED = 6
HOMING_STRENGTH = 0.01
bullets = []

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self, target_x, target_y):
        tx = target_x - self.x
        ty = target_y - self.y
        dist = math.hypot(tx, ty)
        
        if dist != 0:
            tx, ty = tx / dist, ty / dist

        self.dx = self.dx * (1 - HOMING_STRENGTH) + tx * HOMING_STRENGTH * BULLET_SPEED
        self.dy = self.dy * (1 - HOMING_STRENGTH) + ty * HOMING_STRENGTH * BULLET_SPEED

        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), BULLET_SIZE)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mx, my = pygame.mouse.get_pos()
                dx = mx - square.centerx
                dy = my - square.centery
                distance = math.hypot(dx, dy)
                dx, dy = dx / distance * BULLET_SPEED, dy / distance * BULLET_SPEED

                bullets.append(Bullet(square.centerx, square.centery, dx, dy))
                bullets.append(Bullet(square.centerx, square.centery, -dx, -dy))


    mx, my = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))


    pygame.draw.rect(screen, BLUE, square)


    for bullet in bullets[:]:
        bullet.move(mx, my)
        bullet.draw()
        

        if not screen.get_rect().collidepoint((bullet.x, bullet.y)):
            bullets.remove(bullet)


    pygame.draw.circle(screen, WHITE, (mx, my), 5)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
