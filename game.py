import pygame
import time
pygame.init()



X = 1168
Y = 655
BORDER_SIZE = 10
AVATAR_SIZE = 60
VEL = 190
AVATAR_X = (X - AVATAR_SIZE) / 2 # 4
AVATAR_Y = (Y - AVATAR_SIZE) / 2 # 6


direction = pygame.K_RIGHT

character_selection = input("Do you want to be Jack or Michael? ")

screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True

while running == True:
    
            
    screen.fill('black')

    # Creating a border
    house_border = pygame.draw.rect(screen, (152, 59, 16), pygame.Rect(0, 0, X, Y))
    house = pygame.draw.rect(screen, 'black', pygame.Rect(BORDER_SIZE, BORDER_SIZE, X - 2 * BORDER_SIZE, Y - BORDER_SIZE * 2))
    
    if character_selection == "Jack" or "jack":
        avatar_filepath = 'Jack.png' if direction != pygame.K_LEFT else 'Jack_Left.png'
    elif character_selection == "Michael" or "michael":
        avatar_filepath = 'Michael.png' if direction != pygame.K_RIGHT else 'Michael_Left.png'
    # Loading Jack.png(the character) and making it transparent.
    img = pygame.image.load(avatar_filepath).convert_alpha()
    
    # Scaling the character so that is fits according to my size in the frame.
    img = pygame.transform.scale(img, (AVATAR_SIZE, AVATAR_SIZE))
    
    # Finding the midpoint of the screen.
    midpoint = (AVATAR_X , AVATAR_Y)
    
    # Putting the character in the middle
    # and overlapping the two rectangles that we made earlier plus the character.
    screen.blit(img, midpoint)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and pygame.KEYDOWN:
            direction = event.key
            if event.key == pygame.K_LEFT:
                AVATAR_X -= VEL
                time.sleep(5)
            if event.key == pygame.K_RIGHT:
                AVATAR_X += VEL
            if event.key == pygame.K_UP:
                AVATAR_Y -= VEL
            if event.key == pygame.K_DOWN:
                AVATAR_Y += VEL
    
    AVATAR_X = min(X - AVATAR_SIZE, AVATAR_X)
    AVATAR_Y = min(Y - AVATAR_SIZE, AVATAR_Y)
    AVATAR_X = max(0, AVATAR_X)
    AVATAR_Y = max(0, AVATAR_Y)
    pygame.display.flip()
    
    
pygame.quit()


