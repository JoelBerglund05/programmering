import pygame
from pygame.locals import *
import random
import button
 
pygame.init()
 
#display settings
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('box Game')

#games variables
game_pause = True
game_face_1 = False
game_face_2 = False
game_face_3 = False

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colors
text_col = (0, 0, 0)

#text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    game_display.blit(img, (x, y))

#buttons
menu_btn_play = pygame.image.load('pygame/test.svg').convert_alpha()
menu_btn_exit = pygame.image.load('pygame/exit_btn.png').convert_alpha()
select_btn = pygame.image.load('pygame/select_btn.png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, menu_btn_play, 2)
exit_button = button.Button(450, 200, menu_btn_exit, .8)
select_button = button.Button(350, 400, select_btn, 1)

#box images
box_1_img = pygame.image.load('pygame/box.png').convert_alpha()
box_2_img = pygame.image.load('pygame/box.png').convert_alpha()
box_3_img = pygame.image.load('pygame/box.png').convert_alpha()

#create box instances
box_1 = button.Button(50, 200, box_1_img, 1)
box_2 = button.Button(350, 200, box_1_img, 1)
box_3 = button.Button(650, 200, box_1_img, 1)

#box selection
box_choice = [0, 0, 0]

def random_win_box():

    win_box = random.randint(0, 2)

    box_choice.insert(win_box, 1)

    tabort = box_choice.pop(3)

def win_text():
    if box_choice[0] == 1:
        draw_text("Win!", font, text_col, 50, 200)
    elif box_choice[1] == 1:
        draw_text("Win!", font, text_col, 350, 200)
    elif box_choice[2] == 1:
        draw_text("Win!", font, text_col, 650, 200)


#event handeler
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


while True:

    game_display.fill((202, 228, 241))

    draw_text("Box spelet", font, text_col, 300, 50)


    #game faces
    if game_pause == True:
        if start_button.draw(game_display):
            game_pause = False
            game_face_1 = True
        if exit_button.draw(game_display):
            pygame.quit()
            quit()
    elif game_face_1 == True:
        random_win_box()

        if box_1.draw(game_display):
            if select_button.draw(game_display):
                box_choice.insert(0, 2)
                box_choice_removed = box_choice.pop(1)
                game_face_1 = False
                game_face_2 = True
        elif box_2.draw(game_display):
            if select_button.draw(game_display):
                box_choice.insert(1, 2)
                box_choice_removed = box_choice.pop(2)
                game_face_1 = False
                game_face_2 = True
        elif box_3.draw(game_display):
            if select_button.draw(game_display):
                box_choice.insert(2, 2)
                box_choice_removed = box_choice.pop(3)
                game_face_1 = False
                game_face_2 = True
    elif game_face_2 == True:
        pass
        

    pause = pygame.key.get_pressed()

    if pause[pygame.K_ESCAPE]:
        game_pause = True
        game_face_1 = False
        game_face_2 = False
        game_face_3 = False

    event_handler()

    pygame.display.update()