# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM.
# E R$ 0,45 para viagens mais longas.
print('Quantos KM será a viagem?')
km = float(input())
if km <= 200: 
    pass1 = km * 0.50
    print('Sua viagem custará: {:.2f} reais.'.format(pass1))
else: 
    pass2 = km * 0.45
    print('Sua viagem custará {:.2f} reais.'.format(pass2))

print('===== FIM =====')