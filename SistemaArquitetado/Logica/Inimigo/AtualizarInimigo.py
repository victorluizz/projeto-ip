import pygame as pg
from SistemaArquitetado.Logica.Inimigo import LogicaMovimentacao as LM
from SistemaArquitetado.BancoDados import DadosInimigo as DI

def AtualizarInimigo():
    if DI.QuantidadePassos == 10:
        DI.InimigoMovendoDireita, DI.InimigoMovendoEsquerda, DI.InimigoMovendoAbaixo, DI.InimigoMovendoAcima = False, False, False, False
        DI.QuantidadePassos = 0
    LM.LogicaMovimentacaoInimigo()
    #LA.LogicaAnimacaoJogador()
    DI.Inimigo.rect = pg.Rect(DI.XInimigo, DI.YInimigo, DI.LarguraInimigo, DI.AlturaInimigo)