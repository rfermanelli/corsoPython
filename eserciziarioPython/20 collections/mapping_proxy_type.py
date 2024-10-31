from types import MappingProxyType

d_dinamico = {0: 'zero', 1: 'uno', 2: 'due'}
d_vista_d_dinamico = MappingProxyType(d_dinamico)

print(d_vista_d_dinamico)
print(d_vista_d_dinamico[0])

d_dinamico[0] = 'zero_a_zero'
print(d_vista_d_dinamico)
d_vista_d_dinamico[0] = 'zero'
