from module import fact
#simple function
def function():
    print("Hello World!!")

#function with argument
def function_arg(name):
    print(name)

#function with return statement
def function_return(name):
    return name

#function with multiple return statements
def function_mul_return():
    name = "GECG"
    depart = "Computer Engineering"
    return name,depart

#function with default arguments
def function_default(a=1,b=2):
    return a+b

#function with keyword arguments
def function_keyword(a,b):
    return a*b

#function with variable-length(non keyword) arguments
def function_varlength_non(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum

#function with variable-length(keyword) arguments
def function__varlength_key(**args):
    dis = {}
    for key, val in args.items():
        dis[key] = val
    return dis

#scope of variable
def function_scope():
    x = 10
    print("Value inside function:"
          "", x)


print('----------Simple Function----------')
function()

print('----------Function with Argument----------')
function_arg("Rutvik Jakhaniya")

print('----------Function with Return Statement----------')
print(function_return("Rutvik"))

print('----------Function with Multiple Return----------')
name,depart = function_mul_return()
print(f'College name: {name}')
print(f'Department: {depart}')

print('----------Function with Default Arguments----------')
print("function_default(10, 20) :", function_default(10, 20))
print("function_default() :", function_default())

print('----------Function with Keyword Arguments----------')
print("function_keyword(a=10, b=20) :", function_keyword(a=10, b=20))
print("function_keyword(b=10, a=20) :", function_keyword(b=10, a=20))

print("----------Function with Variable-length(Non Keyword) Arguments----------")
print("function_varlength_non(10, 20) : ", function_varlength_non(10,20))
print("function_varlength_non(10, 20, 30) : ", function_varlength_non(10,20,30))
print("function_varlength_non(10, 20, 30, 40) : ", function_varlength_non(10,20,30,40))

print("----------Function with Variable-length(Keyword) Arguments----------")
print('function__varlength_key(Name="Rutvik",Surname="Jakhaniya") :', function__varlength_key(Name="Rutvik",Surname="Jakhaniya"))
print('function__varlength_key(Name="Rutvik",Surname="Jakhaniya", College="GECG") :', function__varlength_key(Name="Rutvik",Surname="Jakhaniya", College="GECG"))

print('----------Scope of Variable----------')
x=20
function_scope()
print("value outside function:", x)

print('----------Module Function----------')
print(f'Factorial: {fact(5)}')
