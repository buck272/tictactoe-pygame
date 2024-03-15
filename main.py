# importing modules needed
import pygame
import random
from sys import exit

# initializing pygame
pygame.init()

# coordinates
choice_cells = [[40, 40],  [190, 40],  [340, 40],
                [40, 190], [190, 190], [340, 190],
                [40, 340], [190, 340], [340, 340]]

computer_cells = [[40, 40],  [190, 40],  [340, 40],
                  [40, 190], [190, 190], [340, 190],
                  [40, 340], [190, 340], [340, 340]]

def reset_game(choice_cells, cells_status):
    choice_cells = [[40, 40],  [190, 40],  [340, 40],
                    [40, 190], [190, 190], [340, 190],
                    [40, 340], [190, 340], [340, 340]]    
    return choice_cells, cells_status

# creating a screen
screen = pygame.display.set_mode((500, 500))
screen.fill("cadetblue1")

# screen overlay
overlay = pygame.Surface((500, 500))
overlay.fill("cadetblue1")

# set title to window
pygame.display.set_caption("TIC-TAC-TOE")

# set framerate
clock = pygame.time.Clock()

class Text(object):
    def __init__(self, width, height, box_color, text, text_color, font_size):
        self.width = width
        self.height = height
        self.box_color = box_color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        
    def render_text(self):
        text_block = pygame.Surface((self.width, self.height))
        text_block.fill(self.box_color)
        font = pygame.font.SysFont("Broadway", self.font_size)
        text = font.render(self.text, True, self.text_color)
        text_surface = text.get_rect()
        text_block.blit(text, text_surface)
        return text_block
    
class Button(object):
    def __init__(self, width, height, btn_color, text, text_color, font_size):
        self.width = width
        self.height = height
        self.btn_color = btn_color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size   
         
    def render_button(self):  
        button_block = pygame.Surface((self.width, self.height))  
        button_block.fill(self.btn_color)
        font_to_use = pygame.font.SysFont("Broadway", self.font_size)
        text_to_render = font_to_use.render(self.text, True, self.text_color)
        text_surface = text_to_render.get_rect()
        text_surface.center = (self.width / 2, self.height / 2)
        button_block.blit(text_to_render, text_surface)
        return button_block

def draw_board():
    board_surface = pygame.Surface((450, 450))
    board_surface.fill("white")
    pygame.draw.line(board_surface, color="black", start_pos=(150, 5), end_pos=(150, 445), width=5)
    pygame.draw.line(board_surface, color="black", start_pos=(300, 5), end_pos=(300, 445), width=5)
    pygame.draw.line(board_surface, color="black", start_pos=(5, 150), end_pos=(445, 150), width=5)
    pygame.draw.line(board_surface, color="black", start_pos=(5, 300), end_pos=(445, 300), width=5)
    screen.blit(board_surface, [25, 25])
    return board_surface
    
def draw_circle():
    circle_surface = pygame.Surface((120, 120))
    circle_surface.fill("white")
    pygame.draw.circle(circle_surface, color="blue", center=(60, 60), radius=50, width=10)
    return circle_surface

def draw_x():
    x_surface = pygame.Surface((120, 120))
    x_surface.fill("white")
    pygame.draw.line(x_surface, color="black", start_pos=(25, 25), end_pos=(95, 95), width=10)
    pygame.draw.line(x_surface, color="black", start_pos=(95, 25), end_pos=(25, 95), width=10)
    return x_surface

# intro screen
intro = True
while intro:    
    intro_text = Text(395, 62, "cadetblue1", "TIC-TAC-TOE", "cyan4", 60)
    screen.blit(intro_text.render_text(), [55, 150])
    
    play_button = Button(220, 70, "cyan4", "PLAY", "cadetblue1", 50)
    screen.blit(play_button.render_button(), [145, 250])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            intro = False
            exit()
    
    x, y = pygame.mouse.get_pos()
    if (x >= 145 and x <= 145 + 220) and (y >= 250 and y <= 250 + 70):
        play_button_hover = Button(220, 70, "cyan3", "PLAY", "cadetblue1", 50)
        screen.blit(play_button_hover.render_button(), [145, 250])

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if (x >= 145 and x <= 145 + 220) and (y >= 250 and y <= 250 + 70):
            intro = False
            
    # display settings
    pygame.display.update()
    clock.tick(60)
    
pygame.event.wait()

