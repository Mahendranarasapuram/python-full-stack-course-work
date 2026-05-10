#Normal function
def wish(name):
    return f'hello {name},Welcom to python'

#Lambda Function
wish1=lambda name:f'hello {name},Welcome to python'
print(wish1("mahe"))
print(wish("raj"))
#2..Adding two numbers
output=lambda a,b,c:(a+b+c)/3
print(output(10,40,5))

#3.even or odd
iseven=lambda n:"True"if n%2==0 else "False"
print(iseven(18))

#finding the greatest number
greatest=lambda a,b: "Greater number is a"if a>b else "Smaller"
print(greatest(5,4))

#finging the greatest number among three numbers
f1=lambda a,b,c:a if (a>b and a>c) else (b if b>c  else c)
print(f1(10,25,45))

#squares of a number
square=lambda x:x*x
print(square(20))

#Multiply the two number using lambda functions
mul=lambda a,b: a*b
print(mul(2,4))

#Sort the list of tuples by second elements 
tuples_list=[(1,3),(2,1),(4,2)]
sorted_list2=sorted(tuples_list,key=lambda y:y[0])
sorted_list=sorted(tuples_list,key=lambda x:x[1])
print(sorted_list)
print(sorted_list2)
#finding the even number using filter()
numbers=[1,2,3,4,5,6]
even_numbers=list(filter(lambda x:x%2==0, numbers))
print(even_numbers)
#finding the squares of numbers using map()
number=[1,2,3]
square_num=list(map(lambda x:x**2,number))
print(square_num)

#Coverting list of strins to upper case
list=["abhi","vijay"]
upper_case=list(map(lambda x:x.upper(),list))
print(upper_case)

