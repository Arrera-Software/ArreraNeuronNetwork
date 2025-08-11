from fnc.fncBase import fncBase,gestionnaire

class fncCalculatrice(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__nb1Complex = complex(0, 0)
        self.__nb2Complex = complex(0, 0)

    def adition(self, a:int, b:int):
        return a + b

    def divsion(self, a:int,b:int):
        if b == 0:
            return None
        return a / b

    def multiplication(self, a:int,b:int):
        return a * b

    def soustraction(self, a:int,b:int):
        return a - b

    def puissance(self, a:int,b:int):
        return a ** b

    def modulo(self, a:int,b:int):
        if b == 0:
            return None
        return a % b

    def racine(self, a:int,b:int):
        if a < 0 or b <= 0:
            return None
        return a ** (1 / b)

    # Nombre complexe

    def setComplexNb(self,nb1_1:int,nb1_2:int,nb2_1:int,nb2_2:int):
        self.__nb1Complex = complex(nb1_1, nb1_2)
        self.__nb2Complex = complex(nb2_1, nb2_2)

    def recuperationNb1Complex(self):
        return str(self.__nb1Complex)

    def recuperationNb2Complex(self):
        return str(self.__nb2Complex)

    def aditionNbComplex(self):
        resultat = self.__nb1Complex + self.__nb2Complex
        return resultat

    def soustrationNbComplex(self):
        resultat = self.__nb1Complex - self.__nb2Complex
        return resultat

    def multiplicationNbComplex(self):
        resultat = self.__nb1Complex * self.__nb2Complex
        return resultat

    def divisionNbComplex(self):
        resultat = self.__nb1Complex / self.__nb2Complex
        return resultat