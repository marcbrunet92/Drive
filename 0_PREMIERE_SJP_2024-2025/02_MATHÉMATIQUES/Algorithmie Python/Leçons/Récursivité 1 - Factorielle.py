# 03-01-2025
# Récursivité - Factorielle    

n = int(input("Entrez un entier naturel non nul : "))


def F(n) :
    if n == 0 :
        return(1)
    else :
        return n * F(n-1)

print('Factorielle de', n, 'vaut', F(n),'.')
