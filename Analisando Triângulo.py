r1 = float(input('Primeiro Seguimento '))
r2 = float(input('Segundo Seguimento '))
r3 = float(input('Terceiro Seguimento '))
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
    print('OS SEGUIMENTOS ACIMA PODEM FORMAR UM TRIÂNGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 !=r3 != r1:
                print('ESCALENO')
    else:
            print('ISÓSCELES')
else:
        print('OS SEGUIMENTOS ACIMA NÃO PODEM FORMAR UM TRIÂNGULO')
