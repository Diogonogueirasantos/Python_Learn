from time import sleep
import sqlite3
from getpass import getpass
from datetime import datetime

db = sqlite3.connect('db_examples/bank_records.db')
cursor = db.cursor()


Mensagem = '''
    Olá, Agradecemos por confiar em nossos serviços!
    A seguir selecione um de nossos seviços
    
    [1] Novo Usuario
    [2] Login

'''

print(Mensagem)

def novo_usuario():
    print('É um prazer em ter você conosco... ')
    sleep(2)
    print('A seguir pedimos que você informe o seu nome e forneça uma senha')
    sleep(1)
    nome = str(input('Qual é o seu nome: ')).strip()
    sleep(2)
    print(f'Ótimo {nome}, por medidas de segura ao fornecer sua senha a mesma não será mostrada, \n'
          f'logo tenha total ciência ao fornece-la')
    senha = getpass(prompt='Forneça a sua senha: ')
    confirmar_senha = getpass(prompt='Confirme a sua senha: ')
    sleep(2)
    if senha != confirmar_senha:
        print('Ops... Parece que as senhas não se coincidem!')
        novo_usuario()
    elif senha == confirmar_senha:
        cursor.execute(
            "INSERT INTO usuario (nome, senha) VALUES (?, ?);",
            (nome, senha)
        )
        db.commit()
        print('Usuário cadastrado com sucesso!')
        login()


def login():
    id_uso = int(input('Forneça seu id de usuário: '))
    sleep(2)
    senha = getpass(prompt=f'Forneça a sua senha: ')
    cursor.execute(
        "SELECT Nome FROM usuario where id_usuario=? AND senha=?;",
        (id_uso, senha)
    )
    query = cursor.fetchone()

    if query:
        for records in query:
            print(f'Seja muito bem vindo: {records}')
            menu()
    else:
        print('Infelizmente não foi possível encontrar o usuário! Tente novamente.')
        login()


def menu():
    print('''A seguir selecione um dos serviços a baixo
            [1] Depositar
            [2] Sacar
            [3] Checar Saldo
             ''')
    servicos = int(input('Por favor selecione uma das opção acima: '))
    match servicos:
        case 1:
            depositos()
        case 2:
            saques()
        case 3:
            saldo()

def depositos():
    valor = float(input('Por favor insira o valor a ser depositado R$: '))
    sleep(2)
    deposito_data = datetime.now()
    conta = int(input('Informe o ID da sua conta: '))
    sleep(1)
    usuario = int(input('Informe o ID de usuário: '))
    sleep(3)
    cursor.execute(
        "INSERT INTO depositos (valor, data, id_usuario, id_conta) VALUES (?, ?, ?, ?); ",
        (valor, deposito_data, usuario, conta)
    )

    cursor.execute(
        """
        INSERT INTO conta (id_conta, saldo, id_usuario) VALUES (?, ?, ?) 
        ON CONFLICT(id_usuario) DO UPDATE SET saldo=saldo + ?, id_conta=?;
        """,
        (conta, valor, usuario, valor, conta)
    )
    db.commit()
    sleep(1)
    print(f'O deposito no valor de R$:{valor} foi Realizado!')


def saques():
    print('3')

def saldo():
    print('4')




selecao = int(input('Por favor selecione uma das opções acima: '))

match  selecao:
    case 1:
        novo_usuario()
    case 2:
        login()



