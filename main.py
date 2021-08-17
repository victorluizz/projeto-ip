import pygame as pg

##########################
# --> FUNÇÃO PARA RODAR O JOGO
##########################

# --> INICIALIZAÇÃO
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
display = pg.display.set_mode((800,600))
pg.display.set_caption("Gotta catch 'em all!")
map = pg.image.load("images/background.png")
map = pg.transform.scale(map, (800, 600))
icon = pg.image.load("images/icon.png")
pg.display.set_icon(icon)


icon_poke = pg.image.load("images/pokeball.png")

# --> INICIALIZAÇÃO E O CARRREGAMENTO DA MÚSICA DE FUNDO  ((PS: TÁ DANDO UNS BUGS VOU ARRUMAR DPS BY: SEVE))
#pg.mixer.init()
#pg.mixer.music.load("sounds/fundo.mp3")
#pg.mixer.music.play(-1)

# --> PONTUAÇÃO DO JOGO
score_value = 0
font = pg.font.Font("freesansbold.ttf", 32)
text_position_x = 10
text_position_y = 10

def main():
    # --> LOOP INFINITO QUE RODA O GAME 
    while True:
        #VERIFICAÇÃO PARA O FECHAMENTO DA JANELA
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()   

        
        score = font.render("PONTUAÇÃO: " +str(score_value), True,  (255,255,255)) 
        display.fill((0,0,0))
        display.blit(map, (0,0))
        display.blit(score, (10,10))
        #display.blit(icon_poke, (10,10))
        #ATUALIZA O DISPLAY
        pg.display.update()
           
main()