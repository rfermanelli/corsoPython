def lunghezza_stringa(s):
    if s == '':
        return 0
    else:
        return 1 + lunghezza_stringa(s[1:])

# Esempio di test
print(lunghezza_stringa("ciao"))  # 4
print(lunghezza_stringa("Python"))  # 6