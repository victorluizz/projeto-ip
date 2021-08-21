from SistemaArquitetado.BancoDados import DadosInimigo as DI
from SistemaArquitetado.BancoDados import DadosJogador as DJ

def LogicaMovimentacaoInimigo():
    VetorX = DJ.XJogador - DI.XInimigo
    VetorY = DJ.YJogador - DI.YInimigo
    CasasX = VetorX/35
    CasasY = VetorY/35
    '''
    if CasasX > CasasY:
        Proporcao = CasasX//CasasY
    elif CasasY > CasasX:
        Proporcao = CasasY//CasasX
    else:
        Proporcao = 1
    if CasasX != 0:
        .
    if CasasY != 0:
        .'''
    if VetorX <0:
        DI.QuantidadePassos +=1
        DI.XInimigo -= 3.5
    elif VetorX >0:
        DI.QuantidadePassos += 1
        DI.XInimigo += 3.5
    if VetorY < 0:
        DI.QuantidadePassos += 1
        DI.YInimigo -= 3.5
    elif VetorY > 0:
        DI.QuantidadePassos += 1
        DI.YInimigo += 3.5