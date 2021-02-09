#dicionarios
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
programa=dict()

programa['nome']=str(input('digite o nome:'))
nasc=int(input('digite o ano de nascimento:'))
programa['idade']= datetime.now().year - nasc
programa['carteira']=int(input('digite o numero da carteira de trabalho: (ou 0 para nao tem)'))
if programa['carteira'] !=0:
    programa['contratacao']=int(input('digite o ano de inicio de contratacao:'))
    programa['salario']=float(input('digite o salario'))
    programa['aposentadoria']=programa['idade'] + (programa['contratacao'] +35 - datetime.now().year)

print('-='*30)

for c,v in programa.items():
    print(f'   * {c} tem o valor {v}')