# fonction à analyser
def f(x:float) -> float:
    return x**2 + x - 1 

def dich_recursive(a:float, b:float, f, p:float, compteur:int = 0) -> tuple[float, int]:
    # algorithme récursif
    c = (a+b)/2
    if abs(a-b)<p:
        return c, compteur
    if f(c)*f(a)<=0:
        return dich_recursive(a, c, f, p, compteur = compteur + 1)
    return dich_recursive(c, b, f, p, compteur = compteur + 1)

# Affichage graphique
def dich_iterative_visuelle(a: float, b: float, f, p: float, pause:float = 0.01):
    import matplotlib.pyplot as plt
    from numpy import linspace # Fonction qui génère des nombres également espacés entre deux bornes spécifiées.
    
    compteur = 0
    
    plt.ion()  # visualistaion en direct
    fig, ax = plt.subplots(figsize=(8, 5))
    
    while not abs(a-b) < p:
        c = (a+b)/2
        
        # Tracer la fonction sur l'intervalle actuel
        x_vals = linspace(a, b, 400)
        y_vals = f(x_vals)
        ax.clear()
        ax.plot(x_vals, y_vals, 'b', label='f(x)')
        ax.axhline(0, color='black', linewidth=0.8)
        ax.set_title(f"Itération {compteur}, intervalle [{a:.5f}, {b:.5f}]")
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)

        # Tracer le milieu
        ax.plot(c, f(c), 'ro', label='milieu')
        plt.pause(pause)

        # Colorier la zone conservée
        if f(c) * f(a) <= 0:
            ax.axvspan(a, c, color='green', alpha=0.3)
            b = c
        else:
            ax.axvspan(c, b, color='green', alpha=0.3)
            a = c
        
        plt.pause(pause)
        
        compteur += 1
        
    return (a+b)/2, compteur

def verif_valeur(a: float, b: float, f, p: float, f_a_executer):
    # Vérification des entrées
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "a et b doivent être des réels"
    assert callable(f), "f doit être une fonction prenant un float et retournant un float"
    assert isinstance(p, (int, float)) and p > 0, f"p doit être un réel strictement positif, p={p}"
    assert f(a) * f(b) <= 0, f"f({a})*f({b}) n'est pas négatif"

    # Exécution de la fonction
    return f_a_executer(a, b, f, p)   

for i in range(-1, -10, -1):
    x_r, c_r = verif_valeur(-1, 1, f, 10**i, dich_recursive)
    print(f"precision = {10**i}  récursif :  x = {x_r},  itérations = {c_r} \n")
    
c, compteur = verif_valeur(-1, 1, f, 10**(-5), dich_iterative_visuelle)
