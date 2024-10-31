def inversione_stringa(s):
    if s == '':
        return ''
    else:
        return s[-1] + inversione_stringa(s[:-1])

print(inversione_stringa('python'))
