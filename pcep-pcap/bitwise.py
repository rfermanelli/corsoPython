decimale_1 = 10
decimale_2 = 2
bitwise = []

shift_a_sinistra = decimale_1 << 1
bitwise.append(shift_a_sinistra)
shift_a_destra = decimale_1 >> 1
bitwise.append(shift_a_destra)
and_bit_a_bit = decimale_1 & decimale_2
bitwise.append(and_bit_a_bit)
or_bit_a_bit = decimale_1 | decimale_2
bitwise.append(or_bit_a_bit)
or_esclusivo = decimale_1 ^ decimale_2
bitwise.append(or_esclusivo)
invertitore_di_bit = ~ decimale_1
bitwise.append(invertitore_di_bit)

print(bitwise)
