class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def userExeption():
    print(bcolors.FAIL + "User already registered or invalid!" + bcolors.RESET)

def passwordException():
    print(bcolors.FAIL + "Invalid password. Password must be longer than 5 characters!" + bcolors.RESET)

def passwordException2():
     print(bcolors.FAIL + "Invalid password. The passwords must be the same!" + bcolors.RESET)

def Finish():
    print(bcolors.OK + 'End of program' + bcolors.RESET)