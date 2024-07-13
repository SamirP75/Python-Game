import pygame
import constants
import time

pygame.init()

# Global variables - do change
direction = pygame.K_RIGHT
key_pressed = False
screen = pygame.display.set_mode((constants.X, constants.Y))
clock = pygame.time.Clock()
running = True
avatar_x = (constants.X - constants.AVATAR_SIZE) / 2 # 4
avatar_y = (constants.Y - constants.AVATAR_SIZE) / 2 # 6
# This is where the terminal asks what character you want to be
character_selection = input("Do you want to be Jack, Michael, Emily, or Sarah? ")

selected_character = constants.Character(character_selection)

# This is where I name the window (you can see this at the very top of the window)
pygame.display.set_caption("Adventures of " + character_selection)    

# Jack.png, Michael.png, Emily.png, and Sarah.png
avatar = pygame.image.load(selected_character.avatar_filepath).convert_alpha()
avatar = pygame.transform.scale(avatar, (constants.AVATAR_SIZE, constants.AVATAR_SIZE))

# Jack_Left.png, Michael_Left.png, Emily_Left.png, and Sarah_Left.png
avatar_left = pygame.image.load(selected_character.avatar_filepath_left).convert_alpha()
avatar_left = pygame.transform.scale(avatar_left, (constants.AVATAR_SIZE, constants.AVATAR_SIZE))


while running == True:
    
    # Making the starting window black.        
    screen.fill('black')

    # Creating a border
    house_border = pygame.draw.rect(screen, (152, 59, 16), pygame.Rect(0, 0, constants.X, constants.Y))
    house = pygame.draw.rect(screen, 'black', pygame.Rect(constants.BORDER_SIZE, constants.BORDER_SIZE, constants.X - 2 * constants.BORDER_SIZE, constants.Y - constants.BORDER_SIZE * 2))
    #portal = pygame.draw.rect(screen, 'aquamarine2', (1100, 530, 50, 50))
    background = pygame.image.load(constants.HOUSE_FILEPATH)
    background = pygame.transform.scale(background, (490, 533))
    
    # Finding the midpoint of the screen.
    midpoint = (avatar_x , avatar_y)
    
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
            avatar_x -= constants.VEL
            
        if event.key == pygame.K_RIGHT:
            avatar_x += constants.VEL
            
        if event.key == pygame.K_UP:
            avatar_y -= constants.VEL
            
        if event.key == pygame.K_DOWN:
            avatar_y += constants.VEL
    # This is where we set borders.   
    '''Y - AVATAR_SIZE'''                  
    avatar_x = min(constants.X - constants.AVATAR_SIZE, avatar_x)
    avatar_y = min(392, avatar_y)
    avatar_x = max(0, avatar_x)
    avatar_y = max(100, avatar_y)
    pygame.display.flip()
    
    clock.tick(120)
    
    
pygame.quit()


