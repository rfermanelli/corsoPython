def somma(n):
    if n == 1:
        return 1
    else:
        return n + somma(n - 1)

# Esempio di test
print(somma(5))  # 15
print(somma(10))  # 55