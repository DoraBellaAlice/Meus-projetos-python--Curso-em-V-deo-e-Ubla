# Aprovação-financiamento-casa

from sys import float_info

casa = float(input('Valor da casa R$ ' ))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos '.format(casa , anos), end='') # quebra de linha
print('a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')

