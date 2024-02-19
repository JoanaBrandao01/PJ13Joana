import random
from jogador import Player
from territorio import Territorio
def BatalhaAgressiva():
    print("Iniciando batalha...\nPreparando para batalha agressiva...\nExecutando batalha agressiva...\nPerformando defesa mínima...\nConcluindo batalha agressiva...")
    
def BatalhaBalanceada():
    print("Iniciando batalha\nPreparando para a batalha balanceada...\nExecutando ataque balanciado...\nPerformando defesa balanceada...\nConcluíndo batalha balnceada...")

def execucao():
    return print("Executando ataque agressivo...\nExecutando defesa forte... \nExecutando ataque balanceado...")

def ganhador(player1,player2):
   ganhador = random.choice([player1, player2])
   print("O ganhador da batalha foi:", ganhador)

jogador1 = Player("Jogador 1")
jogador2 = Player("Jogador 2")

territorio1 = Territorio(jogador1)
territorio2 = Territorio()

exercitos=int(input("Digite a quantidade e exércitos que deseja colocar no território:"))
territorio2.addExercito(exercitos)
print("Exércitos adicionados com sucesso no território 2!\n A quantidade de exércitos no território 2 é:")
print(territorio2.getExercitos())




BatalhaAgressiva()
print("-" * 20)
BatalhaBalanceada() 
execucao()
ganhador(jogador1.getNome(),jogador2.getNome())

