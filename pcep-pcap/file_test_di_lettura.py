import os

#miofile = open('pswfeltrinelli.txt', 'r')
#miofile = open('C:\\Users\\r.fermanelli\\Python\\corsoPython\\pswfeltrinelli.txt', 'r')

miofile = open('..\\pswfeltrinelli.txt', 'r', encoding='UTF-8')

lines = miofile.readlines()
print(lines)
miofile.close()
print(' ')

for line in open('..\\pswfeltrinelli.txt', 'r', encoding='UTF-8'):
    print((line.rstrip()).lstrip())






#print(type(line))

#print(package_B())
#print(package_B(miofile))

