# Média do Aluno

nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
média = (nota1 + nota2) / 2
print('Tirando {:.2f} e {:.1f} a média do aluno é {:.1f}'.format(nota1 , nota2 , média))
#if média >= 5 and média < 7:
if 7 > média >= 5:
    print('O aluno está em recuperação.')
elif média < 5:
    print('O aluno está Reprovado')
elif média >= 7:
    print('O aluno está Aprovado!')

