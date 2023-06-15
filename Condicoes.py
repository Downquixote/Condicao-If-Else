nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2
print('Sua média foi: {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média está boa! PARÁBENS!!!')
else: 
    print('Sua média está ruim, melhore!')
print('Obrigado por utilizar nossos serviços.')