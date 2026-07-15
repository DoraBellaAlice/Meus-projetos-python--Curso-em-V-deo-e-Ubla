# Jogo de Advinhar o número

from  random import randint
from time import sleep
computador = randint (0 , 10)
print('=' * 40)
print('Estava pensando em um número de 0 ao 10. Tente adivinhar.')
print('=' * 40)
jogador = int(input('Em que número pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você me venceu.')
else:
    print('Ganhei! Estava pensando no número {} e não no número {}'.format(computador, jogador))