#while True:

def title(logged=False, user=''):
    if logged == False:
        print("==== WELCOME TO THE DATA BASE ====")
    elif logged == True:
        user = format(f' {user} ')
        print(f"==== WELCOME TO THE DATA BASE{user}====")
        Interface(logged)

# Login
def SignIn():
    print("==== SIGN IN ====")
    user = input('Nome: ').upper()
    if user != "":
        password = input('Password: ')
        if password != '':
            title(True, user)
        else:
            print('Invalid Password or User')

def Interface(logged=False):
    print("="*35)
    title(logged)
    print("="*35)
    print('\nUser Options: ')
    print('1 - Sign up')
    print('2 - Sign In')
    print('3 - Consult')
    print('0 - Finish\n')
    SignIn()
    

Interface()