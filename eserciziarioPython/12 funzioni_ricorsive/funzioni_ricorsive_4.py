def inversione_stringa(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + inversione_stringa(s[:-1])

# Esempio di test
print(inversione_stringa("ciao"))  # "oaic"
print(inversione_stringa("Python"))  # "nohtyP"