from time import sleep

print('='*30)
print('Encontrando o assassino')
print('='*30)

print('Se a resposta for afirmativa ganhará 1 ponto. OBS: Responda apenas [S/N]')

sleep(1)

perg1 = input('Mora perto da vítima? ').upper()
perg2 = input('Já trabalhou com a vítima? ').upper()
perg3 = input('Telefonou para a vítima? ').upper()
perg4 = input('Esteve no local do crime? ').upper()
perg5 = input('Devia para a vítima? ').upper()

c = 0

if perg1 == 'S':
    c = c + 1
if perg2 == 'S':
    c = c + 1
if perg3 == 'S':
    c = c + 1
if perg4 == 'S':
    c = c + 1
if perg5 == 'S':
    c = c + 1
    
if c == 5:
    print('Caso resolvido! encontramos o assassino...')
elif c == 4 or c == 3:
    print('Você é um dos cúmplices né?! Onde está o seu chefe?')
elif c == 2:
    print('Vamos investigar melhor sua fixa criminal... aguarde!')
elif c == 1 or c == 0: 
    print('Está liberado! não encontramos nada demais em você')
    


