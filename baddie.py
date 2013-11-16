import pygame
import random


class Baddie():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = 3
        self.color  = color
        self.alive  = True
        self.IMG = pygame.image.load("dragon.png")   
        return

    def tick(self,back_wall,upper_wall,lower_wall,far_wall):
        self.new_y = self.y + self.speed
        self.new_x = self.x + random.randint(-1,1)
        if self.new_y >lower_wall:
            self.setAlive(False)
        else:
            self.y = self.new_y
        if self.new_x < back_wall:
            self.new_x = back_wall
            self.life =-1
        elif self.new_x + self.width > far_wall:
            self.new_x = far_wall - self.height
        self.x = self.new_x
        return self.alive

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):     
        surface.blit(self.IMG, (self.x, self.y))
        return

class Baddie2():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = 5
        self.color  = color
        self.alive  = True
        self.IMG = pygame.image.load("hat_1.png")
        return

    def tick(self,back_wall,upper_wall,lower_wall,far_wall):
        self.new_y = self.y + self.speed
        self.new_x = self.x + random.randint(-1,1)
        if self.new_y >lower_wall:
            self.setAlive(False)
        else:
            self.y = self.new_y
        if self.new_x < back_wall:
            self.new_x = back_wall
        elif self.new_x + self.width > far_wall:
            self.new_x = far_wall - self.height
        self.x = self.new_x
        return self.alive

    def getAlive(self):
        return self.alive

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive
    
    def draw(self, surface):        
        surface.blit(self.IMG, (self.x, self.y))
        return
        

