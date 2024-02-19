#"Como jogador eu gostaria de colocar exércitos nos meus territórios. A quantidade de exércítos é um número inteiro e, 
#caso o territórios já possua dono, a operação será negada."
class Territorio:
    def __init__(self,jogador=None):
        self.dono = jogador
        self.exercitoTerritorio = 0

    def addExercito(self,qtdExercitos):
        if self.dono is None:
            self.exercitoTerritorio =+ qtdExercitos
        else:
            print("Operação negada")

    def getExercitos(self):
        return self.exercitoTerritorio



