from sys import setrecursionlimit as SRL
SRL(10000)

# fonction à analyser
def f(x:float) -> float:
    return x**2 - 1 

def dich_recursive(a:float, b:float, f, p:float, compteur:int = 0) -> (float, int):
    # Verification des entrées
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a et b doivent être des réels")
    if not callable(f):
        raise TypeError("f doit être une fonction prenant un float et retournant un float")
    if not isinstance(p, (int, float)):
        raise TypeError("p doit être un réel")
    if p <= 0:
        raise ValueError(f"la valeur de p : {p} doit être strictement positive")
    if f(a)*f(b) > 0:
        raise ValueError(f"f({a})*f({b}) n'est pas négatif")

    # algorithme dichotomique
    c = (a+b)/2
    if abs(a-b)<p:
        return c, compteur
    if f(c)*f(a)<=0:
        return dich_recursive(a, c, f, p, compteur = compteur + 1)
    return dich_recursive(c, b, f, p, compteur = compteur + 1)

for i in range(-1, -5, -1):
    print(dich_recursive(-1, 1, f, 10**i))
