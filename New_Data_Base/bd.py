import exception as ex

data_base = {
        'GABRIEL' : ['123123', 'natal'],
        'VITOR' : ['321321', 'natal'],
        'RUAN' : ['123456', 'natal']
        }

def Clear():
    print('\n'*20)

def SignIn():
    print("==== SIGN IN ====")
    user = input('Nome: ').upper()
    if user != "" and user.upper() in list(data_base.keys()):
        password = input('Password: ')
        if password == data_base[user][0]:
            Interface(user)
        else:
            print('Invalid Password or User')


def Details(resp):
    # Transformando as chaves do dicionario em lista
    Clear()
    chaves = sorted(list(data_base.keys()))
    print(f'Name: {chaves[resp-1]}')
    print(f'Password: {data_base.get(chaves[resp-1])[0]}')
    print(f'Location: {data_base.get(chaves[resp-1])[1]}\n')
    print('Type 0 to return to the query')
    resp = input('> ')
    Consult() if resp == '0' else print('Invalid Comand'); Details(resp)
        

def Consult():
    Clear()
    chaves = sorted(list(data_base.keys()))
    print("="*21)
    print("======= USERS =======")
    print("="*21)
    print("0 - Back to the Menu")
    for i in range(len(data_base)):
        print(f'{i+1} - {chaves[i]}')
    print("\nEnter user position for more details")
    resp = int(input('> '))
    if resp == 0:
        Interface()
    else:
        Details(resp)

def SignUp():
    new_user = input('New User: ').upper()
    if new_user != "" and new_user.upper() not in list(data_base.keys()):
        new_password = input('Password: ')
        if len(new_password) >= 6:
            new_password2 = input('Repeat Password: ')
            if new_password == new_password2:
                new_location = input('Location: ')
                new_dict = {new_user: [new_password, new_location]}
                data_base.update(new_dict)
                Clear()
                resp = input("Register new user (y/n) ? ")
                if resp == 'y':
                    SignUp()
                else:
                    Interface()
            else:
                Clear()
                ex.passwordException2()
                SignUp()
        else:
            Clear()
            ex.passwordException()
            SignUp()
    else:
        Clear()
        ex.userExeption()
        SignUp()

def choice(c):
    if c == '1':
        SignUp()
    elif c == '2':
        SignIn()
    elif c == '3':
        Consult()
    elif c == '0':
        ex.Finish()
    else:
        print("Invalid Choice")

def Interface(user=' '):
    Clear()
    if user == ' ':
        print("==== WELCOME TO THE DATA BASE ====")
    elif user in data_base.keys():
        user = format(', ' + '\033[92m' + user + '\033[0m')
        print(f"==== WELCOME TO THE DATA BASE{user} ====")
    print('\nUser Options: ')
    print('1 - Sign up')
    print('2 - Sign In')
    print('3 - Consult')
    print('0 - Finish\n')
    c = input('> ')
    Clear()
    choice(c)

Interface()

