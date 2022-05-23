lista = []   #Criei uma lista para armazenar os números 
print('Digite 15 números inteiros e positivos: ')
x = 0
for i in range (0, 15):   #Utilizei o for para rodar a quantidade de vezes que é informada
    n = int(input('Digite um número:[ %s ]:' %x))   #O usuário irá digitar 15 números,esse código irá rodar as 15 vezes também,pedindo o valor
    lista.append(n)    #Adicionei os valor indicado pelo usuário em uma lista 
    x += 1 
print()

print('Vetor:',(lista), end = ' ')  #Imprimi a lista com os valores indicados 
print()

import random   #Importei o random 
indice_a = random.choice(lista)   #E chamei a função choice,assim será selecionado dois valores aleatórios a partir da lista
print('Indice a: {}'.format(indice_a))   #O print irá imprimir o valor do indice 

indice_b = random.choice(lista)    #Utilizei o choice novamente para selecionar o segundo indice 
print('Indice b: {}'.format(indice_b))
print()

i = int(input('Digite o indice inicial: '))  #O usuário irá informar o primeiro indice que foi imprimido 
f = int(input('Digite o indice final: '))  #E o indice final também
for d in range(i, f+1):  #Utilizei o for para rodar a quantidade de vezes necessárias,a partir do valor das variáveis indicadas pelo usuário
    r = d % 2   
    if r != 0:    #Encontrara apenas os valores ímpares dentre os dois índices 
        print(d, end =' ')   #Por fim,irá imprimir os valores que são ímpares entre os índices 
        
