import time
class Jogadores:
    def __init__(self, nomeJogador, alturaJogador, forcaJogador, velocidadeJogador, habilidadeJogador, pontariaJogador, tecnicaJogador,):
        self.nomeJogador = nomeJogador
        self.alturaJogador = alturaJogador
        self.forcaJogador = forcaJogador
        self.velocidadeJogador = velocidadeJogador
        self.habilidadeJogador = habilidadeJogador
        self.pontariaJogador = pontariaJogador
        self.tecnicaJogador = tecnicaJogador
    def detalhesJogador(self):
        print("A sua carta é:", self.nomeJogador, "--------> Altura:", self.alturaJogador)
        print("Força:", self.forcaJogador)
        print("Velocidade:", self.velocidadeJogador)
        print("Habilidade:", self.habilidadeJogador)
        print("Pontaria:", self.pontariaJogador)
        print("Técnica:", self.tecnicaJogador)
    def detalhesComputador(self):
        print("\nA carta do computador é:", self.nomeJogador, "--------> Altura:", self.alturaJogador)
        print("Força:", self.forcaJogador)
        print("Velocidade:", self.velocidadeJogador)
        print("Habilidade:", self.habilidadeJogador)
        print("Pontaria:", self.pontariaJogador)
        print("Técnica:", self.tecnicaJogador)
