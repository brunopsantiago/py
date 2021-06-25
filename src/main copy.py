

peso = float(input('Escreva seu peso:\n '))
altura = float(input('Escreva sua altura:\n '))

imc = peso / altura ** 2

if imc < 29:
    print('Seu peso {0} e sua altura {1} resulta no imc %.2f' .format(
        peso, altura) % imc)
    print('Parabens, vc esta otimo')
elif imc < 35:
    print('Cuidado gordao')
