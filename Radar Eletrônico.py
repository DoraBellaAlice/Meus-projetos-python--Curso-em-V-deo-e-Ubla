# Radar Eletrônico

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é o de 80km/h ')
    multa = (velocidade - 80) * 7
print('Tenha um bom dia! Dirija com segurança!')