# 03-01-2025
# Récursivité - PGCD via l'algorithme d'Euclide    

a = int(input("Entrez l'entier naturel a : "))
b = int(input("Entrez l'entier naturel b : "))

def PGCD(a,b) :
    if a % b == 0 :            # a%b est le résidu modulo a de b
        return(b)
    else :
        return PGCD(b,a%b)

print('Le PGCD de', a, 'et de', b, 'vaut', PGCD(a,b),'.')

