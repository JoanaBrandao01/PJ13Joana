
class AttackStrategy:
    def executeAttack(self):
        pass

class DefenseStrategy:
    def executeDefense(self):
        pass



class AggressiveAttack(AttackStrategy):
    def executeAttack(self):
        print("Executing aggressive attack...")

class BalancedAttack(AttackStrategy):
    def executeAttack(self):
        print("Executing balanced attack...")

class StrongDefense(DefenseStrategy):
    def executeDefense(self):
        print("Executing strong defense...")


class Player:
    def __init__(self, name):
        self.name = name
        self.attack_strategy = None
        self.defense_strategy = None

    def setAttackStrategy(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def setDefenseStrategy(self, defense_strategy):
        self.defense_strategy = defense_strategy

    def attack(self):
        if self.attack_strategy:
            self.attack_strategy.executeAttack() 
        else:
            print("No attack strategy set.") 
    def defend(self):
        if self.defense_strategy:
            self.defense_strategy.executeDefense()
        else:
            print("No defense strategy set.") 


player1 = Player("Player 1")
player1.setAttackStrategy(AggressiveAttack()) 
player1.setDefenseStrategy(StrongDefense())  

player1.attack()
player1.defend()  


player1.setAttackStrategy(BalancedAttack())
player1.attack()  


#O código apenas imprime (Executing aggressive attack...
#Executing strong defense... 
#Executing balanced attack...)
#as classes AttackStrategy e DefenseStrategy são dead codes
#não há lógica no código, portanto, pode ser substiruído por pela função execucao no main.py
#o nome war-game é um code smell pois é o mesmo nome dos outros, troquei o nome para execucao
#outro code smell são os comentários, que foram retirados