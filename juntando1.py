import pygame as pg
import random
pg.init()

import time

#Tamanho da Janela
LarguraJanela,AlturaJanela = 700,630

#Criar a janela (fora do loop)
display = pg.display.set_mode([LarguraJanela,AlturaJanela])
pg.display.set_caption("Gotta catch 'em all")
#-------------------------------
# --> INICIALIZAÇÃO DA TELA /NOME DA JANELA(GAME)/ CARREGAR A IMAGEM DO map/ SETAR O ICONE DO JOGO NA ABA
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

def movimento_cookie():
    global cookie_x
    global cookie_y
    cookie_x = random.randint(0, 700 - cookie_width)
    cookie_y = random.randint(0, 630 - cookie_height)

icone = False

def atualizar():
    display.fill((0, 0, 0))
    display.blit(map, (0, 0))
    display.blit(score_1, (50, 5))
    display.blit(score_2, (50, 40))
    display.blit(icon_poke_1, (10, 10))
    display.blit(icon_poke_2, (10, 45))

#------------------------------

#Exibicao do Jogador
LarguraJogador,AlturaJogador = 35,35
XJogador,YJogador = 0,0

#Quantos pixels ele anda por quadrado
VelocidadeJogador = 35
cookie_width = 20
cookie_height = 20
green = ((255, 255, 0))
cookie_color = green
cookie_x = 50
cookie_y = 50
#O jogador começa parado
JogadorMovendo = False

#Loop da Janela
JanelaAberta = True


#Informações do Jogador
Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)

# Loop do Jogo.
if __name__ == '__main__':
    while JanelaAberta:
        for evento in pg.event.get():
            #Para fechar a janela ao clicar no x
            if evento.type == pg.QUIT:
                JanelaAberta = False

            jogador_centerx = XJogador + (LarguraJogador / 2)
            jogador_centery = YJogador + (AlturaJogador / 2)

            cookie_centerx = cookie_x + (cookie_width / 2)
            cookie_centery = cookie_y + (cookie_height / 2)

            cookie_distancex = abs(jogador_centerx - cookie_centerx) - (LarguraJogador / 2 + cookie_width / 2)
            cookie_distancey = abs(jogador_centery - cookie_centery) - (AlturaJogador / 2 + cookie_height / 2)
            # Contadores
            score_1 = font_1.render(str(score_value_1), True, (0, 255, 255))
            score_2 = font_1.render(str(score_value_2), True, (0, 255, 255))
            display.fill((0, 0, 0))
            display.blit(map, (0, 0))
            pg.draw.rect(display, cookie_color, (int(cookie_x), int(cookie_y), cookie_width, cookie_height))
            pg.draw.rect(display, [255, 255, 255, 255], Jogador)
            if not icone:
                display.blit(score_1, (50, 15))
                display.blit(score_2, (50, 50))
                display.blit(icon_poke_1, (10, 10))
                display.blit(icon_poke_2, (10, 45))

        #Para habilitar o pressionamento das teclas
        teclas = pg.key.get_pressed()
        if not JogadorMovendo:
            #Os ifs são para registrar o apertar de uma tecla
            if teclas[pg.K_d] and XJogador < LarguraJanela - LarguraJogador:
                icone = True
                #Os for são para criar um movimento contínuo
                for i in range(VelocidadeJogador//5):
                    #Muda a posição do jogador na variável
                    XJogador += 5
                    #Desenha um fundo preto
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))

                    #Atualiza o Jogador e desenha ele na janela
                    cookie_width = 20
                    cookie_height = 20
                    green = ((255, 255, 0))
                    cookie_color = green
                    cookie_x = 50
                    cookie_y = 50
                    pg.draw.rect(display, cookie_color, (int(cookie_x), int(cookie_y), cookie_width, cookie_height))
                    Jogador = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pg.draw.rect(display, [255, 255, 255, 255], Jogador)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    #Atualiza a janela
                    pg.display.update()
                    #Tempo da movimentação de cada pixel
                    #time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
                icone = False
            if teclas[pg.K_a] and XJogador > 0:
                icone = True
                for i in range(VelocidadeJogador//5):
                    XJogador -= 5
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))

                    cookie_width = 20
                    cookie_height = 20
                    green = ((255, 255, 0))
                    cookie_color = green
                    cookie_x = 50
                    cookie_y = 50
                    pg.draw.rect(display, cookie_color, (int(cookie_x), int(cookie_y), cookie_width, cookie_height))
                    Jogador = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pg.draw.rect(display, [255, 255, 255, 255], Jogador)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    pg.display.update()
                    #time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
                icone = False
            if teclas[pg.K_s] and YJogador < AlturaJanela - LarguraJogador:
                icone = True
                for i in range(VelocidadeJogador//5):
                    YJogador += 5
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))

                    cookie_width = 20
                    cookie_height = 20
                    green = ((255, 255, 0))
                    cookie_color = green
                    cookie_x = 50
                    cookie_y = 50
                    pg.draw.rect(display, cookie_color, (int(cookie_x), int(cookie_y), cookie_width, cookie_height))
                    Jogador = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pg.draw.rect(display, [255, 255, 255, 255], Jogador)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    pg.display.update()
                    #time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
                icone = False
            if teclas[pg.K_w] and YJogador > 0:
                icone = True
                for i in range(VelocidadeJogador//5):
                    YJogador -= 5
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))

                    cookie_width = 20
                    cookie_height = 20
                    green = ((255, 255, 0))
                    cookie_color = green
                    cookie_x = 50
                    cookie_y = 50
                    pg.draw.rect(display, cookie_color, (int(cookie_x), int(cookie_y), cookie_width, cookie_height))
                    Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
                    pg.draw.rect(display, [255, 255, 255, 255], Jogador)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    pg.display.update()
                    #time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
                icone = False
                if cookie_distancex <= 0 and cookie_distancey <= 0:
                    movimento_cookie()
                    score_value_1 += 1

        if JogadorMovendo:
            #Para que haja um delay entre o registo de cada pressionar
            #Também para impedir movimento diagonal
            time.sleep(0.0625)
            JogadorMovendo = False


        pg.display.update()