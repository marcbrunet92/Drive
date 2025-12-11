# Version 01-01-2025
# Exercice Chap. Suites (d'après Déclic : 72)

from math import *

Cible = int(input("Entrez une population cible : "))

n = 0
p = 4000        # p(0)

while p < Cible :
    p = 1.05 * p - 100
    n = n + 1
    print(n, floor(p))

print ('Population cible atteinte au bout de', n, 'mois.')

