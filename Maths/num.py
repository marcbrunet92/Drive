def num(d, b):
    if d <= b-1:
        return [d]
    return num(d//b, b) + [d%b]

print(num(17,2))
