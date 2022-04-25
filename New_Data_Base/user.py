from bd import data_base
import exception as ex

print(data_base)

def Clear():
    print('\n' * 30)

def choice(c):
    if c == '1':
        Add()
    elif c == '2':
        Remove()
    elif c == '3':
        Consult()
    elif c == '0':
        ex.Finish()
    else:
        print("Invalid Choice")

def UserInterface(user):
    Clear()
    print(f"==== WELCOME TO THE DATA BASE{user} ====")
    print('\nUser Options: ')
    print('1 - Sign up')
    print('2 - Sign In')
    print('3 - Consult')
    print('0 - Finish\n')
    c = input('> ')
    Clear()
    choice(c)