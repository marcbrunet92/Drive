def division_euclidienne(a:int, b:int) -> (int, int):
    # Initialisation du quotient à 0
    q = 0
    # Cas de b non strictement positif
    if b <= 0:
        raise ValueError(f"Le diviseur : {b} n'est pas strictement positif")
    elif a == b :
        return 1, 0
    # Cas de b > 0
    else :
        # Cas de a < 0
        if a < 0:                                                           
            while b*q > a:
                q -= 1
        # Cas de a > 0
        elif a > 0:                                                              
            while b*q <= a:
                q += 1
            q += -1
    # Si a = 0, aucune condition n'est remplie est le quotient reste 0
    return q, a-(b*q)

def test():
    test_values = [-10, -5, -1, 0, 1, 5, 10]  # Valeurs de a
    divisors = [1, 2, 3, 5, 10]               # Valeurs de b 

    for b in divisors:
        for a in test_values:
            q, r = division_euclidienne(a, b)
            
            # Vérification de la relation a = b*q + r
            assert a == b * q + r, f"Erreur sur a={a}, b={b}: {a} est différent de b*{q} + {r} : {b*q+r}"

            # Vérification que le reste est dans [0, b)
            assert 0 <= r < b, f"Erreur sur a={a}, b={b}: reste r={r} hors de [0,{b}["

            # Vérification que division_euclidienne renvoie le bon résultat
            assert q == a//b and r == a % b, f"Quotient ou reste incorrect pour {a} divisée par {b}"
            
            print(f"a={a}, b={b} → quotient={q}, reste={r}")

    print("Pas d'erreur")

test()
