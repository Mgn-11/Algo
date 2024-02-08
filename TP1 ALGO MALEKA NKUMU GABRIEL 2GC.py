#auteur du code MALEKA NKUMU GABRIEL

# 1. créons une classe Fraction
#la classe Fraction a pour attributs  : num et den des entiers représentants le numérateur et le dénominateur

class Fraction:
    def __init__(self, num, den): # on définit les attributs 
        assert den > 0, " uniquement si le denomonateur est strictement positif."
        self._num = num
        self._den = den
        
# 2. creation d'une méthode spéciale **str de ce fait on aura donc :

    def __str__(self):
        if self._den == 1:
            return str(self._num)
        else:
            return F"{self._num}/{self._den}"
        
# creation des instances F1, F2,F3 et F4

F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

#affichage de nos instances

print(F1)
print(F2)
print(F3)
print(F4)

# ecrivons la méthode speciale eq qui permet de renvoyer true si,les deux fractions sont égales

def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._num * other._den == other._num * self._den
        else:
            return False
# test du code 
F1 = Fraction(3, 4)
F2 = Fraction(6, 8)
F3 = Fraction(-10, 5)
F4 = Fraction(6,8)

print(F1==F2)
print(F1==F3)
print(F2==F3)
print(F3==F4)
