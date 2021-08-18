import pygame as pg

##########################
# --> FUNÇÃO PARA RODAR O JOGO
##########################

# --> INICIALIZAÇÃO
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
display = pg.display.set_mode((700, 630))
pg.display.set_caption("Gotta catch 'em all!")
map = pg.image.load("images/background.png")
map = pg.transform.scale(map, (700, 630))
icon = pg.image.load("images/icon.png")
pg.display.set_icon(icon)
icon_poke_1 = pg.image.load("images/pokebola.png")
icon_poke_2 = pg.image.load("images/pikachu.png")
icon_poke_1 = pg.transform.smoothscale(icon_poke_1, (30, 30))
icon_poke_2 = pg.transform.smoothscale(icon_poke_2, (30, 30))


# --> INICIALIZAÇÃO E O CARRREGAMENTO DA MÚSICA DE FUNDO  ((PS: TÁ DANDO UNS BUGS VOU ARRUMAR DPS BY: SEVE))
pg.mixer.init()
pg.mixer.music.load("sounds/fundo.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)

# --> PONTUAÇÃO DO JOGO
score_value_1 = 0
font_1 = pg.font.Font("freesansbold.ttf", 25)

score_value_2 = 0
font_2 = pg.font.Font("freesansbold.ttf", 25)


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
        # Contadores
        score_1 = font_1.render(str(score_value_1), True, (255, 255, 255))
        score_2 = font_1.render(str(score_value_1), True, (255, 255, 255))
        display.fill((0, 0, 0))
        display.blit(map, (0, 0))
        display.blit(score_1, (50, 5))
        display.blit(score_2, (50, 40))
        display.blit(icon_poke_1, (10, 10))
        display.blit(icon_poke_2, (10, 45))

        # ATUALIZA O DISPLAY
        pg.display.update()


main()
