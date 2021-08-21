import pygame as pg
pg.init()

# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
icon = pg.image.load("Recursos/images/icon.png")
pg.display.set_icon(icon)
icon_poke_1 = pg.image.load("Recursos/images/pokebola.png")
icon_poke_2 = pg.image.load("Recursos/images/pikachu.png")
icon_poke_1 = pg.transform.smoothscale(icon_poke_1, (30, 30))
icon_poke_2 = pg.transform.smoothscale(icon_poke_2, (30, 30))

# --> PONTUAÇÃO DO JOGO
score_value_1 = 0
font_1 = pg.font.Font("freesansbold.ttf", 25)

score_value_2 = 0
font_2 = pg.font.Font("freesansbold.ttf", 25)

score_1 = font_1.render(str(score_value_1), True, (255, 255, 255))
score_2 = font_1.render(str(score_value_1), True, (255, 255, 255))