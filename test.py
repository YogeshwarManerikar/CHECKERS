pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))

# os.path.join properly forms a cross-platform relative path
# by joining directory names

bg = pygame.transform.scale(pygame.image.load('assets/bg.png'), (600, 600))


pygame.mouse.set_visible(0)



pygame.display.set_caption('Checkers')

# fix indentation
g=Ga,e()
while True:
    clock.tick(60)

    screen.blit(bg, (0,0))
    g.curr_menu.display_menu()
    g.game_loop()



    pygame.display.update()