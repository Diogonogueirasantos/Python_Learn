from collections import namedtuple

registros = namedtuple('Usuario', ['Nome', 'Idade'])

sesson = 1

while sesson == 1:

    nome = str(input('Digite o nome do usuário: ')).strip()
    idade = int(input('Digite a sua idade: '))

    registros(nome, idade)

    print(f'O cadastro foi efetivado com sucesso! \n O usuário:{registros.Nome} e idade:{registros.Idade} já constam no banco de dados!')

    cadastro = str(input('Deseja  registrar outro usuário [S/N]: ')).strip().upper()
    if cadastro == 'S':
        sesson = 1
    elif cadastro == 'N':
        sesson = 0


print('Muito obrigado por utilizar nossos serviços!')