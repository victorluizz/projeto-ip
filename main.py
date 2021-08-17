import pygame

pygame.init()

def main():
    display = pygame.display.set_mode((800,600))
    pygame.display.set_caption("PokeEdit")
    mapa = pygame.image.load("imagens/background.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        display.fill((0,0,0))
        display.blit(mapa, (0,0))
        pygame.display.update()
           
main()