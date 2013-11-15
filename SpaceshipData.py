import pygame
import random
from spaceship import Spaceship, Spaceship2
from baddie import Baddie

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/3
        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,255,255))
        self.spaceship_speed = 10        
        self.spaceship2_width = 20
        self.spaceship2_height = 10
        self.spaceship2 = Spaceship2(self.spaceship2_width,self.spaceship2_height,0,(self.height / 2) - 10, (255,255,0))
        self.spaceship2_speed = 10
        self.bullets = []
        self.bullet_width = 10
        self.bullet_height = 5
        self.bullet_color = (255,255,255)
        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (255,0,0)
        self.kills = 0
        self.score_color = (255, 255, 255)
        self.score_x = 10
        self.score_y = 30
        self.money = 0
        self.gold_color = (255, 255, 255)
        self.gold_x = 10
        self.gold_y = 60
        self.lives = 30
        self.lives_color = (255, 255, 255)
        self.lives_x = 10
        self.lives_y = 90
        
        
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_LEFT in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_RIGHT in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_DOWN in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
        if pygame.K_a in keys:
            self.spaceship2.moveLeft(self.spaceship2_speed)
        if pygame.K_d in keys:
            self.spaceship2.moveRight(self.spaceship2_speed,self.upper_limit)
        if pygame.K_w in keys:
            self.spaceship2.moveUp(self.spaceship2_speed)
        if pygame.K_s in keys:
            self.spaceship2.moveDown(self.spaceship2_speed,self.height)
        if pygame.K_g in newkeys:
            self.bullets.append(self.spaceship2.fire(self.bullet_width,self.bullet_height,self.bullet_color)) 

        if random.randint(1, self.frame_rate/2) == 1:
            self.addBaddie()

        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
                
        for baddie in self.baddies:
            baddie.tick(0,0,self.height)

        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHitBaddie(x,y,w,h)
                if bullet.getHit():
                    bullet.setAlive(False)
                    baddie.setAlive(False)
                    bullet.hit = False
                    self.kills = self.kills + 1
                    self.money = self.money + 1


        live_bullets = []
        live_baddies = []
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
      
        self.bullets = live_bullets
        self.baddies = live_baddies
            
        return

    def addBaddie(self):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )
                   
        return

    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        score_str = "Dragons Killed: " + str(self.kills)
        self.drawTextLeft(surface, score_str, self.score_color, self.score_x, self.score_y, self.font2)
        gold_str = "Gold: " + str(self.money)
        self.drawTextLeft(surface, gold_str, self.gold_color, self.gold_x, self.gold_y, self.font2)
        gold_str = "Civillions: " + str(self.lives)
        self.drawTextLeft(surface, lives_str, self.lives_color, self.live_x, self.lives_y, self.font2)
        self.spaceship.draw(surface)
        self.spaceship2.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
           baddie.draw(surface)
        return

    
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
