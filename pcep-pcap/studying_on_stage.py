#
if __name__ == '__main__':
    print('Eseguito come uno script')
else:
    print('Importato come un modulo')
# La classe come iteratore (o generatore)
import os


class Fibonacci:
    def __init__(self, indice_successione):
        self.__ultimo_indice = indice_successione
        self.__fib_elem_prec = 1
        self.__fib_elem_succ = 1
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice > self.__ultimo_indice:
            raise StopIteration
        if self.__indice in [0, 1]:
            self.__indice += 1
            return 1
        else:
            self.__ret = self.__fib_elem_prec + self.__fib_elem_succ
            self.__fib_elem_prec, self.__fib_elem_succ = self.__fib_elem_succ, self.__ret
            self.__indice += 1
            return self.__ret


print('La classe come iteratore: ')
for i in Fibonacci(7):
    print(i, end=' ')
print()
#
# La classe che instanzia la classe iterotore
class FibonacciIterator:
    def __init__(self, n):
        self.__iter = Fibonacci(n)
    def __iter__(self):
        return self.__iter

print('La classe che instanzia la classe iteratore: ')
fib = FibonacciIterator(16)
for i in fib:
    print(i, end=' ')
print()
#
# La parola chiave yield
# La funzione con return non è un generatore
def f(n):
    for i in range(n):
        return i

print(f(80))
# La funzione con yield è un generatore
print('La parola chiave yield come iteratore: ')
def f(n):
    for i in (map(lambda x: x**2, [x for x in range(n)])):
        yield i

print(f(8))
for i in f(5):
    print(i, end=' ')
print()
#
# Generatore delle prime n potenze di 2
def power_of_2(n):
    for pow in range(1,n + 1):
        yield 2**pow


for i in power_of_2(4):
    print(i, end=' ')
print()
#
# Generatori e list comprehension
print('Un iteratore in list comprehension: ')
l_c = [i for i in power_of_2(6)]
print(l_c)

# La funzione list() e l'iteratore
l_c = list(power_of_2(7))
print(l_c)
#
# L'operatore in
for i in range(20):
    if i in power_of_2(14):
        print(i, end=' ')
print()
#
# Un generatore dei primi n elementi della successione di Fibonacci con la parola chiave yield
def Fibonacci(n):
    prec = 1
    succ = 1
    elem = 0
    ind = 0
    for ind in range(n):
        if ind == 0 or ind == 1:
            elem = 1
            yield elem
        else:
            elem = prec + succ
            prec, succ = succ, elem
            yield elem


print('Fibonacci yield: ')
for i in Fibonacci(7):
    print(i, end=' ')
print()
#
# List comprehension ed espressione booleana
l_ist = []
for i in range(10):
    l_ist.append(0 if i % 2 == 0 else 1)
print('List comprehension ed espressioni booleane come operatori con le funzioni range(), map() e filter(): ')
print(l_ist)
l_ist =[0 if i % 2 == 0 else 1 for i in range(10)]
print(l_ist)
l_ist =[0 if i % 2 == 0 else 1 for i in map(lambda x: x**3, (0, 1, 2, 3, 4, 5, 6))]
print(l_ist)
l_ist =[0 if i % 2 == 0 else 1 for i in filter(lambda x: x**3 >8, (0, 1, 2, 3, 4, 5, 6))]
print(l_ist)
#
#
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

print('the_list è una lista: ', the_list)
for v in the_list:
    print(v, end=" ")
print()

print('the_generator è un iteratore: ', the_generator)
for v in the_generator:
    print(v, end=" ")
print()
#
# La funzione lambda
list_n_1 = [el for el in range(10)]
list_n_2 = [map(lambda c: c**2, list_n_1)]
print('La funzione lambda in una funzione map() come iteratore: ')
for g in map(lambda c: c**2, list_n_1):
    print(g, end=' * ')
print()
#
from random import seed, randint
seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print('La funzione filter(): ')
print(data)
print(filtered)
#
#
def outer(par):
    loc = par

    def inner():
        return loc, par
    return inner


var = 40
fun = outer(var)
print('La tecnica closures: ')
print(fun())
#
#
any_list = [1, 2, 3, 4]
even_list = list(map(lambda v: v | 1, any_list))
print(even_list)
#
#
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars)
print(stars("And Now for Something Completely Different"))
#
#
from os import strerror

try:
    stream = open('file_1.txt', 'r')
    line = stream.readline()
    print('La riga del file contiene:', line)
    stream.close()
except IOError as ioerr:
    print(strerror(ioerr.errno))
except Exception as exc:
    print("Cannot open the file:", exc)
