import random

print('#############################')
print('# O que deseja fazer?       #')
print('# 1 - Criar chave           #')
print('# 2 - Cifrar mensagem       #')
print('# 3 - Descifrar mensagem    #')
print('#############################')

message = int(input())

print('Opção digitada: ', message)

# Verifica se um numero gerado é primo
def prime(n): 
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
            return False
        i+=6
    return True

def verificaPrimo(primo):
    if(prime(primo) == True):
        print('É primo!')
    else:
        print('Não é primo!')

#def gerarChavePublicaPrivada (primo):

if(message == 1):
    print("Por favor digite dois números primos:")
    primoA = int(input())
    primoB = int(input())

    verificaPrimo(primoA)
    verificaPrimo(primoB)
