def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n - 1)

# Esempio di test
print(fattoriale(5))  # 120
print(fattoriale(3))  # 6