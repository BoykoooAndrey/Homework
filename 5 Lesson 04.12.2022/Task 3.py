import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Ничья'
    return False


pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

size_block = 200
margin = 15
width = hight = size_block*3 + margin*4
size_window = (width, hight)
mas = []
for i in range(3):
    mas.append([0]*3)
query = 0
game_over = False

screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')
img = pygame.image.load('Caption.jpg')
pygame.display.set_icon(img)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse} y={y_mouse}')
            col = x_mouse // (margin+size_block)
            row = y_mouse // (margin+size_block)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = []
            for i in range(3):
                mas.append([0]*3)
            query = 0
            screen.fill(BLACK)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = RED
                elif mas[row][col] == 'o':
                    color = GREEN
                else:
                    color = WHITE
                x = col*size_block + (col+1)*margin
                y = row*size_block + (row+1)*margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == RED:
                    pygame.draw.line(screen, BLACK, (x+10, y+10),
                                     (x+size_block-10, y+size_block-10), 3)
                    pygame.draw.line(
                        screen, BLACK, (x+size_block-10, y+10), (x+10, y+size_block-10), 3)
                if color == GREEN:
                    pygame.draw.circle(
                        screen, BLACK, (x + (size_block//2), y + (size_block//2)), (size_block//2-5), 3)
    if (query-1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')
    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont("stxingkai", 80)
        text1 = font.render(game_over, True, WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width()/2 - text_rect.width / 2
        text_y = screen.get_height()/2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()
