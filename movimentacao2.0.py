import pygame as pg
pg.init()
import math

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
XJogador,YJogador = 315,280

#Quantos pixels ele anda por quadrado
VelocidadeJogador = 35

#O jogador começa parado
JogadorMovendo = False

#Loop da Janela
JanelaAberta = True

#Informações do Jogador
#Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
GrupoJogador = pg.sprite.Group()
Jogador = pg.sprite.Sprite(GrupoJogador)
Jogador.image = pg.image.load('images/Jogador_Frente.png')
Jogador.image = pg.transform.scale(Jogador.image, [35,35])
Jogador.rect = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
icone = False

direita, esquerda, baixo, cima = 0,0,0,0

def SpriteJogadorDireita():
    if direita%4 == 0:
        return(pg.image.load('images/Jogador_DireitaB.png'))
    if direita%4 == 1:
        return(pg.image.load('images/Jogador_Direita1B.png'))
    if direita%4 == 2:
        return(pg.image.load('images/Jogador_DireitaB.png'))
    if direita%4 == 3:
        return (pg.image.load('images/Jogador_Direita2B.png'))
def SpriteJogadorEsquerda():
    if esquerda%4 == 0:
        return(pg.image.load('images/Jogador_EsquerdaB.png'))
    if esquerda%4 == 1:
        return(pg.image.load('images/Jogador_Esquerda1B.png'))
    if esquerda%4 == 2:
        return(pg.image.load('images/Jogador_EsquerdaB.png'))
    if esquerda%4 == 3:
        return (pg.image.load('images/Jogador_Esquerda2B.png'))
def SpriteJogadorFrente():
    if baixo%4 == 0:
        return(pg.image.load('images/Jogador_FrenteB.png'))
    if baixo%4 == 1:
        return(pg.image.load('images/Jogador_Frente1B.png'))
    if baixo%4 == 2:
        return(pg.image.load('images/Jogador_FrenteB.png'))
    if baixo%4 == 3:
        return (pg.image.load('images/Jogador_Frente2B.png'))
def SpriteJogadorCostas():
    if cima%4 == 0:
        return(pg.image.load('images/Jogador_CostasB.png'))
    if cima%4 == 1:
        return(pg.image.load('images/Jogador_Costas1B.png'))
    if cima%4 == 2:
        return(pg.image.load('images/Jogador_CostasB.png'))
    if cima%4 == 3:
        return (pg.image.load('images/Jogador_Costas2B.png'))

Jogador.image = SpriteJogadorFrente()

# Loop do Jogo.
if __name__ == '__main__':
    while JanelaAberta:
        for evento in pg.event.get():
            #Para fechar a janela ao clicar no x
            if evento.type == pg.QUIT:
                JanelaAberta = False
            # Contadores
            score_1 = font_1.render(str(score_value_1), True, (255, 255, 255))
            score_2 = font_1.render(str(score_value_1), True, (255, 255, 255))
            display.fill((0, 0, 0))
            display.blit(map, (0, 0))
            GrupoJogador.draw(display)
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
                Jogador.image = SpriteJogadorDireita()
                direita += 1
                #Os while são para criar um movimento contínuo
                inicio = XJogador
                final = XJogador
                while final - inicio < 35:
                    XJogador+=3.5
                    final = XJogador
                    # Desenha um fundo preto
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))
                    # Atualiza o Jogador e desenha ele na janela
                    Jogador.rect = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    GrupoJogador.draw(display)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    # Atualiza a janela
                    pg.display.update()
                icone = False
            if teclas[pg.K_a] and XJogador > 0:
                icone = True
                Jogador.image = SpriteJogadorEsquerda()
                esquerda += 1
                inicio = XJogador
                final = XJogador
                while math.fabs(final - inicio) < 35:
                    XJogador -= 3.5
                    final = XJogador
                    # Desenha um fundo preto
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))
                    # Atualiza o Jogador e desenha ele na janela
                    Jogador.rect = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    GrupoJogador.draw(display)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    # Atualiza a janela
                    pg.display.update()
                icone = False
            if teclas[pg.K_s] and YJogador < AlturaJanela - LarguraJogador:
                icone = True
                Jogador.image = SpriteJogadorFrente()
                baixo += 1
                inicio = YJogador
                final = YJogador
                while final - inicio < 35:
                    YJogador += 3.5
                    final = YJogador
                    # Desenha um fundo preto
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))
                    # Atualiza o Jogador e desenha ele na janela
                    Jogador.rect = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    GrupoJogador.draw(display)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    # Atualiza a janela
                    pg.display.update()
                icone = False
            if teclas[pg.K_w] and YJogador > 0:
                icone = True
                Jogador.image = SpriteJogadorCostas()
                cima += 1
                inicio = YJogador
                final = YJogador
                while math.fabs(final - inicio) < 35:
                    YJogador -= 3.5
                    final = YJogador
                    # Desenha um fundo preto
                    display.fill((0, 0, 0))
                    display.blit(map, (0, 0))
                    # Atualiza o Jogador e desenha ele na janela
                    Jogador.rect = pg.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    GrupoJogador.draw(display)
                    display.blit(score_1, (50, 15))
                    display.blit(score_2, (50, 50))
                    display.blit(icon_poke_1, (10, 10))
                    display.blit(icon_poke_2, (10, 45))
                    # Atualiza a janela
                    pg.display.update()
                icone = False
        pg.display.update()
