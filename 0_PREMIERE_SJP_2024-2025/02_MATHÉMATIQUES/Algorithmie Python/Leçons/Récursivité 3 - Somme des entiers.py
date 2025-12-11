# 05-01-2025
# Récursivité - Sommes des entiers    

n = int(input("Entrez un entier naturel non nul : "))


def S(n) :
    if n == 0 :
        return(0)
    else :
        return n + S(n-1)

print('La somme des entiers de 0 à', n, 'vaut', S(n),'.')
