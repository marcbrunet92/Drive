# 01-01-2025
# Boucle bornée - Calcul de  1 + 2 + ... + n


n = int(input("Entrez un entier naturel non nul : "))

S = 0

for i in range(1, n + 1) :
    S = S + i

print('La somme des', n, 'premiers entiers naturels est', S,'.')
