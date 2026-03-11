bullets=10
while bullets>0:
    print(f'{bullets} are left ,you can shoot!!')
    bullets-=1
else:
    print("Game over")


#candy crush game code
moves=32
winning_points=24
while moves >0:
    if moves==winning_points:
        print("you win the game")
        break
    print(f'{moves} moves are left, you can play!!')
    moves-=1
else:
    print("game over")
#Student attendace code
data={}
n=int(input("Enter no of student :"))
for i in range (n):
           name=input("Enter student name:")
           data[name]=False
print(data)
for name in data:
    print(name)
    status=int(input(f"Enter the {name} status (0-Absent),1-Present):"))
    data[name]=bool(status)
print(data)
