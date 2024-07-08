import pygame
import time
pygame.init()



X = 510
Y = 552
BORDER_SIZE = 10
AVATAR_SIZE = 80
VEL = 4
AVATAR_X = (X - AVATAR_SIZE) / 2 # 4
AVATAR_Y = (Y - AVATAR_SIZE) / 2 # 6


direction = pygame.K_RIGHT
key_pressed = False

screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True

# This is where the terminal asks what character you want to be
character_selection = input("Do you want to be Jack, Michael, Emily, or Sarah? ")

# This is where you select your character and where it displays it based off of what you picked.
if character_selection == 'Jack' or character_selection == 'jack':
    avatar_filepath = 'Jack.png'
    avatar_filepath_left = 'Jack_Left.png'
elif character_selection == 'Michael' or character_selection == 'michael':
    avatar_filepath = 'Michael.png'
    avatar_filepath_left = 'Michael_Left.png'
elif character_selection == 'Emily' or character_selection == 'emily':
    avatar_filepath = 'Emily.png'
    avatar_filepath_left = 'Emily_Left.png'   
elif character_selection == 'Sarah' or character_selection == 'sarah':
    avatar_filepath = 'Sarah.png'
    avatar_filepath_left = 'Sarah_Left.png'

# This is where I name the window (you can see this at the very top of the window)
pygame.display.set_caption("Adventures of " + character_selection)    

# Jack.png, Michael.png, Emily.png, and Sarah.png
avatar = pygame.image.load(avatar_filepath).convert_alpha()
avatar = pygame.transform.scale(avatar, (AVATAR_SIZE, AVATAR_SIZE))

# Jack_Left.png, Michael_Left.png, Emily_Left.png, and Sarah_Left.png
avatar_left = pygame.image.load(avatar_filepath_left).convert_alpha()
avatar_left = pygame.transform.scale(avatar_left, (AVATAR_SIZE, AVATAR_SIZE))


while running == True:
    
    # Making the starting window black.        
    screen.fill('black')

    # Creating a border
    house_border = pygame.draw.rect(screen, (152, 59, 16), pygame.Rect(0, 0, X, Y))
    house = pygame.draw.rect(screen, 'black', pygame.Rect(BORDER_SIZE, BORDER_SIZE, X - 2 * BORDER_SIZE, Y - BORDER_SIZE * 2))
    #portal = pygame.draw.rect(screen, 'aquamarine2', (1100, 530, 50, 50))
    background = pygame.image.load('House_background.png')
    background = pygame.transform.scale(background, (490, 533))
    
    # Finding the midpoint of the screen.
    midpoint = (AVATAR_X , AVATAR_Y)
    
    # Putting the character in the middle
    # and overlapping the two rectangles that we made earlier plus the character.
    screen.blit(background, (10,10))
    screen.blit(avatar_left if direction == pygame.K_LEFT else avatar, midpoint)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            direction = event.key
            key_pressed = True
        if event.type == pygame.KEYUP:
            key_pressed = False
    # This part is where it determines what the character does when you press any of the arrow keys.    
    if key_pressed == True:
        if event.key == pygame.K_LEFT:
            AVATAR_X -= VEL
            
        if event.key == pygame.K_RIGHT:
            AVATAR_X += VEL
            
        if event.key == pygame.K_UP:
            AVATAR_Y -= VEL
            
        if event.key == pygame.K_DOWN:
            AVATAR_Y += VEL
    # This is where we set borders.                    
    AVATAR_X = min(X - AVATAR_SIZE, AVATAR_X)
    AVATAR_Y = min(Y - AVATAR_SIZE, AVATAR_Y)
    AVATAR_X = max(0, AVATAR_X)
    AVATAR_Y = max(0, AVATAR_Y)
    pygame.display.flip()
    
    clock.tick(120)
    
    
pygame.quit()


