from Logica import RodarLogica as RL
from Logica import AtualizarTela as AT
import time

from SistemaArquitetado.BancoDados import DadosJogador as DJ

def AtualizarTudo():
    InicioTempo = time.time()
    RL.AtualizarDados()
    AT.AtualizarTela()
    FinalTempo = time.time()
    TempoDeEspera = (1 - (FinalTempo-InicioTempo))/180
    #print(f'tempo para rodar o código de {FinalTempo-InicioTempo}')
    time.sleep(TempoDeEspera)
    #TempoAposSleep = time.time()
    #TempoFrame = (TempoAposSleep-InicioTempo)
    #print(f'tempo após sleep de {TempoAposSleep-FinalTempo}')
    #print(f'Quantidade de Frames de {1/(TempoAposSleep-InicioTempo)}')
    #print(f'Tempo de 1 frame de {TempoFrame}')