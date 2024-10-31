def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Esempio di test
print(fibonacci(6))  # 8
print(fibonacci(10))  # 55