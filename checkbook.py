user_name = 'Codeup'

def welcome_user():
    """This function will walk the user 
    through the the initialization of the application"""
    print('For this application')
    print('Username: Codeup')
    print('Password: P@ssw0rd')
    import time as t
    t.sleep(3)

    print('Welcome to Online Usury Bank!!')
    user_name = input('Please enter a user name: ')
    if user_name != 'Codeup':
        print('Try again dummy')
        user_name == 'Codeup'
        user_name = input('Please enter a username: ')
    password = input('Please enter a password:')
    if password != 'P@ssw0rd':
        print('Try again dummy')
        password = 'P@ssw0rd'
        password = input('Please enter a password:')
    print('Authenticating')
    t.sleep(1)
    print('.')
    t.sleep(1)
    print('.')
    t.sleep(1)
    print('.')
    t.sleep(2)
    return f"Welcome to Online Usury Bank {user_name}"
    
def create_menu():
    """this function will hold the main menu for each of the options"""
    print('What action would you like to take?')
    print('1) View Current Balance')
    print('2) Make a deposit')
    print('3) Make a withdrawal')
    print('4) Exit')
    action = input(f'What can we do for you today, {user_name}? ')
    if action == 1:
        current_balance()
    if action == 2:


def build_text_file():
    with open ('transactions.txt') as f:
        file_contents = f.read()

def write_text_file(item):
    with open ('transactions.txt', 'a') as f:
        f.write(item + '\n')

def open_file():
    with open ('transactions.txt') as f:
        file_contents = f.readlines()
        return file_contents
file_contents = open_file()

# def clean_data(x = file_contents):
#     clean_file = file_contents.replace('\n',",")[:-1]
#     string_file = list(clean_file.split(','))
#     list_file = [int(s) for s in string_file]
#     return list_file
# list_file = clean_data() 

def clean_data(x = file_contents):
    list_file = [int(f.replace('\n',"")) for f in file_contents]
    return list_file

def account_balance():
    total = sum(list_file)
    return "Your balance is: " + str(total)
    import time as t
    t.sleep(2)
    create_menu()

def make_deposit():
    transaction = input('What would you like to deposit?  ')
    while (type(transaction) == 'str'
    or transaction.isdigit() == False 
    or int(transaction) < 0):
        print(f"You cannot deposit {transaction} ")
        transaction = input('What would you like to deposit?  ')
    with open ('transactions.txt', 'a') as f:
        f.write(transaction + '\n')
    print(f"You successfully deposited ${transaction}")
    print(f"Thank you!")
    import time as t
    t.sleep(2)
    create_menu()

    def make_withdrawal():
    """this function takes in a positive number and sends the negative
    to the transactions.txt file"""
    transaction = input('What would you like to withdrawal?  ')
    while (type(deposit) == 'str'
    or transaction.isdigit() == False 
    or int(transaction) > 0):
        print(f"You cannot deposit {transaction} ")
        transaction = input('What would you like to withdrawal?  ')
    with open ('transactions.txt', 'a') as f:
        f.write(-transaction + '\n')
    print(f"You successfully deposited ${transaction}")
    print(f"Thank you!")
    import time as t
    t.sleep(2)
    create_menu()

