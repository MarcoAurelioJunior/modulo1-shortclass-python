from time import sleep

valor = float(input('Digite um valor qualquer: '))
desconto = valor - (valor * 15/100)

print('Descontando 15% desse valor...')
sleep(1)

print('Pronto! o novo valor é {}'.format(desconto))

