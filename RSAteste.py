# Desenvolvido por Isabeli Reik - fevereiro de 2022
# Trabalho da disciplina de GEX112 - Segurança e auditoria de sistemas 
# (Ciência da Computação - 9ª fase (Noturno - Remoto e Presencial) - 2021/2 - 2021/2

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

# Calcula o totiente do numero primo
def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False

def mdc(n1,n2):
    rest = 1
    while(n2 != 0):
        rest = n1%n2
        n1 = n2
        n2 = rest
    return n1

# Gera um numero aleatório E, sasfazendo as condições
def generate_E(num): 
    while True:
        e = random.randrange(0,num) #or. é 2
        if(mdc(num,e) == 1):
            return e

# Função modular entre dois números
def mod(a,b):
    if(a < b):
        return a
    else:
        c = a % b
        return c

def gerarChavePrivada(primoA, primoB):
    y = totient(primoA) # compute the totient of primoA
    x = totient(primoB) # compute the totient of primoB
    totient_de_N = x * y # compute the totient of N
    e = generate_E(totient_de_N) # generate E

    d = 0
    while(mod(d * e, totient_de_N) != 1):
        d += 1
    return d

def verificaPrimo(primo):
    if(prime(primo) == True):
        print('É primo!')
        return True
    else:
        print('Não é primo!')
        return False

def gerarChavePublica(primoA, primoB):
    n = primoA * primoB 
    y = totient(primoA) # compute the totient of primoA
    x = totient(primoB) # compute the totient of primoB
    totient_de_N = x * y # compute the totient of N
    e = generate_E(totient_de_N) # generate E

    return (n, e)


if(message == 1):
    print("Por favor digite dois números primos:")
    print('O primeiro número é...')
    primoA = int(input())
    print('O segundo número é...')
    primoB = int(input())

    if(verificaPrimo(primoA) == True and verificaPrimo(primoB) == True):

        chavePrivada = gerarChavePrivada(primoA, primoB)
        print('A chave privada é:')
        print(chavePrivada)

        chavePublica = gerarChavePublica(primoA, primoB)
        print('A chave pública é:')
        print(chavePublica)
