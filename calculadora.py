print('Calculadora')
print('=' * 40)
print('Qual a sua escolha de hoje?')
print('Escolha um item abaixo:')
print('1 para somar')
print('2 para subtrair')
print('3 para múltiplicar')
print('4 para dividir')
print('5 para potência')
print('=' *40)
opcao = int(input('Digite a opção desejada: '))
n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))

if opcao == 1:
    soma = n1 + n2
    print('A soma de {} mais {} é igual a {}'.format(n1, n2, soma))

elif opcao == 2:
    subtr = n1 - n2
    print('O número {} menos {} é igual a {}'.format(n1, n2, subtr))

elif opcao == 3:
    mul = n1 * n2
    print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, mul))

elif opcao == 4:
    if n2 == 0:
        print('Não é possível dividir por zero')
    else:
        div = n1 / n2
        print('A divisão entre {} e {} é igual a {}'.format(n1 , n2 , div))

elif opcao == 5:
    poten = n1 **  n2
    print('A potência de  {} elevado a  {} é igual a {}'.format(n1, n2, poten))

else:
    print('opção inválida')








