import pygame as pg
from SistemaArquitetado.Logica.Jogador import LogicaInputs as LI
from SistemaArquitetado.Logica.Jogador import LogicaMovimentacao as LM
from SistemaArquitetado.Logica.Jogador import LogicaAnimacao as LA
from SistemaArquitetado.BancoDados import DadosJogador as DJ

def AtualizarJogador():
    if DJ.QuantidadePassos == 10:
        DJ.JogadorMovendoDireita, DJ.JogadorMovendoEsquerda, DJ.JogadorMovendoAbaixo, DJ.JogadorMovendoAcima = False, False, False, False
        DJ.QuantidadePassos = 0
    LI.LogicaInputsJogador()
    LM.LogicaMovimentacaoJogador()
    LA.LogicaAnimacaoJogador()
    DJ.Jogador.rect = pg.Rect(DJ.XJogador, DJ.YJogador, DJ.LarguraJogador, DJ.AlturaJogador)