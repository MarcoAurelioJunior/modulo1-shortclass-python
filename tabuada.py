from time import sleep

print('=' * 40)
print('Tabuada personalizada')
print('=' * 40)
sleep(1)

num = int(input('Escolha um número para gerar sua tabuada: '))
num2 = int(input('Esscolha um número para gerar o tamanho da tabuada: '))
for i in range(1, num2 + 1):
  print('{} x {} = {}'.format(num, i, num * i))
