from fnc.fncBase import fncBase

class fncCalculatrice(fncBase):
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
