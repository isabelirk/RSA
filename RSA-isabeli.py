import math

from sympy import Q

print('#############################')
print('# O que deseja fazer?       #')
print('# 1 - Criar chave           #')
print('# 2 - Cifrar mensagem       #')
print('# 3 - Descifrar mensagem    #')
print('#############################')

message = int(input('Digite a mensagem a ser criptografaga: '))

p = 11
q = 7
e = 3

n = p * q

def encrypt(me):
    en = math.pow(me, e)
    c = en % n
    print('Encriptando a mensagem: ', c)
    return c

print ('Mensagem original: ', message)
c = encrypt(message)