mode = True
while mode:
    screen.blit(overlay, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mode = False
            quit()
    
    vs_computer = Button(250, 70, "cyan4", "VS COMPUTER", "cadetblue1", 30)
    screen.blit(vs_computer.render_button(), [130, 150])
    
    vs_player = Button(250, 70, "cyan4", "VS PLAYER", "cadetblue1", 30)
    screen.blit(vs_player.render_button(), [130, 250])
    
    x, y = pygame.mouse.get_pos()
    if (x >= 130 and x <= 130 + 250) and (y >= 150 and y <= 150 + 70):
        vs_computer_hover = Button(250, 70, "cyan3", "VS COMPUTER", "cadetblue1", 30)
        screen.blit(vs_computer_hover.render_button(), [130, 150])
    elif (x >= 130 and x <= 130 + 250) and (y >= 250 and y <= 250 + 70):
        vs_player_hover = Button(250, 70, "cyan3", "VS PLAYER", "cadetblue1", 30)
        screen.blit(vs_player_hover.render_button(), [130, 250])
    
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if (x >= 130 and x <= 130 + 250) and (y >= 150 and y <= 150 + 70):
            set_mode = "vs_computer"
            mode = False
        elif (x >= 130 and x <= 130 + 250) and (y >= 250 and y <= 250 + 70):
            set_mode = "vs_player"
            mode = False
        
    pygame.display.update()
    # game framerate set to 60fps
    clock.tick(60)

pygame.event.wait()    

clicked = False
player = 1
turn = 0
coordinates = [[],[],[],
               [],[],[],
               [],[],[]]
checker = [0, 0, 0,
           0, 0, 0,
           0, 0, 0]

computer_choice = []

def draw_marker():
    for item in coordinates:
        if len(item) > 0:
            if item[2] == 1:
                screen.blit(draw_x(), (item[0], item[1]))
            elif item[2] == -1:
                screen.blit(draw_circle(), (item[0], item[1]))

def check_winner():
    winner = 0
    running = True
    player_1 = [1, 1, 1]
    player_2 = [-1, -1, -1]
    if checker[:3] == player_1 or checker[3:6] == player_1 or checker[6:] == player_1 or checker[0::4] == player_1 or \
        checker[2:7:2] == player_1 or checker[0:7:3] == player_1 or checker[1:8:3] == player_1 or checker[2::3] == player_1:
        winner = 1
        running = False
    elif checker[:3] == player_2 or checker[3:6] == player_2 or checker[6:] == player_2 or checker[0::4] == player_2 or \
        checker[2:7:2] == player_2 or checker[0:7:3] == player_2 or checker[1:8:3] == player_2 or checker[2::3] == player_2:
        winner = -1
        running = False
    return winner, running
    
if set_mode == 'vs_player':
    # game running
    running = True
    while running:
        screen.blit(overlay, [0, 0])
        draw_board()
        draw_marker()
        winner, running = check_winner()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked == False
                x, y = pygame.mouse.get_pos()
                for i in range(len(choice_cells)):
                    if (x >= choice_cells[i][0] and x <= choice_cells[i][0] + 120) and (y >= choice_cells[i][1] and y <= choice_cells[i][1] + 120):
                        if coordinates[i] == []:
                            coordinates[i] = choice_cells[i]
                            coordinates[i].append(player)
                            checker[i] = player
                            player *= -1
        #print(winner)
        pygame.display.update()
        # game framerate set to 60fps
        clock.tick(60)
    if winner == 1:
        winner_screen = True
        while winner_screen:
            intro_text = Text(395, 62, "cadetblue1", "Player 'X' WON!", "cyan4", 48)
            screen.blit(intro_text.render_text(), [55, 150])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit()
                    
            pygame.display.update()
            # game framerate set to 60fps
            clock.tick(60)
    elif winner == -1:
        winner_screen = True
        while winner_screen:
            intro_text = Text(395, 62, "cadetblue1", "Player 'O' WON!", "cyan4", 48)
            screen.blit(intro_text.render_text(), [55, 150])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit()
                    
            pygame.display.update()
            # game framerate set to 60fps
            clock.tick(60)
elif set_mode == 'vs_computer':
    # game running
    running = True
    while running:
        screen.blit(overlay, [0, 0])
        draw_board()
        draw_marker()
        winner, running = check_winner()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit()
            if player == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked == False
                    x, y = pygame.mouse.get_pos()
                    for i in range(len(choice_cells)):
                        if (x >= choice_cells[i][0] and x <= choice_cells[i][0] + 120) and (y >= choice_cells[i][1] and y <= choice_cells[i][1] + 120):
                            if coordinates[i] == []:
                                coordinates[i] = choice_cells[i]
                                coordinates[i].append(player)
                                checker[i] = player
                                player *= -1
            if player == -1:
                computer_choice = random.choice(computer_cells)
                for i in range(len(choice_cells)):
                    if choice_cells[i] == computer_choice and coordinates[i] == []:
                        coordinates[i] = choice_cells[i]
                        coordinates[i].append(player)
                        checker[i] = player
                        player *= -1
                computer_cells.remove(computer_choice)         
        pygame.display.update()
        # game framerate set to 60fps
        clock.tick(60)
    if winner == 1:
        winner_screen = True
        while winner_screen:
            intro_text = Text(395, 62, "cadetblue1", "Player 'X' WON!", "cyan4", 48)
            screen.blit(intro_text.render_text(), [55, 150])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit()
                    
            pygame.display.update()
            # game framerate set to 60fps
            clock.tick(60)
    elif winner == -1:
        winner_screen = True
        while winner_screen:
            intro_text = Text(395, 62, "cadetblue1", "Player 'O' WON!", "cyan4", 48)
            screen.blit(intro_text.render_text(), [55, 150])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit()
                    
            pygame.display.update()
            # game framerate set to 60fps
            clock.tick(60)    

