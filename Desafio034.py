# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais o aumento é de 15%.
s = float(input('Digite o valor do salário: '))
base = 1250.00
if s > base:
    aumento10 = s * 10 / 100
    newsalario10 = aumento10 + s
    print('Você ganhou um aumento de 10%. que é equivalente a R$ {:.2f}'.format(aumento10))
    print('Seu salário agora está no valor de R$ {:.2f}'.format(newsalario10))
else: 
    aumento15 = s * 15 / 100 
    newsalario15 = aumento15 + s
    print('Você ganhou um aumento de 15%. Que é equivalente a R$ {:.2f}'.format(aumento15))
    print('Seu salário agora está no valor de R$ {:.2f}'.format(newsalario15))