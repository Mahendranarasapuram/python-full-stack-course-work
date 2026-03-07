########Condition Statements####
# checking the min and max balance#
min_balance=5000
cur_balance=2000
if cur_balance<min_balance:
    print('Send message and cut the amount')
##Checking the batery percentage
min_charge=20
cur_charge=15
if cur_charge<min_charge:
    print('send alert message to charge the phone')
##checking the user login details
data=('user@gmail',123)
mail=input('Enter email:')
password=int(input('Enter password:'))
if data== mail and password:
    print('Login Successful')
else:
    print('Invalid login')
##checking the gloceries is there or not
fruits=['mango,apples,papaya']
search_item=input('Search here :')
if search_item in fruits:
    print(f"{search_item} found! Buy Now")
else:
    print(f'{search_item} is out of stock, we will notify you once is available')
#checking the bus available buses 
time=int(input('Enter the hours'))
print("Available Buses are:")
if 0<=time <=6:
    print("Bus2\nBus7\n")
elif 7<=time <=12:
    print("Bus1\nBus19\n")
elif 13<=time <=18:
    print("Bus9\nBus80")
else:
    print("Enterr the time in giving range") 
## uber booking system 
print("welcome to Uber ,Book the raid")
print("1.Bike")
print("2.Auto")
print("3.Car")
choice=int(input("choose the option:"))
if choice ==1:
    print("Hey, you have booked the Bike Taxi successfully\n Driver is on the way. wear the helmet")
elif choice==2:
    print("Hello you have booked Auto successfully\n Driver is on the way , Keep tracking for your safety")
else :
    print("Helllo you booked car successfully\n")


