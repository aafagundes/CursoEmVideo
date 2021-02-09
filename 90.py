#dicionarios
aluno=dict()
aluno['nome']=str(input('digite o nome:'))
aluno['media']= float(input(f'a media de {aluno["nome"]} :'))
if aluno['media'] >= 6:
    aluno['situacao']= 'aprovado'
elif aluno['media']<6:
    aluno['situacao']='reprovado'
print('>>>>'*25)
for c,v in aluno.items():
    print(f'- {c} é igual a {v}')
print('>>>>'*25)