#
#
stream_text_file = open('file_1.txt', 'rt')
contatore_caratteri_file = 0
carattere_file = stream_text_file.read(1)
print('Il file file.txt è:')
while carattere_file != '':
    print(carattere_file, end='')
    contatore_caratteri_file += 1
    carattere_file = stream_text_file.read(1)
stream_text_file.close()
print('Il file file.txt contiene', contatore_caratteri_file, 'caratteri')
print()
#
# il metodo readline() per leggere una riga alla volta fi un file
s = open('file_1.txt', 'rt')
line = s.readline()
while line:
    print(line)
    line = s.readline()
s.close()
#
# il metodo readlines() per leggere tutte le righe in una lista di stringhe
s = open('file_1.txt', 'rt')
line = s.readlines()
print(line)
s.close()
print()
#
# La funzione open() mappa un file a un oggetto iterabile
for file_line in open('file_1.txt', 'rt'):
    print(file_line, end='')
#
# Il metodo write()
stream = open('file_1.txt', 'a')
for i in range(5):
    linea = 'Linea n.:' + str(i) + '\n'
    stream.write(linea)
stream.close()
#
# la classe bytearray
data = bytearray(10)
for i in range(len(data)):
    data[i] = i
for i in data:
    print(hex(i), end=' ')
print()
#
data = bytearray(10)
for i in range(len(data)):
    data[i] = ord('a') + i
print('Scrittura di un file binario con un oggetto bytearray:')
print(data)
binary_file_stream = open('b_file.bin', 'wb')
binary_file_stream.write(data)
binary_file_stream.close()
#
from os import strerror
print('Lettura di un file binario in un oggetto bytearray:')
# modo n. 1: con il metodo readinto() dell'oggetto stream
binary_file_stream = open('b_file.bin', 'rb')
binary_file_stream.readinto(data)
binary_file_stream.close()
for b in data:
    print(hex(b), end= ' ')
print()
print(data)
# modo n. 2: con la funzione bytearray() applicata al metodo read() dell'oggetto stream
bf_s = open('b_file.bin', 'rb')
data = bytearray(bf_s.read())
bf_s.close()
print(data)
bf_s = open('b_file.bin', 'rb')
data = bytearray(bf_s.read(3))
bf_s.close()
print(data)
#
# copiare un file
"""
from os import strerror
import errno

source_file = input('Nome del file sorgente: ')

try:
    sbf_s = open(source_file, 'rb')
except IOError as sbf_s_error:
    print(strerror(sbf_s_error.errno))

destination_file = input('Nome del file destinazione: ')

try:
    sbf_d = open(destination_file, 'wb')
except IOError as sbf_d_error:
    print(strerror(sbf_d_error.errno))

buffer = bytearray(1000)
total = 0

try:
    readin = sbf_s.readinto(buffer)
    #while readin > 0:
    sbf_d.write(buffer[:readin])
    #    readin = sbf_s.readinto(buffer)
    sbf_s.close()
    sbf_d.close()
except IOError as copy_file_error:
    print(strerror(copy_file_error.errno))
"""
#
# Copia di un file bitmap in un oggetto di tipo bytearray
try:
    stream = open("download.png", "rb")
    image = bytearray(stream.read())
    stream.close()
except IOError:
    print("failed")
else:
    print("bitmap in bytearray success...")
#
# Lavorare col modulo os (Unix/Linux) platform (Windows)
import platform
print(platform.uname())
os.mkdir('../test')
os.makedirs('../testtest/testtesttest')
print(os.getcwd())
os.rmdir('../test')
os.removedirs('../testtest/testtesttest')
os.chdir('../')
print(os.getcwd())
print(os.listdir())
#
# Lavorare con la data e l'ora
print('Lavorare con il tempo (la data e l\'ora):')
import datetime
data = datetime.date.today()
mia_data = datetime.date(2020, 12, 3)
print(mia_data)
iso_data = datetime.date.fromisoformat('2019-11-02')
print(iso_data)
iso_data = iso_data.replace(year=2023, month=7, day=16)
print(iso_data)
print(iso_data.weekday())
print(iso_data.isoweekday())
l = [iso_data.weekday(), iso_data.isoweekday()]
print(l)

# Lavorare con il tempo (Timestamp)
print('Lavorare con il tempo (Timestamp):')
import time
sec = time.time()
print(sec)
tempo = datetime.time(9,4, 3)
print(tempo)
print(tempo.microsecond)
time_stamp = 12345555
print(time.ctime(time_stamp))
print(time.ctime())
#
tm_zona = time.struct_time.tm_zone
print(tm_zona)
