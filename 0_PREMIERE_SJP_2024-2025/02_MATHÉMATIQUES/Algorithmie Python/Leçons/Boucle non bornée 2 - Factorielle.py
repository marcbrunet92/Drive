# 03-01-2025
# Boucle non bornée - Calcul de factorielle de n    

n = int(input("Entrez un entier naturel non nul : "))

F = 1
k = 1

while k <= n :
    F = F * k
    k = k +1
    
print('Factorielle de', n, 'vaut', F,'.')
