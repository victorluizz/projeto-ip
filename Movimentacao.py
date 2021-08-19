#Inicializar o Pygame
import pygame
pygame.init()

import time

#Tamanho da Janela
LarguraJanela,AlturaJanela = 700,630

#Criar a janela (fora do loop)
janela = pygame.display.set_mode([LarguraJanela,AlturaJanela])
pygame.display.set_caption("Gotta catch 'em all")

#Exibicao do Jogador
LarguraJogador,AlturaJogador = 35,35
XJogador,YJogador = 0,0

#Quantos pixels ele anda por quadrado
VelocidadeJogador = 35

#O jogador começa parado
JogadorMovendo = False

#Loop da Janela
JanelaAberta = True

#Função para preencher a tela
def desenhar(r, g, b):
    janela.fill([r, g, b])

#Informações do Jogador
Jogador = pygame.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)

# Loop do Jogo.
if __name__ == '__main__':
    while JanelaAberta:
        for evento in pygame.event.get():
            #Para fechar a janela ao clicar no x
            if evento.type == pygame.QUIT:
                JanelaAberta = False
        #Para habilitar o pressionamento das teclas
        teclas = pygame.key.get_pressed()
        if not JogadorMovendo:
            #Os ifs são para registrar o apertar de uma tecla
            if teclas[pygame.K_d] and XJogador < LarguraJanela - LarguraJogador:
                #Os for são para criar um movimento contínuo
                for i in range(VelocidadeJogador):
                    #Muda a posição do jogador na variável
                    XJogador += 1
                    #Desenha um fundo preto
                    desenhar(0, 0, 0)
                    #Atualiza o Jogador e desenha ele na janela
                    Jogador = pygame.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pygame.draw.rect(janela, [255, 255, 255, 255], Jogador)
                    #Atualiza a janela
                    pygame.display.update()
                    #Tempo da movimentação de cada pixel
                    time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
            if teclas[pygame.K_a] and XJogador > 0:
                for i in range(VelocidadeJogador):
                    XJogador -= 1
                    desenhar(0, 0, 0)
                    Jogador = pygame.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pygame.draw.rect(janela, [255, 255, 255, 255], Jogador)
                    pygame.display.update()
                    time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
            if teclas[pygame.K_s] and YJogador < AlturaJanela - LarguraJogador:
                for i in range(VelocidadeJogador):
                    YJogador += 1
                    desenhar(0, 0, 0)
                    Jogador = pygame.Rect(XJogador, YJogador, LarguraJogador, AlturaJogador)
                    pygame.draw.rect(janela, [255, 255, 255, 255], Jogador)
                    pygame.display.update()
                    time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
            if teclas[pygame.K_w] and YJogador > 0:
                for i in range(VelocidadeJogador):
                    YJogador -= 1
                    desenhar(0, 0, 0)
                    Jogador = pygame.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
                    pygame.draw.rect(janela, [255, 255, 255, 255], Jogador)
                    pygame.display.update()
                    time.sleep(0.03125 / VelocidadeJogador)
                JogadorMovendo = True
        if JogadorMovendo:
            #Para que haja um delay entre o registo de cada pressionar
            #Também para impedir movimento diagonal
            time.sleep(0.0625)
            JogadorMovendo = False
        pygame.draw.rect(janela, [255, 255, 255, 255], Jogador)
        pygame.display.update()