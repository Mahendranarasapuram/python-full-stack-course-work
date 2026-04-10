def add_sum(a,b):
    return a+b
def sub_num(a,b):
    return a-b
def div_num(a,b):
    return a/b
def mul_num(a,b):
    return a*b
def mod_num(a,b):
    return a%b

exp=input("")
if '+' in exp:
    a,b=exp.split('+')
elif '-' in exp:
    a,b=exp.split('-')
elif '/'in exp:
    a,b=exp.split('/')
elif '*'in exp:
    a,b=exp.split('*')
elif '%' in exp:
    a,b=exp.split('%')
    
    
    