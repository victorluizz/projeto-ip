import pygame as pg
from SistemaArquitetado.BancoDados import DadosTela as DT

#Criar a janela (fora do loop)
display = pg.display.set_mode([DT.LarguraJanela,DT.AlturaJanela])
pg.display.set_caption("Gotta catch 'em all")

#Variável que Mantém a Janela Aberta
JanelaAberta = True