import pygame as pg
from SistemaArquitetado.BancoDados import DadosJogador as DJ
from SistemaArquitetado.Logica.Jogador import LogicaInputs as LI

def SpriteJogadorDireita():
    if DJ.DireitaJogador==20:
        DJ.DireitaJogador = 0
    if DJ.DireitaJogador in range (0,4):
        return(pg.image.load('Recursos/images/Jogador_DireitaB.png'))
    if DJ.DireitaJogador in range (4,10):
        return(pg.image.load('Recursos/images/Jogador_Direita1B.png'))
    if DJ.DireitaJogador in range (10,14):
        return(pg.image.load('Recursos/images/Jogador_DireitaB.png'))
    if DJ.DireitaJogador in range (14,20):
        return (pg.image.load('Recursos/images/Jogador_Direita2B.png'))
def SpriteJogadorEsquerda():
    if DJ.EsquerdaJogador == 20:
        DJ.EsquerdaJogador = 0
    if DJ.EsquerdaJogador in range(0, 4):
        return (pg.image.load('Recursos/images/Jogador_EsquerdaB.png'))
    if DJ.EsquerdaJogador in range(4, 10):
        return (pg.image.load('Recursos/images/Jogador_Esquerda1B.png'))
    if DJ.EsquerdaJogador in range(10, 14):
        return (pg.image.load('Recursos/images/Jogador_EsquerdaB.png'))
    if DJ.EsquerdaJogador in range(14, 20):
        return (pg.image.load('Recursos/images/Jogador_Esquerda2B.png'))
def SpriteJogadorFrente():
    if DJ.AbaixoJogador == 20:
        DJ.AbaixoJogador = 0
    if DJ.AbaixoJogador in range(0, 4):
        return (pg.image.load('Recursos/images/Jogador_FrenteB.png'))
    if DJ.AbaixoJogador in range(4, 10):
        return (pg.image.load('Recursos/images/Jogador_Frente1B.png'))
    if DJ.AbaixoJogador in range(10, 14):
        return (pg.image.load('Recursos/images/Jogador_FrenteB.png'))
    if DJ.AbaixoJogador in range(14, 20):
        return (pg.image.load('Recursos/images/Jogador_Frente2B.png'))
def SpriteJogadorCostas():
    if DJ.AcimaJogador == 20:
        DJ.AcimaJogador = 0
    if DJ.AcimaJogador in range(0, 4):
        return (pg.image.load('Recursos/images/Jogador_CostasB.png'))
    if DJ.AcimaJogador in range(4, 10):
        return (pg.image.load('Recursos/images/Jogador_Costas1B.png'))
    if DJ.AcimaJogador in range(10, 14):
        return (pg.image.load('Recursos/images/Jogador_CostasB.png'))
    if DJ.AcimaJogador in range(14, 20):
        return (pg.image.load('Recursos/images/Jogador_Costas2B.png'))

def LogicaAnimacaoJogador():
    if DJ.JogadorMovendoDireita:
        DJ.DireitaJogador += 1
        DJ.Jogador.image = SpriteJogadorDireita()
    if DJ.JogadorMovendoEsquerda:
        DJ.EsquerdaJogador += 1
        DJ.Jogador.image = SpriteJogadorEsquerda()
    if DJ.JogadorMovendoAbaixo:
        DJ.AbaixoJogador += 1
        DJ.Jogador.image = SpriteJogadorFrente()
    if DJ.JogadorMovendoAcima:
        DJ.AcimaJogador += 1
        DJ.Jogador.image = SpriteJogadorCostas()