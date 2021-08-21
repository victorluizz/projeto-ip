import pygame as pg
from SistemaArquitetado.Logica.Jogador import LogicaInputs as LI
from SistemaArquitetado.BancoDados import DadosJogador as DJ

def LogicaMovimentacaoJogador():
    global QuantidadePassos
    if DJ.JogadorMovendoDireita:
        DJ.QuantidadePassos += 1
        DJ.XJogador += 3.5
    if DJ.JogadorMovendoEsquerda:
        DJ.QuantidadePassos += 1
        DJ.XJogador -= 3.5
    if DJ.JogadorMovendoAbaixo:
        DJ.QuantidadePassos += 1
        DJ.YJogador += 3.5
    if DJ.JogadorMovendoAcima:
        DJ.QuantidadePassos += 1
        DJ.YJogador -= 3.5

'''
def AtualizarLogica():
    AtualizarLogicaJogador()
'''