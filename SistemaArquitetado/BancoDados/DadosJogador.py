import pygame as pg

#Exibicao do Jogador
LarguraJogador,AlturaJogador = 35,35
XJogador,YJogador = 315,280

#Jogador = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)
GrupoJogador = pg.sprite.Group()
Jogador = pg.sprite.Sprite(GrupoJogador)
Jogador.image = pg.image.load('Recursos/images/Jogador_FrenteB.png')
Jogador.image = pg.transform.scale(Jogador.image, [35,35])
Jogador.rect = pg.Rect(XJogador,YJogador,LarguraJogador,AlturaJogador)

#Situação em Relação à Animação
DireitaJogador,EsquerdaJogador,AcimaJogador,AbaixoJogador = 0,0,0,0

#Situaçaõ em Relação à Movimentação
QuantidadePassos = 0
JogadorMovendoDireita = False
JogadorMovendoEsquerda = False
JogadorMovendoAbaixo = False
JogadorMovendoAcima = False