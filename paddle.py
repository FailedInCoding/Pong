import pygame

#color
black = (0,0,0)

#this curent class derives as Sprite class in/from Pygame
class Paddle(pygame.sprite.Sprite):

    #def screen color
    def __init__(self, color, width, height):
        super().__init__()

        #background color 
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        #drawing a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #summoning the rectangle that has dimensions for the images
        self.rect = self.image.get_rect()

    #def moving down
    def moveUp(self, pixels):
        self.rect.y -= pixels
    #checks if it doesnt go of the screen
        if self.rect.y < 0:
            self.rect.y = 0
    
    #def moving up
    def moveDown(self, pixels):
        self.rect.y += pixels
    #checks if it doenst go of the screen
        if self.rect.y > 400:
            self.rect.y = 400
    