import pygame
import random
import game_mouse
from spaceship import Spaceship, Spaceship2, Spaceship3, Spaceship4
from baddie import Baddie,Baddie2,Baddie3 

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/1
        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 50, (255,255,255))
        self.spaceship_speed = 10        
        self.spaceship2_width = 20
        self.spaceship2_height = 10
        self.spaceship2 = Spaceship2(self.spaceship2_width,self.spaceship2_height,0,(self.height / 2) - 10, (255,255,0))
        self.spaceship2_speed = 10
        self.spaceship3_width = 20
        self.spaceship3_height = 10
        self.spaceship3 = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,255,255))
        self.spaceship3_speed = 10        
        self.spaceship4_width = 20
        self.spaceship4_height = 10
        self.spaceship4 = Spaceship4(self.spaceship4_width,self.spaceship4_height,0,(self.height / 2) - 10, (255,255,0))
        self.spaceship4_speed = 10
        self.bullets = []
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.baddies = []
        self.baddie_width = 121
        self.baddie_height = 95
        self.baddie_color = (255,0,0)
        self.baddie2_width = 121
        self.baddie2_height = 95
        self.baddie2_color = (255,0,0)
        self.baddie3_width = 121
        self.baddie3_height = 95
        self.baddie3_color = (255,0,0)
        self.kills = 0
        self.score_color = (255, 255, 255)
        self.score_x = 10
        self.score_y = 30
        self.money = 0
        self.gold_color = (255, 255, 255)
        self.gold_x = 10
        self.gold_y = 60
        self.Img = pygame.image.load("background.png")
        self.lives = 30
        self.lives_color = (255, 255, 255)
        self.lives_x = 10
        self.lives_y = 90
        self.a_counter = 0

        
        
        return


    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position, a_clicked, axis_position, left, right, down, up):
        if self.lives <= 0:
            return
        self.a_counter += 1
        if left:
            self.spaceship.moveLeft(self.spaceship_speed)
        if right:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if up:
            self.spaceship.moveUp(self.spaceship_speed)
        if down:
            self.spaceship.moveDown(self.spaceship_speed,self.height)
        if a_clicked:
            if self.a_counter > 10:
                self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
                self.a_counter = 0
           

        if pygame.K_LEFT in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_RIGHT in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_DOWN in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        if pygame.K_l in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
        if pygame.K_a in keys:
            self.spaceship2.moveLeft(self.spaceship2_speed)
        if pygame.K_d in keys:
            self.spaceship2.moveRight(self.spaceship2_speed,self.upper_limit)
        if pygame.K_w in keys:
            self.spaceship2.moveUp(self.spaceship2_speed)
        if pygame.K_s in keys:
            self.spaceship2.moveDown(self.spaceship2_speed,self.height)
        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship2.fire(self.bullet_width,self.bullet_height,self.bullet_color))

        if pygame.K_a in keys:
            self.spaceship3.moveLeft(self.spaceship3_speed)
        if pygame.K_d in keys:
            self.spaceship3.moveRight(self.spaceship3_speed,self.upper_limit)
        if pygame.K_w in keys:
            self.spaceship3.moveUp(self.spaceship3_speed)
        if pygame.K_s in keys:
            self.spaceship3.moveDown(self.spaceship3_speed,self.height)
        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship3.fire(self.bullet_width,self.bullet_height,self.bullet_color))

        if pygame.K_a in keys:
            self.spaceship4.moveLeft(self.spaceship4_speed)
        if pygame.K_d in keys:
            self.spaceship4.moveRight(self.spaceship4_speed,self.upper_limit)
        if pygame.K_w in keys:
            self.spaceship4.moveUp(self.spaceship4_speed)
        if pygame.K_s in keys:
            self.spaceship4.moveDown(self.spaceship4_speed,self.height)
        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship4.fire(self.bullet_width,self.bullet_height,self.bullet_color))     


        if self.kills < 150:
            if random.randint(1, self.frame_rate/9) == 1:
                self.addBaddie()
        if self.kills > 75:
            if random.randint(1, self.frame_rate/2) == 1:
                self.addBaddie2()
                
        if self.kills > 10:
            if random.randint(1, self.frame_rate/3) == 1:
                self.addBaddie()
                
        if random.randint(1, self.frame_rate/2) == 1:
            self.addBaddie3()

        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)
                
        for baddie in self.baddies:
            if not baddie.tick(0,0,self.height,self.width):
                self.lives -= 1
        

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
                    self.money = self.money + 7


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
        new_baddie = Baddie( self.baddie_width, self.baddie_height, random.randint (1,self.width - self.baddie_width) , 0,   self.baddie_color )             
        self.baddies.append( new_baddie )

    def addBaddie2(self):
        new_baddie2 = Baddie2( self.baddie2_width, self.baddie2_height, random.randint (1,self.width - self.baddie2_width) , 0,   self.baddie2_color )             
        self.baddies.append( new_baddie2 )

    def addBaddie3(self):
        new_baddie3 = Baddie3( self.baddie3_width, self.baddie3_height, random.randint (1,self.width - self.baddie3_width) , 0,   self.baddie3_color )             
        self.baddies.append( new_baddie3 )
                   
        return

    def draw(self,surface):
        surface.blit(self.Img, (0, 0))
        score_str = "Dragons Killed: " + str(self.kills)
        self.drawTextLeft(surface, score_str, self.score_color, self.score_x, self.score_y, self.font2)
        gold_str = "Gold: " + str(self.money)
        self.drawTextLeft(surface, gold_str, self.gold_color, self.gold_x, self.gold_y, self.font2)
        lives_str = "lives: " + str(self.lives)
        self.drawTextLeft(surface, lives_str, self.lives_color, self.lives_x, self.lives_y, self.font2)
        self.spaceship.draw(surface)
        self.spaceship2.draw(surface)
        for bullet in self.bullets:
            bullet.draw(surface)
        for baddie in self.baddies:
           baddie.draw(surface)
        for baddie2 in self.baddies:
           baddie2.draw(surface)
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
