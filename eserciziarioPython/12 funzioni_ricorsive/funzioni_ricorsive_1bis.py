def somma(n):
    if n <=1:
        return n
    else:
        return n+ somma(n-1)

print(somma(10))
