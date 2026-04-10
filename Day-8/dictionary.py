# ATM System
data = {
    '123456': {'pin': '1234', 'balance': 4000, 'history': []},
    '234567': {'pin': '2345', 'balance': 2000, 'history': []},
    '345678': {'pin': '4567', 'balance': 5000, 'history': []}
}

def deposit(acc_num):
    print('---------------------------------------------------')
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    print(f"{amount} is deposited successfully")
    data[acc_num]['history'].append(f"{amount} deposited")
    check_balance(acc_num)
    print('---------------------------------------------------')

def withdraw(acc_num):
    print('---------------------------------------------------')
    amount = int(input("Enter the amount you want to withdraw: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        print(f"{amount} is withdrawn successfully")
        data[acc_num]['history'].append(f"{amount} withdrawn")
        check_balance(acc_num)
    else:
        print("Insufficient balance")
    print('---------------------------------------------------')

def change_pin(acc_num):
    old_pin = input("Enter old PIN: ")
    if data[acc_num]['pin'] == old_pin:
        new_pin = input("Enter new PIN: ")
        data[acc_num]['pin'] = new_pin
        print("PIN changed successfully")
    else:
        print("Incorrect old PIN")

def check_balance(acc_num):
    print('---------------------------------------------------')
    print(f"Current Balance: {data[acc_num]['balance']}")
    print('---------------------------------------------------')

def view_transactions(acc_num):
    print('---------------------------------------------------')
    if data[acc_num]['history']:
        for i in data[acc_num]['history']:
            print(i)
        print("---------- End of transactions ----------")
    else:
        print("No Transactions")
    print('---------------------------------------------------')

def menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transactions")
    print("5. Change PIN")
    print("6. Exit")

# Main Program
print("\n-------- Welcome to ATM --------")
acc_num = input("Enter the account number: ")
pin = input("Enter your PIN: ")

if acc_num in data and data[acc_num]['pin'] == pin:
    print("Login Successful")

    while True:
        menu()
        ch = input("Enter your choice: ")

        if ch == '1':
            check_balance(acc_num)
        elif ch == '2':
            deposit(acc_num)
        elif ch == '3':
            withdraw(acc_num)
        elif ch == '4':
            view_transactions(acc_num)
        elif ch == '5':
            change_pin(acc_num)
        elif ch == '6':
            print("------------ Thank you ------------")
            break
        else:
            print("Invalid choice")

else:
    print("Invalid Login")