from Classe import Jogadores
from Classe import Jogo
Jogador = Jogadores("Duda Lisboa", 1.8, 6, 5, 10, 6, 7)
Jogador2= Jogadores("Ana Patrícia", 1.94, 5, 7, 6, 5, 6)
Jogador3 = Jogadores("Alana", 1.63, 9, 4, 5, 7, 4 )
jogoatual=Jogo()
Jogadores.detalhesJogador(Jogador)
jogoatual.Rodada1(Jogador)
Jogadores.detalhesJogador(Jogador2)
jogoatual.Rodada2(Jogador2)
Jogadores.detalhesJogador(Jogador3)
jogoatual.Rodada3(Jogador3)
jogoatual.exiblir_pontuacao()