import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, YELLOW, WHITE, GREEN
from checkers.piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 6
        self.red_kings = self.white_kings = 0
        self.create_board()
    def draw_square(self, window):   # CREATING A BAGROUND
        window.fill(GREEN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, YELLOW, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # if the loops statisfies then piece is drawn in the board (0%2 == ((0+1))%2) draw only on even cols
                    if row < 2:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 3:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)  # for the blank spaces
                else:
                    self.board[row].append(0)

    def draw(self, window):
        self.draw_square(window)   # CALL BG WINDOW
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:   # WHEN SQUARE IS NOT EQUAL TO 0 THEN PIECE WILL BE DRAWN
                    piece.draw(window)