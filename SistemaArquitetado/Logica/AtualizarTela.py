import pygame as pg
from SistemaArquitetado.Logica import LogicaTela as LT
from SistemaArquitetado.BancoDados import DadosMapa as DM
from SistemaArquitetado.BancoDados import DadosJogador as DJ
from SistemaArquitetado.BancoDados import DadosIcones as DI
from SistemaArquitetado.BancoDados import DadosInimigo as DIn

def AtualizarTela():
    LT.display.fill((0, 0, 0))
    LT.display.blit(DM.map, (0, 0))
    #Itens
    #DIn.GrupoInimigo.draw(LT.display)
    DJ.GrupoJogador.draw(LT.display)
    LT.display.blit(DI.score_1, (50, 15))
    LT.display.blit(DI.score_2, (50, 50))
    LT.display.blit(DI.icon_poke_1, (10, 10))
    LT.display.blit(DI.icon_poke_2, (10, 45))
    pg.display.update()