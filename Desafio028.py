# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

print("Bem-vindo(a) ao Brando's Prize Draw!")

user = int(input('Digite um número entre 0 e 5, para saber se venceu ou perdeu: '))  
r = randint(0, 5)
if user == r:
    print('UAU, Você venceu! PARÁBENS!!')
else: 
    print('Poxa, que pena... Você perdeu. Mas não desista!')
print('O número selecionado foi: {}'.format(r))