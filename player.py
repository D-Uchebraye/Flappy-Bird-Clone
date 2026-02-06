import pygame
class Player:
    def __init__(self,x_pos,y_pos,screen,gravity,):
        self.angle = 0
        self.velocity = 0
        self.gravity = gravity
        self.screen = screen
        self.bird_surface = pygame.image.load('flappybird.png').convert_alpha()
        original_width = self.bird_surface.get_width()
        orignal_height = self.bird_surface.get_height()
        self.bird_surface = pygame.transform.scale(self.bird_surface,(original_width//2,orignal_height//2))



        self.rect = self.bird_surface.get_rect(topleft=(x_pos,y_pos))
        self.hitbox = self.rect.inflate(-10,-10)


    def set_y_pos(self,y_pos):
        self.rect.y = y_pos
    


    def draw(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        self.hitbox = self.rect.inflate(-70,-70)
        pygame.draw.rect(self.screen,(255,255,255),self.hitbox)
        if self.velocity < 0 : #bouncing
            self.angle = min(self.angle +5 , +25)
        else:
            self.angle = max(self.angle - 5, -35)

        self.bird_surface_new = pygame.transform.rotate(self.bird_surface,self.angle)
        self.rect_new = self.bird_surface_new.get_rect(center=self.rect.center)

    



        self.screen.blit(self.bird_surface_new,self.rect_new)  

       # pygame.draw.rect(self.screen, (128, 0, 128), self.hitbox, 2)


        
        pass

    def bounce(self):
        self.velocity = -7
        pass
