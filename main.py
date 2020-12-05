# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.board import Board
from checkers.game import Game
FPS = 60

pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    g = Game()

    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


main()
