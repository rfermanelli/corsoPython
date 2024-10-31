# Input: il testo da cifrare e il passo di cifratura
testo = input("Messaggio da cifrare: ")
passo = input('Passo della cifratura (è un intero compreso tra 1 e 25: ')
#
while not passo.isdigit() or int(passo) not in range(1, 26):
    passo = input('Passo della cifratura (è un intero compreso tra 1 e 25: ')
#
testo_cifrato = ''
for carattere_da_cifrare in testo:
    if carattere_da_cifrare.isdigit():
        codice_ascii = ord(carattere_da_cifrare)
    if carattere_da_cifrare == ' ':
        codice_ascii = ord(carattere_da_cifrare)
    if carattere_da_cifrare.islower():
        codice_ascii = ord(carattere_da_cifrare) + int(passo)
        if codice_ascii > ord('z'):
            codice_ascii = ord('a') - 1 + codice_ascii - ord('z')
    if carattere_da_cifrare.isupper():
        codice_ascii = ord(carattere_da_cifrare) + int(passo)
        if codice_ascii > ord('Z'):
            codice_ascii = ord('A') - 1 + codice_ascii - ord('Z')
    testo_cifrato = testo_cifrato + chr(codice_ascii)
#
print(testo_cifrato)


