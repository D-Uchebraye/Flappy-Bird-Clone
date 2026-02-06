# Example file showing a basic pygame "game loop"
import pygame
from player import Player
from pipes import Pipes
scored_pipes = []

#----settings----#
gravity = -5
screen_height = 720
screen_width = 1280
pipes_list = []
count = 0
state = "start"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pipes= Pipes()
top_surface = pygame.image.load('top_pipe.png').convert_alpha()
bottom_surface = pygame.image.load('bottom_pipe.png').convert_alpha()
border =  pygame.Rect(0,0,screen_width,screen_height)


 
text_rect = pygame.Rect(screen_width//2,0,110,140)
font= pygame.font.Font(None,50)


def draw_death_menu(count):
    text = font.render("Dead", True, (255, 255, 255))
    text2 = font.render('press P to continue' , True, (255,255,255))
   # screen.fill('light blue')
    screen.blit(text,(screen_width // 2 -75,screen_height // 2 +25))
    screen.blit(text2,(screen_width//2  -75, screen_height //2 +50))
    pygame.display.flip()
    
def reset_game():
    global pipes_list, scored_pipes, count, state, player, paused, running
    pipes_list = []
    scored_pipes = []
    count = 0
    paused = False
    running = True
    player.rect.y= screen_width // 3
    player.rect.y = screen_height // 2
    player.velocity = 0  # or whatever your Player class uses


def draw_pause_menu():
    screen.fill('light blue', border)
    text = font.render("Game Paused - Press P to Resume", True, (255, 255, 255))
    screen.blit(text,(400,360))
    pygame.display.flip()



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
life = True


player = Player(screen_width//3,screen_height//2,screen,0.5)
paused = True
dead = False



while running:
        



    for top,bottom in pipes_list:
        if top not in scored_pipes and top.right <= player.hitbox.left:
            count+= 1
            scored_pipes.append(top)


        if player.hitbox.colliderect(top) or player.hitbox.colliderect(bottom) or  not border.contains(player.hitbox):
            dead = True


        



    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = False
                dead = False
                reset_game()

            if event.key == pygame.K_SPACE:
                player.bounce()

    if dead:
        draw_death_menu(count)
        continue


    if paused:
        draw_pause_menu()
        continue

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    # RENDER YOUR GAME HERE
    player.draw()
    pipes.goon(1280,pipes_list)
    pipes.move_pipe(pipes_list)
    for top, bottom in pipes_list:
        screen.blit(pygame.transform.scale(top_surface, (top.width + 15, top.height)), top)
        screen.blit(pygame.transform.scale(bottom_surface, (bottom.width + 15, bottom.height )), bottom)
    
    text_surface = font.render(f'score:{count}',True,'black')
    screen.blit(text_surface,text_rect)
    
    





    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()