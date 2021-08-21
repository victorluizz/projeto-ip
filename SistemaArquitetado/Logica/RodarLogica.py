from SistemaArquitetado.Logica.Jogador import AtualizarJogador as AJ
from SistemaArquitetado.Logica.Inimigo import AtualizarInimigo as AI

def AtualizarDados():
    AI.AtualizarInimigo()
    #AtualizarItens()
    AJ.AtualizarJogador()
    #AtualizarHUD()