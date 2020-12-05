WIDTH, HEIGHT = 600, 600
ROWS, COLS = 0, 2
SQUARE_SIZE = WIDTH//COLS

x = SQUARE_SIZE * ROWS + SQUARE_SIZE // 2
y = SQUARE_SIZE * COLS+ SQUARE_SIZE // 2

print("position where circle will draw =( %d , %d )" %(x,y))