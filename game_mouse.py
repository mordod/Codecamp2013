import pygame
import pygame.locals

class Game:
    def __init__(self, name, width, height, frames_per_second):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True

        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption(name)
        pygame.joystick.init()
        self.count = pygame.joystick.get_count()
        if self.count == 1:
            self.j1 = pygame.joystick.Joystick(0)
            self.j1.init()
        if self.count == 2:
            self.j1 = pygame.joystick.Joystick(0)
            self.j1.init()
            self.j2 = pygame.joystick.Joystick(1)
            self.j2.init()
        if self.count == 3:
            self.j1 = pygame.joystick.Joystick(0)
            self.j1.init()
            self.j2 = pygame.joystick.Joystick(1)
            self.j2.init()
            self.j3 = pygame.joystick.Joystick(2)
            self.j3.init()
        if self.count == 4:
            self.j1 = pygame.joystick.Joystick(0)
            self.j1.init()
            self.j2 = pygame.joystick.Joystick(1)
            self.j2.init()
            self.j3 = pygame.joystick.Joystick(2)
            self.j3.init()
            self.j4 = pygame.joystick.Joystick(3)
            self.j4.init()
        return self.count
    def joystick(self, a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4):
        a_clicked = False
        left = False
        right = False
        up = False
        down = False
        start_clicked = False
        
        a_clicked2 = False
        left2 = False
        right2 = False
        up2 = False
        down2 = False
        start_clicked2 = False
        
        a_clicked3 = False
        left3 = False
        right3 = False
        up3 = False
        down3 = False
        start_clicked3 = False
        
        a_clicked4 = False
        left4 = False
        right4 = False
        up4 = False
        down4 = False
        start_clicked4 = False
        
        A_BUTTON = 0
        B_BUTTON = 1
        Y_AXIS = 1
        X_AXIS = 0
        START = 9
        if self.count == 1:
            j = self.j1        
            if j.get_button(A_BUTTON) != 0:
                a_clicked = True
            if j.get_button(START) != 0:
                start_clicked = True
                pygame.quit()
            if j.get_axis(X_AXIS) != 0:
 #               (x,y) = axis_position
                axis = round(j.get_axis(X_AXIS)*10)
                if axis < 0:
                    left = True
                if axis > 0:
                    right = True
#                axis_position = (int(x), int(y))
            if j.get_axis(Y_AXIS) != 0:
#                (x,y) = axis_position
                axis = round(j.get_axis(Y_AXIS)*10)
                if axis > 0:
                    down = True
                if axis < 0:
                    up = True            
