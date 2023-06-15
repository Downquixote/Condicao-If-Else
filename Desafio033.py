# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < b and c < a: 
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b: 
    maior = c

print('O menor número digitado foi: {}'.format(menor))
print('O maior número digitado foi: {}'.format(maior))
