"""
Dato un numero in input espresso in notazione decimale
convertirlo in notazione binaria.
"""

def decimale_binario(numero_decimale):
    if numero_decimale > 0:
        numero_binario = []
        quoziente = numero_decimale
        while numero_decimale // 2 != 0:
            cifra_binaria = numero_decimale % 2
            numero_binario.append(cifra_binaria)
            numero_decimale = numero_decimale // 2
        numero_binario.append(numero_decimale % 2)
        numero_binario.reverse()
        return numero_binario
    else:
        return

print(decimale_binario(100))