#                axis_position = (int(x), int(y))


        if self.count == 2:
            j = self.j1        
            if j.get_button(A_BUTTON) != 0:
                a_clicked = True
            if j.get_button(START) != 0:
                start_clicked = True
                pygame.quit()
            if j.get_axis(X_AXIS) != 0:
                axis = round(j.get_axis(X_AXIS)*10)
                if axis < 0:
                    left = True
                if axis > 0:
                    right = True
            if j.get_axis(Y_AXIS) != 0:
                axis = round(j.get_axis(Y_AXIS)*10)
                if axis > 0:
                    down = True
                if axis < 0:
                    up = True            
            j2 = self.j2        
            if j2.get_button(A_BUTTON) != 0:
                a_clicked2 = True
            if j2.get_button(START) != 0:
                start_clicked2 = True
                pygame.quit()
            if j2.get_axis(X_AXIS) != 0:
                axis2 = round(j.get_axis(X_AXIS)*10)
                if axis2 < 0:
                    left2 = True
                if axis2 > 0:
                    right2 = True
            if j2.get_axis(Y_AXIS) != 0:
                axis2 = round(j.get_axis(Y_AXIS)*10)
                if axis2 > 0:
                    down2 = True
                if axis2 < 0:
                    up2 = True

        if self.count == 3:
            j = self.j1        
            if j.get_button(A_BUTTON) != 0:
                a_clicked = True
            if j.get_button(START) != 0:
                start_clicked = True
                pygame.quit()
            if j.get_axis(X_AXIS) != 0:
                axis = round(j.get_axis(X_AXIS)*10)
                if axis < 0:
                    left = True
                if axis > 0:
                    right = True
            if j.get_axis(Y_AXIS) != 0:
                axis = round(j.get_axis(Y_AXIS)*10)
                if axis > 0:
                    down = True
                if axis < 0:
                    up = True            
            j2 = self.j2        
            if j2.get_button(A_BUTTON) != 0:
                a_clicked2 = True
            if j2.get_button(START) != 0:
                start_clicked2 = True
                pygame.quit()
            if j2.get_axis(X_AXIS) != 0:
                axis2 = round(j2.get_axis(X_AXIS)*10)
                if axis2 < 0:
                    left2 = True
                if axis2 > 0:
                    right2 = True
            if j2.get_axis(Y_AXIS) != 0:
                axis2 = round(j2.get_axis(Y_AXIS)*10)
                if axis2 > 0:
                    down2 = True
                if axis2 < 0:
                    up2 = True 
            j3 = self.j3        
            if j3.get_button(A_BUTTON) != 0:
                a_clicked3 = True
            if j3.get_button(START) != 0:
                start_clicked3 = True
                pygame.quit()
            if j3.get_axis(X_AXIS) != 0:
                axis3 = round(j3.get_axis(X_AXIS)*10)
                if axis3 < 0:
                    left3 = True
                if axis3 > 0:
                    right3 = True
            if j3.get_axis(Y_AXIS) != 0:
                axis3 = round(j3.get_axis(Y_AXIS)*10)
                if axis3 > 0:
                    down3 = True
                if axis3 < 0:
                    up3 = True

        if self.count == 4:
            j = self.j1        
            if j.get_button(A_BUTTON) != 0:
                a_clicked = True
            if j.get_button(START) != 0:
                start_clicked = True
                pygame.quit()
            if j.get_axis(X_AXIS) != 0:
                axis = round(j.get_axis(X_AXIS)*10)
                if axis < 0:
                    left = True
                if axis > 0:
                    right = True
            if j.get_axis(Y_AXIS) != 0:
                axis = round(j.get_axis(Y_AXIS)*10)
                if axis > 0:
                    down = True
                if axis < 0:
                    up = True            
            j2 = self.j2        
            if j2.get_button(A_BUTTON) != 0:
                a_clicked2 = True
            if j2.get_button(START) != 0:
                start_clicked2 = True
                pygame.quit()
            if j2.get_axis(X_AXIS) != 0:
                axis2 = round(j2.get_axis(X_AXIS)*10)
                if axis2 < 0:
                    left2 = True
                if axis2 > 0:
                    right2 = True
            if j2.get_axis(Y_AXIS) != 0:
                axis2 = round(j2.get_axis(Y_AXIS)*10)
                if axis2 > 0:
                    down2 = True
                if axis2 < 0:
                    up2 = True 
            j3 = self.j3        
            if j3.get_button(A_BUTTON) != 0:
                a_clicked3 = True
            if j3.get_button(START) != 0:
                start_clicked3 = True
                pygame.quit()
            if j3.get_axis(X_AXIS) != 0:
                axis3 = round(j3.get_axis(X_AXIS)*10)
                if axis3 < 0:
                    left3 = True
                if axis3 > 0:
                    right3 = True
            if j3.get_axis(Y_AXIS) != 0:
                axis3 = round(j3.get_axis(Y_AXIS)*10)
                if axis3 > 0:
                    down3 = True
                if axis3 < 0:
                    up3 = True
            j4 = self.j4        
            if j4.get_button(A_BUTTON) != 0:
                a_clicked4 = True
            if j4.get_button(START) != 0:
                start_clicked4 = True
                pygame.quit()
            if j4.get_axis(X_AXIS) != 0:
                axis4 = round(j4.get_axis(X_AXIS)*10)
                if axis4 < 0:
                    left4 = True
                if axis4 > 0:
                    right4 = True
            if j4.get_axis(Y_AXIS) != 0:
                axis4 = round(j4.get_axis(Y_AXIS)*10)
                if axis4 > 0:
                    down4 = True
                if axis4 < 0:
                    up4 = True 
        return a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4
        
        

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError()

    def paint(self, surface):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        buttons = set()
        mouse_position = (1,1)
        a_clicked = False
        left = False
        right = False
        up = False
        down = False
        start_clicked = False
        a_clicked2 = False
        left2 = False
        right2 = False
        up2 = False
        down2 = False
        start_clicked2 = False
        
        a_clicked3 = False
        left3 = False
        right3 = False
        up3 = False
        down3 = False
        start_clicked3 = False
        
        a_clicked4 = False
        left4 = False
        right4 = False
        up4 = False
        down4 = False
        start_clicked4 = False
        axis_position = (1,400)

        while True:
            clock.tick(self.frames_per_second)

            newkeys = set()
            newbuttons = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which mouse buttons are currently pressed
                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add(e.button)
                    newbuttons.add(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos
                
                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)
            a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4 = self.joystick(a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4)

            if self.on:
                self.game_logic(keys, newkeys, buttons, newbuttons, mouse_position, a_clicked, axis_position, left, right, down, up, a_clicked2, left2, right2, down2, up2, a_clicked3, left3, right3, down3, up3, a_clicked4, left4, right4, down4, up4)
                self.paint(self.screen)

            pygame.display.flip()

