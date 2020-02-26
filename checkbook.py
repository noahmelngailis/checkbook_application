user_name = 'Codeup'

def welcome_user():
    """This function will walk the user 
    through the the initialization of the application"""
    print('For this application')
    print('Username: Codeup')
    print('Password: P@ssw0rd')
    import time as t
    t.sleep(2)

initialize = welcome_user()
    
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
    create_menu()
    return f"Welcome to Online Usury Bank {user_name}"
    
def create_menu():
    open_file()
    file_contents = open_file()
    clean_data()
    list_file = clean_data()
    """this function will hold the main menu for each of the options"""
    print('What action would you like to take?')
    print('1) View Current Balance')
    print('2) Make a deposit')
    print('3) Make a withdrawal')
    print('4) Exit')
    action = input('What can we do for you today? ')
    if action == '1':
        account_balance()
    elif action == '2':
        make_deposit()
    elif action == '3':
        make_withdrawl()
    elif action == '4':
        print('Type to start application')
        return
    else:
        print(f'{action} is not an option...')
        action = input('What can we do for you today? ')

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
list_file = clean_data()

def account_balance(x = list_file):
    total = sum(x)
    print("Your balance is: " + str(total))
    import time as t
    t.sleep(1)
    create_menu()


account_total = account_balance()

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

def make_withdrawl():
    """this function takes in a positive number and sends the negative
    to the transactions.txt file"""
    transaction = input('What would you like to withdrawl?  ')
    while (type(transaction) == 'str'
    or transaction.isdigit() == False 
    or int(transaction) < 0):
        print(f"You cannot deposit {transaction} ")
        transaction = input('What would you like to withdrawl?  ')
    new_trans = int(transaction)* -1
    with open ('transactions.txt', 'a') as f:
        f.write(str(new_trans) + '\n')
    print(f"You successfully withdrew ${transaction}")
    print(f"Thank you!")
    open_file()
    file_contents = open_file()
    clean_data()
    list_file = clean_data()
    print(list_file)
    import time as t
    t.sleep(2)
    create_menu()

    