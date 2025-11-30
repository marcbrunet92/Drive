def f(x:float) -> float:
    return x**3+x

def dich_recursive(a:float, b:float, f, p:float) -> float:
    if p <= 0:
        raise ValueError(f"la valeur de p : {p} doit être strictement positive")
    if f(a)*f(b) > 0:
        raise ValueError(f"f({a})*f({b}) n'est pas négatif")
    c = (a+b)/2
    if abs(a-b)<p:
        return c
    if f(c)-f(a)<=0:
        return dich(a, c, f, p)
    return dich(c, b, f, p)
