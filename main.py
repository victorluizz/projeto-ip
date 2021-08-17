import pygame as pg

pg.init()

##########################
# --> FUNÇÃO PARA RODAR O JOGO
##########################

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO MAPA/ SETAR O ICONE DO JOGO NA ABA
display = pg.display.set_mode((1080, 720))
pg.display.set_caption("Gotta catch 'em all!")
mapa = pg.image.load("images/background.png")
mapa = pg.transform.scale(mapa, (1080, 720))


# icon = pg.image.load("images/icon.png")
# pg.display.set_icon(icon)


# --> INICIALIZAÇÃO E O CARRREGAMENTO DA MÚSICA DE FUNDO  ((PS: TÁ DANDO UNS BUGS VOU ARRUMAR DPS BY: SEVE))
# pg.mixer.init()
# pg.mixer.music.load("/home/juninho/Documentos/PROJETO-IP/fundo.mp3")
# pg.mixer.music.play(-1)


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

        display.fill((0, 0, 0))
        display.blit(mapa, (0, 0))

        # ATUALIZA O DISPLAY
        pg.display.update()


main()
