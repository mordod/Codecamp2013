import pygame
import spaceship
import baddie
import random

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
        self.spaceship = spaceship.Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, ( 0, 0,255))
        self.spaceship_speed = 10
        self.spaceship2_width = 20
        self.spaceship2_height = 10
        self.spaceship2 = spaceship.Spaceship2(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, ( 0, 0,255))
        self.spaceship2_speed = 10        
        self.bullets = []
        self.bullet_width = 20
        self.bullet_height = 3
        self.bullet_color = (0,0,255)
        self.baddies = []
        self.baddie_width = 40
        self.baddie_height = 40
        self.baddie_color = (255,0,0)
        self.baddies2 = []
        self.baddie2_width = 40
        self.baddie2_height = 40
        self.baddie2_color = (255,0,0)  
        self.show_controls = True
        self.life = 25
        self.score = 0
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if self.show_controls :
            if pygame.K_SPACE in keys:
               self.show_controls = False
            return
        if pygame.K_LEFT in keys:
            self.spaceship.moveLeft(self.spaceship_speed)

        if pygame.K_RIGHT in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)

        if pygame.K_UP in keys:
            self.spaceship.moveUp(self.spaceship_speed)

        if pygame.K_DOWN in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        if pygame.K_KP0 in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))

        if pygame.K_a in keys:
             self.spaceship2.moveLeft(self.spaceship_speed)

        if pygame.K_d in keys:
            self.spaceship2.moveRight(self.spaceship_speed,self.upper_limit)

        if pygame.K_w in keys:
            self.spaceship2.moveUp(self.spaceship_speed)

        if pygame.K_s in keys:
            self.spaceship2.moveDown(self.spaceship_speed,self.height)


        if pygame.K_SPACE in newkeys:
            self.bullets.append(self.spaceship2.fire(self.bullet_width,self.bullet_height,self.bullet_color))        
   

        if random.randint(1, self.frame_rate/2) == 1:
            self.addBaddie()

        if random.randint(1, self.frame_rate/2) == 1:
            self.addBaddie2()

        if baddie self.alive = false
            self.score =+100


        live_bullets = []
        live_baddies = []

        if len(self.bullets) > 0 and len(self.baddies) > 0:
            bullet_id = 1
            for bullet in self.bullets:
                bullet.moveBullet()
                bullet.checkBackWall(self.width)
                for baddie in self.baddies:
                    x,y,w,h = baddie.getDimensions()
                    bullet.checkHitBaddie(x,y,w,h)
                    if bullet.getHit():
                        bullet.setAlive(False)
                        baddie.setAlive(False)
                        bullet.hit = False
                        self.score =+1
                    if bullet_id == 1:
                        if baddie.tick(0,0,self.height):
                            live_baddies.append(baddie)
                if bullet.alive:
                    live_bullets.append(bullet)
                bullet_id += 1
                    
        elif len(self.bullets) > 0 and len(self.baddies) < 1:
            for bullet in self.bullets:
                bullet.moveBullet()
                bullet.checkBackWall(self.width)
                if bullet.alive:
                    live_bullets.append(bullet)
                    
        elif len(self.bullets) < 1 and len(self.baddies) > 0:
            for baddie in self.baddies:
               if baddie.tick(0,0,self.height):
                    live_baddies.append(baddie)
        
        else:
            pass
      
        self.bullets = live_bullets
        self.baddies = live_baddies
            
        return

    def addBaddie(self):
        new_baddie = baddie.Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color )
        self.baddies.append( new_baddie )

    def addBaddie2(self):
        new_baddie = baddie.Baddie2( self.baddie2_width, self.baddie2_height, self.width, random.randint(0,(self.height-self.baddie2_height)), self.baddie2_color )
        self.baddies.append( new_baddie )
                   
        return

    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        if self.show_controls :
            image = pygame.image.load("controls.png")
            surface.blit(image,(0,0))
        else :
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
