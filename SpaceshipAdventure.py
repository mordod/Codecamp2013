import pygame
import game_mouse
from game_mouse import Game
from SpaceshipData import SpaceshipData

class SpaceshipAdventure(Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return
    
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4):
        self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position, a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4)
        return

    def paint(self, surface):
        self.data.draw(surface)
        return

    
    def newGame(self,width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        Game.__init__(self, "Spaceship Adventure", width, height, frame_rate)   
        self.data = SpaceshipData(width,height,frame_rate)
        
        return
