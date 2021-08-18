import pygame as pg

##########################
# --> FUNÇÃO PARA RODAR O JOGO
##########################

# --> INICIALIZAÇÃO
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
display = pg.display.set_mode((800, 600))
pg.display.set_caption("Gotta catch 'em all!")
map = pg.image.load("images/background.png")
map = pg.transform.scale(map, (800, 600))
# icon = pg.image.load("images/icon.png")
# pg.display.set_icon(icon)

# icon_poke = pg.image.load("images/pokeball.png")

# --> INICIALIZAÇÃO E O CARRREGAMENTO DA MÚSICA DE FUNDO  ((PS: TÁ DANDO UNS BUGS VOU ARRUMAR DPS BY: SEVE))
# pg.mixer.init()
# pg.mixer.music.load("sounds/fundo.mp3")
# pg.mixer.music.play(-1)

# --> PONTUAÇÃO DO JOGO
score_value_1 = 0
font_1 = pg.font.Font("freesansbold.ttf", 32)
text_position_x_1 = 10
text_position_y_1 = 10

score_value_2 = 0
font_2 = pg.font.Font("freesansbold.ttf", 32)
text_position_x_2 = 0
text_position_y_2 = 0

def main():
    # --> LOOP INFINITO QUE RODA O GAME
    while True:
        # VERIFICAÇÃO PARA O FECHAMENTO DA JANELA
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()

        score_1 = font_1.render("Pokemon x" + str(score_value_1), True, (255, 255, 255))
        score_2 = font_1.render("Pokebola x" + str(score_value_1), True, (255, 255, 255))
        display.fill((0, 0, 0))
        display.blit(map, (0, 0))
        display.blit(score_1, (5, 5))
        display.blit(score_2, (5, 40))
        # display.blit(icon_poke, (10,10))
        # ATUALIZA O DISPLAY
        pg.display.update()


main()
