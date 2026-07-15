Peso = float(input('Qual é o seu peso? (KG) '))
Altura = float(input('Qual a sua altura? (m) '))
imc = Peso / (Altura ** 2)
print('O IMC, dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif  18.5 <= imc < 25:
    print('Parabéns ,Você está na faixa de peso normal')
elif 25 <= imc  < 30:
    print('Você está sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
elif imc >= 40:
    print('Você está em obesidade Mórmida, Cuidado!')


