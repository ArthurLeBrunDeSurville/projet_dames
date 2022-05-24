import pygame
import os
WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salut")
WHITE = (255, 255, 255)
MARRON = (88, 41, 0)
PION_WIDTH, PION_HEIGHT = 40, 40
FPS = 60
Premier_case_blanche_WIDTH, Premier_case_blanche_HEIGHT= 100, 20

Coordonnees = [[[100,20],[260,20],[420,20],[580,20],[740,20]],
               [[20,100],[180,100],[340,100],[500,100],[660,100]],
               [[100,180],[260,180],[420,180],[580,180],[740,180]],
               [[20,260],[180,260],[340,260],[500,260],[660,260]],
               [[100,340],[260,340],[420,340],[580,340],[740,340]],
               [[200,420],[180,420],[340,420],[500,420],[660,420]],
               [[100,500],[260,500],[420,500],[580,500],[740,500]],
               [[20,580],[180,580],[340,580],[500,580],[660,580]],
               [[100,660],[260,660],[420,660],[580,660],[740,660]],
               [[20,740],[180,740],[340,740],[500,740],[660,740]]]

Coordonnees_x = [20,100,180, 260,340, 420,500, 580,660, 740]
                 
Coordonnees_y = [20,100,180, 260,340, 420,500, 580,660, 740]
                 
               

CHECKERS_BACKGROUND = pygame.image.load('Captur.PNG')
PION_ROUGE_IMAGE = pygame.image.load('Pion_rouge.PNG')
PION_MARRON_IMAGE = pygame.image.load('Pion_marron.PNG')
PION_ROUGE = pygame.transform.scale(PION_ROUGE_IMAGE,(PION_WIDTH, PION_HEIGHT))

def draw_window():
    WIN.fill(MARRON)
    WIN.blit(CHECKERS_BACKGROUND,(0,0))
    WIN.blit(PION_ROUGE,(Coordonnees_x[1], Coordonnees_y[1]))
    WIN.blit(PION_ROUGE,(Coordonnees_x[2],Coordonnees_y[2]))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()
    
if __name__ == "__main__":
    main()
