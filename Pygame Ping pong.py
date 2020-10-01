import pygame
pygame.init()

win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong Game')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
navyblue = (0, 0, 128)
orange = (255, 165, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(navyblue)
        self.rect = self.image.get_rect()
        self.speed = 20
        self.dx = 1
        self.dy = 1


paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

paddle_speed = 20

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)

def redraw():
    win.fill(white)
    # Title Font
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('PONG', False, black)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    win.blit(text, textRect)

    # Player1 Score title
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('Player 1', False, green)
    textRect = text.get_rect()
    textRect.center = (70, 20)
    win.blit(text, textRect)
    # PLayer1 score
    p1_score = font.render(str(paddle1.points), False, green)
    p1_Rect = p1_score.get_rect()
    p1_Rect.center = (60, 60)
    win.blit(p1_score, p1_Rect)


    # Player2 Score Title
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('Player 2', False, red)
    textRect = text.get_rect()
    textRect.center = (650, 20)
    win.blit(text, textRect)
    # PLayer2 score
    p2_score = font.render(str(paddle2.points), False, red)
    p2_Rect = p2_score.get_rect()
    p2_Rect.center = (675, 60)
    win.blit(p2_score, p2_Rect)

    all_sprites.draw(win)
    pygame.display.update()


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_1]:
        paddle1.rect.y += - paddle_speed
    if key[pygame.K_TAB]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y += - paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed


    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    if pong.rect.y > 490:
        pong.dy = -1
    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        paddle1.points += 1
    if pong.rect.y < 10:
        pong.dy = 1
    if pong.rect.x < 10:
        pong.rect.x, pong.rect.y = 380, 250
        pong.dx = 1
        paddle2.points += 1

    if paddle1.rect.colliderect(pong.rect):
        pong.dx += 1
    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1
    redraw()

pygame.quit()