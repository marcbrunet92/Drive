def racine_carree_heron(n, precision=1e-10):
    if n < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif")
    if n == 0:
        return 0
    
    def heron_recursif(x):
        x_new = (x + n / x) / 2
        if abs(x_new - x) < precision:
            return x_new
        return heron_recursif(x_new)
    
    return heron_recursif(n)

if __name__ == "__main__":
    nombres_test = [2, 9, 16, 25, 100, 2.5]
    
    print("=" * 50)
    print("ALGORITHME DE HÉRON - CALCUL DE RACINE CARRÉE")
    print("=" * 50)
    
    for num in nombres_test:
        resultat = racine_carree_heron(num)
        print(f"√{num} ≈ {resultat:.10f} (vérification: {resultat**2:.10f})")
    

    import math
    for num in nombres_test:
        result_heron = racine_carree_heron(num)
        result_math = math.sqrt(num)
        difference = abs(result_heron - result_math)
        print(f"√{num}: Héron={result_heron:.10f}, math.sqrt={result_math:.10f}, diff={difference:.2e}")