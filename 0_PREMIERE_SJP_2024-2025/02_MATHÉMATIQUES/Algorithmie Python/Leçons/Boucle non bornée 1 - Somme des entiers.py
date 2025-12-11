# 01-01-2025
# Boucle non bornée - Calcul de  1 + 2 + ... + n

n = int(input("Entrez un entier naturel non nul : "))

S = 0
i = 1

while i <= n :
    S = S + i
    i = i + 1

print('La somme des', n, 'premiers entiers naturels est', S,'.')