lista = []
print('Digite 15 números inteiros e positivos: ')
x = 0
for i in range (0, 15):
    n = int(input('Digite um número:[ %s ]:' %x))
    lista.append(n)
    x += 1 
print()

print('Vetor:',(lista), end = ' ')
print()

import random
indice_a = random.choice(lista)
print('Indice a: {}'.format(indice_a))

indice_b = random.choice(lista)
print('Indice b: {}'.format(indice_b))
print()

i = int(input('Digite o indice inicial: '))
f = int(input('Digite o indice final: '))
for d in range(i, f+1):
    r = d % 2 
    if r != 0:
        print(d, end =' ')
        
