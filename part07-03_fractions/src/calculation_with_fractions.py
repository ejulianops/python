from fractions import Fraction

def fractionate(amount: int):

    fractions = []

    for i in range(1, amount+1):
        fractions.append(Fraction(1, amount))

    return fractions
       