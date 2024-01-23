import pygame
from random import randrange

WINDOW = 800SIZE = 50x, y = randrange(0, WINDOW, SIZE), randrange(0, WINDOW, SIZE)
apple = randrange(0, WINDOW, SIZE), randrange(0, WINDOW, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1snake = [(x, y)]
dx, dy = 0, 0fps = 5score = 0pygame.init()
screen = pygame.display.set_mode([WINDOW, WINDOW])
clock = pygame.time.Clock()
front_score = pygame.font.SysFont('Arial', 26, bold=True)
front_end = pygame.font.SysFont('Arial', 66, bold=True)

while True:
    screen.fill(pygame.Color('black'))

    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = front_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[- length:]

    if snake[-1] == apple:
        apple = randrange(0, WINDOW, SIZE), randrange(0, WINDOW, SIZE)
        length += 1        score += 1        fps += 1    if x < 0 or x > WINDOW - SIZE or y < 0 or y > WINDOW - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = front_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (WINDOW // 2 - 200, WINDOW // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0        dirs = {'W': True, 'S': True, 'A': False, 'D': True}