Emanuel = Jogadores("Emanuel Rego", 1.9, 7, 6, 9, 8, 10)
agatha = Jogadores("Ágatha", 1.82, 4, 8, 3, 4, 5)
andressa = Jogadores("Andressa Calvacanti", 1.75, 8, 9, 7, 3, 3)
class Jogo:
  def __init__ (self):
        self.pontojogador=0
        self.pontoconputador=0
  def contar_pontos (self,pontojogador,pontoconputador):
        self.pontojogador+=pontojogador
        self.pontoconputador+=pontoconputador
  def exiblir_pontuacao (self):
    print("--------------------PLACAR--------------------")
    print( '>>> Pontos feitos por você: ',self.pontojogador,'\n' ">>> Pontos feitos pelo computador: ",self.pontoconputador)
  def Rodada1(self,Jogador):
        categoria_escolhida = input(" --> Escolha uma categoria para ser comparada:\n(Digite 1 para:força; Digite 2 para:velocidade; Digite 3 para:habilidade; Digite 4 para:pontaria; Digite 5 para:técnica): ")
        if categoria_escolhida == "1":
            Jogador = Jogador.forcaJogador
            AtrComputador = Emanuel.forcaJogador
            print(">> A categoria escolhida foi: 'Força'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontojogador+=3 
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "2":
            Jogador = Jogador.velocidadeJogador
            AtrComputador = Emanuel.velocidadeJogador
            print(">> A categoria escolhida foi: 'Velocidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontojogador+=3
            else: 
                print("Infelizmente, você perdeu a rodada 1.")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "3":
            Jogador = Jogador.habilidadeJogador
            AtrComputador = Emanuel.habilidadeJogador
            print(">> A categoria escolhida foi: 'Habilidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontojogador+=3
                #pontosJogador += 3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "4":
            Jogador = Jogador.pontariaJogador
            AtrComputador = Emanuel.pontariaJogador
            print(">> A categoria escolhida foi: 'Pontaria'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!!, você ganhou a rodada 1!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "5":
            Jogador = Jogador.tecnicaJogador
            AtrComputador = Emanuel.tecnicaJogador
            print(">> A categoria escolhida foi: 'Técnica'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!!, você ganhou a rodada 1!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                print("")
                time.sleep(2)
                print("--------> RODADA 2")
                print("")
                self.pontoconputador+=3
  def Rodada2(self,Jogador2):
        categoria_escolhida = input(" --> Escolha uma categoria para ser comparada:\n(Digite 1 para:força; Digite 2 para:velocidade; Digite 3 para:habilidade; Digite 4 para:pontaria; Digite 5 para:técnica): ")
        if categoria_escolhida == "1":
            Jogador2 = Jogador2.forcaJogador
            Atr2Computador = agatha.forcaJogador
            print(">> A categoria escolhida foi: 'Força'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(agatha)
            if Jogador2 > Atr2Computador:
                print("PARABÉNS!!, você ganhou a rodada 2!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 2.")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "2":
            Jogador2 = Jogador2.velocidadeJogador
            Atr2Computador = agatha.velocidadeJogador
            print(">> A categoria escolhida foi: 'Velocidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(agatha)
            if Jogador2 > Atr2Computador:
                print("PARABÉNS!!, você ganhou a rodada 2!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 2.")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "3":
            Jogador2 = Jogador2.habilidadeJogador
            Atr2Computador = agatha.habilidadeJogador
            print(">> A categoria escolhida foi: 'Habilidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(agatha)
            if Jogador2 > Atr2Computador:
                print("PARABÉNS!!, você ganhou a rodada 2!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 2.")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "4":
            Jogador2 = Jogador2.pontariaJogador
            Atr2Computador = agatha.pontariaJogador
            print(">> A categoria escolhida foi: 'Pontaria'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(agatha)
            if Jogador2 > Atr2Computador:
                print("PARABÉNS!!, você ganhou a rodada 2!!")
                print("")
                print("--------> RODADA 3")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 2.")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "5":
            Jogador2 = Jogador2.tecnicaJogador
            Atr2Computador = agatha.tecnicaJogador
            print(">> A categoria escolhida foi: 'Técnica'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(agatha)
            if Jogador2 > Atr2Computador:
                print("PARABÉNS!!, você ganhou a rodada 2!!")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 2.")
                print("")
                time.sleep(2)
                print("--------> RODADA 3")
                print("")
                self.pontoconputador+=3
  def Rodada3(self,Jogador3):
        categoria_escolhida = input(" --> Escolha uma categoria para ser comparada:\n(Digite 1 para:força; Digite 2 para:velocidade; Digite 3 para:habilidade; Digite 4 para:pontaria; Digite 5 para:técnica): ")
        if categoria_escolhida == "1":
            Jogador3 = Jogador3.forcaJogador
            Atr3Computador = andressa.forcaJogador
            print(">> A categoria escolhida foi: 'Força'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(andressa)
            if Jogador3 > Atr3Computador:
                print("PARABÉNS!! Você ganhou a rodada 3!!")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 3.")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "2":
            Jogador3 = Jogador3.velocidadeJogador
            Atr3Computador = andressa.velocidadeJogador
            print(">> A categoria escolhida foi: 'Velocidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(andressa)
            if Jogador3 > Atr3Computador:
                print("PARABÉNS!! Você ganhou a rodada 3!!")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontojogador+=3
            else: 
                print("Infelizmente, você perdeu a rodada 3.")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "3":
            Jogador3 = Jogador3.habilidadeJogador
            AtrComputador = andressa.habilidadeJogador
            print(">> A categoria escolhida foi: 'Habilidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(andressa)
            if Jogador3 > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 3!!")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 3.")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "4":
            Jogador3 = Jogador3.pontariaJogador
            Atr3Computador = andressa.pontariaJogador
            print(">> A categoria escolhida foi: 'Pontaria'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(andressa)
            if Jogador3 > Atr3Computador:
                print("PARABÉNS!!, você ganhou a rodada 3!!")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 3.")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontoconputador+=3
        elif categoria_escolhida == "5":
            Jogador3= Jogador3.tecnicaJogador
            Atr3Computador = andressa.tecnicaJogador
            print(">> A categoria escolhida foi: 'Técnica'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesComputador(andressa)
            if Jogador3 > Atr3Computador:
                print("PARABÉNS!!, você ganhou a rodada 3!!")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontojogador+=3
            else:
                print("Infelizmente, você perdeu a rodada 3.")
                print("")
                time.sleep(2)
                print("------------------Fim de Jogo------------------")
                print("")
                self.pontoconputador+=3