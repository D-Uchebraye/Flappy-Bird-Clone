<<<<<<< HEAD
import random
import pygame
class Pipes:
    def __init__(self):
        self.scored = False

    def goon(self,x_pos:int,pipes:list):
        #--when to generate pipes--
        PIPE_SPACING = 700

        if len(pipes) == 0:
            self.generate_pipe(x_pos,pipes)

        else:
            last_top, _=pipes[-1]
            if last_top.x <= 720 - PIPE_SPACING:
                self.generate_pipe(x_pos,pipes)        




    def generate_pipe(self,x_pos:int,pipes:list):
        #--rules for pipe generation--
        gap_y = random.randint(100,325)
        PIPE_WIDTH = 128
        gap_height = 150
        top_pipe = pygame.Rect(x_pos,0,PIPE_WIDTH,gap_y)
        bottom_pipe = pygame.Rect(x_pos,gap_y+gap_height,PIPE_WIDTH,720-(gap_height+gap_y))    

        pipes.append((top_pipe,bottom_pipe))

    def move_pipe(self,pipes):
        SPEED = 5
        for top,bottom in pipes:
            top.x -= SPEED
            bottom.x -= SPEED
        









=======
import random
import pygame
class Pipes:
    def __init__(self):
        self.scored = False

    def goon(self,x_pos:int,pipes:list):
        #--when to generate pipes--
        PIPE_SPACING = 700

        if len(pipes) == 0:
            self.generate_pipe(x_pos,pipes)

        else:
            last_top, _=pipes[-1]
            if last_top.x <= 720 - PIPE_SPACING:
                self.generate_pipe(x_pos,pipes)        




    def generate_pipe(self,x_pos:int,pipes:list):
        #--rules for pipe generation--
        gap_y = random.randint(100,325)
        PIPE_WIDTH = 128
        gap_height = 150
        top_pipe = pygame.Rect(x_pos,0,PIPE_WIDTH,gap_y)
        bottom_pipe = pygame.Rect(x_pos,gap_y+gap_height,PIPE_WIDTH,720-(gap_height+gap_y))    

        pipes.append((top_pipe,bottom_pipe))

    def move_pipe(self,pipes):
        SPEED = 5
        for top,bottom in pipes:
            top.x -= SPEED
            bottom.x -= SPEED
        









>>>>>>> 535e8fd (added ground texture)
