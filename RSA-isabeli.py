# Desenvolvido por Isabeli Reik - fevereiro de 2022
# Trabalho da disciplina de GEX112 - Segurança e auditoria de sistemas 
# (Ciência da Computação - 9ª fase (Noturno - Remoto e Presencial) - 2021/2 - 2021/2

import random


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
# Um número perfeito de totiente é um número inteiro que é igual à soma de suas iterações de totiente. 
# Ou seja, aplica-se a função totiente para um número n, aplicá-lo de novo para o resultante da função 
# totiente, e assim por diante, até que o número 1 seja alcançado, e adicionar em conjunto a sequência 
# de números resultante; se a soma é igual a n, n é um número perfeito de totiente.

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


def gerarChavePrivada(e, totient_de_N):
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

    return n, e, totient_de_N

# estrutura do tipo dicionário para auxiliar na criptografia e descriptografia
def dicionario():
    meu_dicionario = {'a': 1, 'b': 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j":10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "x": 22, "z": 23}
    return meu_dicionario


def criptografa(usuarioArquivo, n, e):
    viuArquivo = 1
    dicionario2 = dicionario()
    usuarioArquivo2 = open(usuarioArquivo,'r')

    for char in usuarioArquivo2:
        mensagem = list(char.lower())
    
    for i in range(0, len(mensagem)):
        if mensagem[i] in dicionario2.keys():
            aux = (dicionario2[mensagem[i]] ** e)
            modulo = str(aux % n)

        if (viuArquivo == 1):
            with open ('teste2.txt', 'w') as arquivo:
                arquivo.write(modulo)
                arquivo.write(' ')
                viuArquivo = 0
                continue

        if (viuArquivo == 0):
            with open ('teste2.txt', 'a') as arquivo:
                arquivo.write(modulo)
                arquivo.write(' ')

    usuarioArquivo2.close()


def descriptografa(usuarioArquivo3, n, d):
    dicionario2 = dicionario()
    usuarioArquivo2 = open(usuarioArquivo3,'r')

    for char in usuarioArquivo2:
        aux = char.split(' ')
        lista = list(aux)
    
    lista.pop()
    lista2 = list(map(int, lista)) 

    lista3 = []
    for i in lista2:
        aux2 = i ** d % n 
        lista3.append(aux2)
    
    for i in range(0, len(lista3)):
        for chave, valor in dicionario2.items():
            if lista3[i] == valor:
                print(chave, end = " ")

    usuarioArquivo2.close()


continuar = True

while (continuar):

    print('#############################')
    print('# O que deseja fazer?       #')
    print('# 1 - Criar chave           #')
    print('# 2 - Cifrar mensagem       #')
    print('# 3 - Descifrar mensagem    #')
    print('# 4 - Sair                  #')
    print('#############################')

    message = int(input())
    print('Opção digitada: ', message)

    if(message == 1):

        print("Por favor digite dois números primos:")
        print('O primeiro número é...')
        primoA = int(input())
        print('O segundo número é...')
        primoB = int(input())

        if(verificaPrimo(primoA) == True and verificaPrimo(primoB) == True):

            n, e, totient_de_N = gerarChavePublica(primoA, primoB)
            print('A chave pública é:')
            print(n, e)

            d = gerarChavePrivada(e, totient_de_N)
            print('A chave privada é:')
            print(n, d)

    elif(message == 2):

        print('Digite o primeiro valor da chave pública:') #n
        usuarioChavePublica1 = int(input())

        print('Digite o segundo valor da chave pública:') #e
        usuarioChavePublica2 = int(input())

        if(int(n) == int(usuarioChavePublica1) and int(e) == int(usuarioChavePublica2)):
            print('Digite o nome do arquivo que deseja abrir e cifrar a mensagem:')
            usuarioArquivo = input()

            criptografa(usuarioArquivo, n, e)
        else:
            print('Chave pública informada está incorreta ou não existe!')
    
    elif(message == 3):
        print('Digite o primeiro valor da chave privada:') #n
        usuarioChavePrivada1 = int(input())

        print('Digite o segundo valor da chave privada:') #d
        usuarioChavePrivada2 = int(input())

        if(n == int(usuarioChavePrivada1) and d == int(usuarioChavePrivada2)):
            print('Digite o nome do arquivo que deseja abrir e decifrar a mensagem:')
            usuarioArquivo3 = input()

            descriptografa(usuarioArquivo3, n, d)
        else:
            print('Chave privada informada está incorreta ou não existe!')

    elif(message == 4):
        continuar = False