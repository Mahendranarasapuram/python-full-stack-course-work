# code for glocery store application

product=['Rice','wheat','sugar','Milk','Eggs(12 pcs)','Cooking oil','Tea Powder','salt','Bread',
    'Soap']
price=[60,30,40,20,70,80,110,35,45,65]
print("------Welcome  to glocery store-------")
print("Here are the available products:\n")
print(f'Index'.ljust(6,' '),'product'.ljust(15,' '),'price'.ljust(6,' '))
for i in range (10):
    print(str(i+1).ljust(6,' '),product[i].ljust(15,' '),str(price[i]).ljust(6,' '))
items=list(map(int,input("Enter the indexes:  ").split()))
print("Seleted Items:")
print('----------- You Bill--------------')
total_amount=0
for item in items:
    print(product[item-1],price[item-1])
    total_amount+=price[item-1]
print("Total Amount to pay  :" , total_amount)
print('Thank you for shopping in our store!! ')


    
    

 