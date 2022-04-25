'''#while True:
data_base = {
    'GABRIEL' : ['123123', 'natal'],
    'VITOR' : ['VitorSenha', 'Barra Do Rio'],
    'RUAN' : ['senhaRuan', 'Campina Grande']
    }

def title(logged=False, user=''):
    if logged == False:
        print("==== WELCOME TO THE DATA BASE ====")
    elif logged == True:
        user = format(f' {user} ')
        print(f"==== WELCOME TO THE DATA BASE{user}====")

def SignIn():
    print("==== SIGN IN ====")
    user = input('Nome: ').upper()
    if user != "" and user.upper() in list(data_base.keys()):
        password = input('Password: ')
        if password == data_base[user][0]:
            Interface(True, user)
        else:
            print('Invalid Password or User')

def Interface(user=''):
    print("="*35)
    title(False, '') if user == '' else title(True, user)
    print("="*35)

Interface()'''

name = 'gabriel'

print(f"{'-' * 30}")