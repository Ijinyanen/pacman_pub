import pygame
import random

pygame.init()

#constants
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (229,18,161)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
LIGHT_BLUE = (155,155,255)

#Pacman variables
pac_x_y = [30,30]
pac_width=6
pac_height=20
vel=1
direction = [0,0]
pac_colour = YELLOW

#ghosts
ghost_width=6
ghost_vel=1

red_x_y = [210,170]
red_direction = [0,0]
red_ghost_colour = RED

green_x_y = [210,170]
green_direction = [0,0]
green_ghost_colour = GREEN

blue_x_y = [210,170]
blue_direction = [0,0]
blue_ghost_colour = LIGHT_BLUE


#set screen
screen_width=420
screen_height=420
surface = pygame.display.set_mode((screen_width, screen_height))
surface.fill(BLACK)
game_on = 1

#main
def start_game():
    global game_on 
    global pac_x_y
    global direction
    global red_x_y
    global red_direction
    global green_x_y
    global green_direction
    global blue_x_y
    global blue_direction
    global ghost_start
    
    #game loop
    while game_on:
        pygame.time.delay(15)
        surface.fill(BLACK)
        
        for wall in game_walls_array:
            draw_wall(wall[0],wall[1],wall[2],wall[3])

        #checking event list to see if keys pressed
        for event in pygame.event.get():
            #code for exit
            if event.type == pygame.QUIT:
                game_on = 0

            #code to see if keys were pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = [-1,0]
                if event.key == pygame.K_RIGHT:
                    direction = [1,0]
                if event.key == pygame.K_UP:
                    direction = [0,-1]
                if event.key == pygame.K_DOWN:
                    direction = [0,1]

        #update character
        pac_x_y[0] += direction[0]
        pac_x_y[1] += direction[1]

        #update ghost move
        red_direction = ghost_move(red_direction)
        blue_direction = ghost_move(blue_direction)
        green_direction = ghost_move(green_direction)
        
        red_x_y[0] += red_direction[0]
        red_x_y[1] += red_direction[1]
        print(red_direction[0],red_direction[1])
        print(red_x_y[0], red_x_y[1])

        green_x_y[0] += green_direction[0]
        green_x_y[1] += green_direction[1]

        blue_x_y[0] += blue_direction[0]
        blue_x_y[1] += blue_direction[1]

        #draw_pacman
        pygame.draw.circle(surface,pac_colour, (pac_x_y[0],pac_x_y[1]),pac_width)
        #draw_ghosts
        pygame.draw.circle(surface,red_ghost_colour,(red_x_y[0],red_x_y[1]),ghost_width)
        pygame.draw.circle(surface,green_ghost_colour,(green_x_y[0],green_x_y[1]),ghost_width)
        pygame.draw.circle(surface,blue_ghost_colour,(blue_x_y[0],blue_x_y[1]),ghost_width)
        
        ghost_cought_pac_detec()
        ghost_start=1
        pygame.display.update()


#game geometery
game_walls_array = [
    [0,0,400,20],
    [0,0,20,400],
    [400,0,20,400],
    [0,400,420,20],
    [40,40,60,40],
    [80,80,20,20],
    [0,100,60,20],
    [80,120,20,20],
    [40,140,60,40],
    [40,200,60,20],
    [80,220,20,40],
    [20,240,40,20],
    [40,280,60,20],
    [80,300,20,40],
    [20,320,40,20],
    [40,360,140,20],
    [120,320,20,40],
    [120,40,20,140],
    [120,100,60,20],
    [120,200,20,60],
    [120,280,60,20],
    [160,40,20,40],
    [160,60,100,20],
    [240,40,20,20],
    [200,20,20,20],
    [200,80,20,40],
    [160,140,40,20],
    [160,160,20,60],
    [160,200,100,20],
    [220,140,40,20],
    [240,160,20,60],
    [160,240,100,20],
    [200,260,20,40],
    [160,320,100,20],
    [200,340,20,40],
    [280,40,20,140],
    [240,100,40,20],
    [280,200,20,60],
    [240,280,60,20],
    [280,320,20,40],
    [240,360,140,20],
    [320,40,60,40],
    [320,80,20,20],
    [360,100,40,20],
    [320,120,20,20],
    [320,140,60,40],
    [320,200,60,20],
    [320,220,20,40],
    [360,240,40,20],
    [320,280,60,20],
    [320,300,20,40],
    [360,320,40,20],
    [180,160,20,40],
    [220,160,20,40]
 ]

#FUNCTIONS
#function to draw wall , and call col_dec function
def draw_wall(x_coor, y_coor, wall_width, wall_depth):
    pygame.draw.rect(surface, BLUE, pygame.Rect(x_coor,y_coor,wall_width,wall_depth),)
    col_dec(x_coor,y_coor, wall_width,wall_depth)

