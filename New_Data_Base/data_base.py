banco_de_dados = {}

c = 0

def Clear():
    print(30 * '\n')

def Consultar():
    Clear()
    print("=== BANCO DE DADOS ===")
    # Ordenando a Lista
    dictList = list(sorted(banco_de_dados))
    # Usuarios Cadastrados
    for i in range(len(dictList)):
        print(f'{i+1} - {dictList[i]}')
    n = int(input("Digite o número correspondente ao usuário: "))
    n -= 1
    if n < len(dictList):
        usuario = str(dictList[n])
        GetUser(usuario)
    else:
        print("Digite um número válido")

def GetUser(usuario):
    Clear()
    print(f"Usuário: {usuario}")
    print(f"Idade: {banco_de_dados[usuario]['idade']}")
    print(f"Altura: {banco_de_dados[usuario]['altura']}")
    # print(banco_de_dados.get(usuario))
    c = input("Digite 9 para voltar: ")
    if c == '9':
        Interface()

def Cadastrar(c):
    while c == "1":
        z = input("Cadastrar Novo Cliente (s/n)? ")
        if z == "s":
            # Criando uma lista para armazenar atributos
            usuario = []

            # Ler o nome do cliente
            nome = input("Nome: ")
            usuario.append(nome)
            # Ler o idade do cliente
            senha = int(input("Senha: "))
            usuario.append(senha)
            # Ler altura
            altura = float(input("altura: "))
            usuario.append(altura)

            for i in range(len(usuario)):
                construtor = {usuario[0]: {'Senha': usuario[1], 'altura': usuario[2]}}
                # Adicionar usuario ao banco
                banco_de_dados.update(construtor)

        else:
            c = []
            Interface()

def Drawer(c):
    if c == '1':
        Cadastrar(c)
    elif c == '2':
        Consultar()
    elif c == '9':
        Interface()
    elif c == '0':
        Clear()
        print('Fim do Banco de Dados')


def Interface():
    Clear()
    print("="*35)
    print("=== BEM-VINDO AO BANCO DE DADOS ===")
    print("="*35)
    print("\nEscolha uma opção abaixo:\n")
    print("1 - Cadastrar Usuário")
    print("2 - Consultar Usuário")
    print("0 - Sair\n")
    c = input(">>> ")
    Clear()
    Drawer(c)

Interface()