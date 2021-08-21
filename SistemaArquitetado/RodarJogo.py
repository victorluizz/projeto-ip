import pygame as pg
from Logica import LogicaSons as LS
from Logica import LogicaTela as LT
import AtualizarTudo as AT
from BancoDados import DadosJogador as DJ

def RodarJogo():
    LS.TocarMusicaFundo()
# Loop do Jogo
    while LT.JanelaAberta:
        AT.AtualizarTudo()
        for evento in pg.event.get():
            #Para fechar a janela ao clicar no x
            if evento.type == pg.QUIT:
                LT.JanelaAberta = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_e:
                    print(f'O X do Jogador é {DJ.XJogador} e o Y dele é {DJ.YJogador}')