#function that adds collision detection
def col_dec(x_coor, y_coor, wall_width, wall_depth):
    #collision dection for pacman
    x_adjust = x_coor - pac_width
    y_adjust = y_coor - pac_width
    width_adjust = wall_width + pac_width + x_coor
    depth_adjust = wall_depth + pac_width + y_coor
    global pac_x_y
    global direction

    if pac_x_y[0] >= x_adjust and pac_x_y[0] <= width_adjust and pac_x_y[1] >= y_adjust and pac_x_y[1] <= depth_adjust:
        print("reached")
        direction = [0,0]
        if pac_x_y[0] == x_adjust:
            pac_x_y[0] = x_adjust - 1
            print("x is:", pac_x_y[0])
        if pac_x_y[0] == width_adjust: 
            pac_x_y[0] = width_adjust + 1
            print("x is:", pac_x_y[0])
        if pac_x_y[1] == y_adjust:
            pac_x_y[1] = y_adjust - 1
            print("y is:", pac_x_y[1])
        if pac_x_y[1] == depth_adjust:
            pac_x_y[1] = depth_adjust + 1
            print("y is:", pac_x_y[1])

    #collision detection for the ghosts
    global red_x_y
    global red_direction
    global green_x_y
    global green_direction
    global blue_x_y
    global blue_direction
    x_adjust = x_coor - ghost_width
    y_adjust = y_coor - ghost_width
    width_adjust = wall_width + ghost_width + x_coor
    depth_adjust = wall_depth + ghost_width + y_coor

    if red_x_y[0] >= x_adjust and red_x_y[0] <= width_adjust and red_x_y[1] >= y_adjust and red_x_y[1] <= depth_adjust:
        red_direction = [0,0]
        if red_x_y[0] == x_adjust:
            red_x_y[0] = x_adjust - 1
            print("red x is:", red_x_y[0])
        if red_x_y[0] == width_adjust: 
            red_x_y[0] = width_adjust + 1
            print("red x is:", red_x_y[0])
        if red_x_y[1] == y_adjust:
            red_x_y[1] = y_adjust - 1
            print("red y is:", red_x_y[1])
        if red_x_y[1] == depth_adjust:
            red_x_y[1] = depth_adjust + 1
            print("red y is:", red_x_y[1])

    if blue_x_y[0] >= x_adjust and blue_x_y[0] <= width_adjust and blue_x_y[1] >= y_adjust and blue_x_y[1] <= depth_adjust:
        blue_direction = [0,0]
        if blue_x_y[0] == x_adjust:
            blue_x_y[0] = x_adjust - 1
            print("red x is:", blue_x_y[0])
        if blue_x_y[0] == width_adjust: 
            blue_x_y[0] = width_adjust + 1
            print("red x is:", blue_x_y[0])
        if blue_x_y[1] == y_adjust:
            blue_x_y[1] = y_adjust - 1
            print("red y is:", blue_x_y[1])
        if blue_x_y[1] == depth_adjust:
            blue_x_y[1] = depth_adjust + 1
            print("red y is:", blue_x_y[1])

    if green_x_y[0] >= x_adjust and green_x_y[0] <= width_adjust and green_x_y[1] >= y_adjust and green_x_y[1] <= depth_adjust:
        green_direction = [0,0]
        if green_x_y[0] == x_adjust:
            green_x_y[0] = x_adjust - 1
            print("red x is:", green_x_y[0])
        if green_x_y[0] == width_adjust: 
            green_x_y[0] = width_adjust + 1
            print("red x is:", green_x_y[0])
        if green_x_y[1] == y_adjust:
            green_x_y[1] = y_adjust - 1
            print("red y is:", green_x_y[1])
        if green_x_y[1] == depth_adjust:
            green_x_y[1] = depth_adjust + 1
            print("red y is:", green_x_y[1])


#Ghost move function
def ghost_move (ghost_direction):

    if ghost_direction[0] == 0 and ghost_direction[1] == 0: 
        number = 0
        number = random.randint(1,4)
        print(number)
        if number == 1:
            ghost_direction = [0,-1]
        elif number == 2:
            ghost_direction = [0,1]    
        elif number == 3:
            ghost_direction = [1,0]
        elif number == 4:
            ghost_direction = [-1,0]
        else:
            print("error in assigning direction")
        print("ghost direction in function:", ghost_direction)

    return(ghost_direction)

def ghost_cought_pac_detec():
    global game_on
    if (pac_x_y[0] % red_x_y[0] <=10 and pac_x_y[1] % red_x_y[1] <= 10)or(pac_x_y[0] % blue_x_y[0] <=10 and pac_x_y[1] % blue_x_y[1] <= 10)or(pac_x_y[0] % blue_x_y[0] <=10 and pac_x_y[1] % blue_x_y[1] <= 10):
        surface.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        img = font.render("Game Over", True, RED)
        surface.blit(img, (200,200))
        game_on = 0

start_game()