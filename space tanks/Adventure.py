

import pygame
import game_mouse
import AdventureData

class SpaceshipAdventure(game_mouse.Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return
    
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        
        self.data.draw(surface)
        return

    
    def newGame(self,width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        game_mouse.Game.__init__(self, "Spaceship Adventures", width, height, frame_rate)   
        self.data = AdventureData.SpaceshipData(width,height,frame_rate)
        self.life = 25
        
        return

def main():
    pygame.font.init()
    c = SpaceshipAdventure(1000, 600, 60)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

