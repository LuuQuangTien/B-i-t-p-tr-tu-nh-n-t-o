import pygame
import numpy as np
from Tile import Tile

pygame.init()

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("8 Puzzle")
text = pygame.font.Font(None, 50)
running = True
win_flag = False
win_condition = np.arange(9).reshape(3, 3)
"""print(win_condition)"""

def Can_be_solved(begin_game):
    temp = np.copy(begin_game[begin_game != 0].flatten())
    count = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if(temp[i] > temp[j]):
                count += 1
    return (count % 2 == 0)
while(True):
    begin_game = np.random.permutation(win_condition.flatten()).reshape(3, 3)
    if(Can_be_solved(begin_game)):
        break

def Find_index(begin_game, num):
    index = np.where(begin_game == num)
    return (index[0][0], index[1][0])

def Check_Blank(begin_game, num):
    row_blank, column_blank = Find_index(begin_game, 0)
    row_tile, column_tile = Find_index(begin_game, num)
    return (abs(column_tile - column_blank) + abs(row_tile - row_blank) == 1)

def Move_Tile(begin_game, num):
    if(Check_Blank(begin_game, num)):
        row_blank, column_blank = Find_index(begin_game, 0)
        row_tile, column_tile = Find_index(begin_game, num)
        begin_game[row_blank, column_blank] = begin_game[row_tile, column_tile]
        begin_game[row_tile, column_tile] = 0

def Check_Win(begin_game):
    return np.array_equal(begin_game, win_condition)

while(running):
    screen.fill((255, 255, 255))
    screen.blit(text.render("8 Puzzle", True, (0, 0, 0)), (80, 10))
    if(win_flag):
        screen.fill((255, 255, 255))
        win_text = text.render("You Win", True, (0, 0, 0))
        screen.blit(win_text, (80, 200))
        pygame.display.flip()
    else:
        tiles = []
        tile_size = 100
        for row in range(3):
            for col in range(3):
                num = begin_game[row, col]
                x, y = col * tile_size, row * tile_size + 80
                tile = Tile(screen, (200, 200, 200), x, y, tile_size, num, text)
                tiles.append(tile)
        for tile in tiles:
            tile.Draw()

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if(80 <= mouse_y < (80 + 3 * tile_size) and 0 <= mouse_x < (3 * tile_size)):
                column = mouse_x // tile_size
                row = (mouse_y - 80) // tile_size
                if(row < 3 and column < 3): value = begin_game[row, column]

                """Move_Tile(begin_game, value)
                print(begin_game)"""

                print(Check_Win(begin_game))
                if(Check_Win(begin_game)):
                    win_flag = True
    pygame.display.flip()
pygame.quit()