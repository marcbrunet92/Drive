# 03-01-2025
# Boucle bornée - Calcul de factorielle de n

n = int(input("Entrez un entier naturel non nul : "))

F = 1

for k in range(1,n+1) :
    F = F * k
    
print('Factorielle de', n, 'vaut', F,'.')