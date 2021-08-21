import pygame as pg
from SistemaArquitetado.BancoDados import DadosTela as DT
from SistemaArquitetado.BancoDados import DadosJogador as DJ

QuantidadePassos = 0

def LogicaInputsJogador():
    global JogadorMovendoDireita
    global JogadorMovendoEsquerda
    global JogadorMovendoAbaixo
    global JogadorMovendoAcima
    teclas = pg.key.get_pressed()
    if teclas[pg.K_d] and DJ.XJogador < DT.LarguraJanela - DJ.LarguraJogador:
        if  not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAbaixo and not DJ.JogadorMovendoAcima:
             DJ.JogadorMovendoDireita = True
    if teclas[pg.K_a] and DJ.XJogador > 0:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoAbaixo and not DJ.JogadorMovendoAcima:
            DJ.JogadorMovendoEsquerda = True
    if teclas[pg.K_s] and DJ.YJogador < DT.AlturaJanela - DJ.LarguraJogador:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAcima:
            DJ.JogadorMovendoAbaixo = True
    if teclas[pg.K_w] and DJ.YJogador > 0:
        if  not DJ.JogadorMovendoDireita and not DJ.JogadorMovendoEsquerda and not DJ.JogadorMovendoAbaixo:
            DJ.JogadorMovendoAcima = True