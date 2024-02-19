import random

class BattleObserver:
    def notifyWinner(self, winner): 
        pass

class BattleNotifier:
    def __init__(self):
        self.observers = [] 

    def addObserver(self, observer):
        self.observers.append(observer) 

    def removeObserver(self, observer):
        self.observers.remove(observer) 

    def notifyObservers(self, winner):
        for observer in self.observers:
            observer.notifyWinner(winner)


class Player(BattleObserver):
    def __init__(self, name, notifier):
        self.name = name
        self.notifier = notifier 
        self.notifier.addObserver(self)  

    def notifyWinner(self, winner):
        if winner == self:
            print(f"{self.name} venceu a batalha!")  


battle_notifier = BattleNotifier()

player1 = Player("Player 1", battle_notifier)
player2 = Player("Player 2", battle_notifier) 

winner = random.choice([player1, player2])
battle_notifier.notifyObservers(winner)

#neste código temos os seguintes code smells: comentários, o nome que era war-game e agora se chama ganhador
#classe BattleObserver dead code
#como o código apenas diz quem ganha baseado em uma escolha aleatória, o código será substituído pelo jogador.py
#além disso, todo o código rodará no main, então o código do jogador.py possui apenas métodos