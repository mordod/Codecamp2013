import pygame
import bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.image = self.spaceship = pygame.image.load("tank.png")
        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color):
        return bullet.Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def draw(self, surface):
        img = self.spaceship = pygame.image.load("tank.png")
        surface.blit(img, (self.x, self.y))
        return

        import pygame
import bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color):
        return bullet.Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def draw(self, surface):
        self.image = self.spaceship = pygame.image.load("tank.png")
        surface.blit(self.image, (self.x, self.y))
        return
        
import pygame
import bullet

class Spaceship2():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color):
        return bullet.Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def draw(self, surface):
        self.image = pygame.image.load("space.png")
        surface.blit(self.image, (self.x, self.y))
        return
    


