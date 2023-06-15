# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.
km = int(input('Digite a velocidade: '))
if km >= 80:
    print('Você ultrapassou o limite de 80KM/h!')
    ultra = km - 80
    m = ultra * 7
    print('Sua multa será no valor de {} reais.'.format(m))
else: 
    print('Obrigado por respeitar as normas do trânsito!')
print('===== FIM =====')
    
