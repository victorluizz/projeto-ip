import pygame as pg

#Exibicao do Inimigo
LarguraInimigo,AlturaInimigo = 35,35
XInimigo,YInimigo = 0,0

GrupoInimigo = pg.sprite.Group()
Inimigo = pg.sprite.Sprite(GrupoInimigo)
Inimigo.image = pg.image.load('Recursos/images/Jogador_FrenteB.png')
Inimigo.image = pg.transform.scale(Inimigo.image, [35,35])
Inimigo.rect = pg.Rect(XInimigo,YInimigo,LarguraInimigo,AlturaInimigo)

#Situação em Relação à Animaçaõ
DireitaInimigo,EsquerdaInimigo,AcimaInimigo,AbaixoInimigo = 0,0,0,0
QuantidadePassos = 0
InimigoMovendoDireita = False
InimigoMovendoEsquerda = False
InimigoMovendoAbaixo = False
InimigoMovendoAcima = False