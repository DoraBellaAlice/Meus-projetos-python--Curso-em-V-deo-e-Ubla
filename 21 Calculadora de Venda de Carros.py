Valor_pago = float (input('Valor pago: '))
Valor_investido = float(input('Valor investido '))
Valor_venda = float(input('Valor da venda: '))
Custo_total = Valor_pago + Valor_investido
Lucro = Valor_venda - Custo_total
print('Custo total: R$ ' + str(Custo_total))
print('Lucro obtido: R$ ' + str(Lucro))

if Lucro > 0:
    print('Resultado: Lucro na venda!')
elif Lucro < 0:
    print('Resultado: Prejuizo na venda!')
else:
    print('Resultado: Empate! ')