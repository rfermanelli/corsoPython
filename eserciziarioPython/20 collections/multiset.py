import collections
from collections import Counter

c = collections.Counter('The Lord of the rings')

print(c.most_common(4)) # i primi n elementi più comuni (n) (predefiniti: tutti)
print(c.most_common()[:-4-1:-1]) # i primi n elementi meno comuni (n) (predefiniti: tutti)
print(c.total()) # totale di tutti i conteggi (somma delle frequenza)
print(list(c)) # elenca gli elementi univoci
print(set(c)) # converte in un set
print(dict(c)) # converte in un dizionario normale
print(c.items()) # converte in un elenco di coppie (elemento, conteggio)
print(list(c.elements())) # restituisce un elenco [elem, …] con ripetizioni
print(+c) # rimuove i conteggi zero e negativi
print(c.clear()) # reimposta tutti i conteggi








