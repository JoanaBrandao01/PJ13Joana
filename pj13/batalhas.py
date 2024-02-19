from abc import ABC, abstractmethod

class BattleTemplate(ABC):
    def executeBattle(self):
        self.prepare()        
        self.performAttack()  
        self.performDefense() 
        self.conclude()       

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def performAttack(self):
        pass

    @abstractmethod
    def performDefense(self):
        pass

    @abstractmethod
    def conclude(self):
        pass

class AggressiveBattle(BattleTemplate):
    def prepare(self):
        print("Preparing for aggressive battle...")

    def performAttack(self):
        print("Executing aggressive attack...")

    def performDefense(self):
        print("Performing minimal defense...")

    def conclude(self):
        print("Concluding aggressive battle...")

class BalancedBattle(BattleTemplate):
    def prepare(self):
        print("Preparing for balanced battle...")

    def performAttack(self):
        print("Executing balanced attack...")

    def performDefense(self):
        print("Performing balanced defense...")

    def conclude(self):
        print("Concluding balanced battle...")

def startBattle(battle):
    print("Starting battle...")
    battle.executeBattle()

# Exemplo de Uso
aggressive_battle = AggressiveBattle()
balanced_battle = BalancedBattle()

startBattle(aggressive_battle)
print("-" * 20)
startBattle(balanced_battle)  

#o código apenas imprime (Starting battle...
#Preparing for aggressive battle...
#Executing aggressive attack...
#Performing minimal defense...
#Concluding aggressive battle...
#--------------------
#Starting battle...
#Preparing for balanced battle...
#Executing balanced attack...
#Performing balanced defense...
#Concluding balanced battle...)
#podemos subtituir ele por um print(substituído pelo main.py) (dead code)

#apenas nesse código temos 3 code smells (dead code, comentários e o nome do arquivo)
#troquei o nome de war-game para batalhas