idade = int(input('Qual a sua idade: '))
salario = float(input('Qual o seu salário: '))
sexo = input('Qual o seu sexo: ').upper()

if idade >= 150 or idade <= 0:
    print('ERROR: Idade invalida!')
if salario <= 0:
    print('ERROR: Sálario invalido!')
if sexo != 'M' and sexo != 'F' and sexo != 'OUTRO' :
    print('ERROR: Sexo invalido!')

    


