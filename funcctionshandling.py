# Functions --- group of statement(s) ---- block
# Function --- Lifecylce ---> 1. Define, 2. Invoke/Call
x = 90
# def funcName():
#     for i in range(5):
#         print("Hello, World")



# print(type(funcName)) # function is an object in python, from class 'function'
# x = 90
# s = 'string'
# l = [1,2,3,4,5]

# funcName() # call operators

# # Arguments
# # 4 Types
# # 1. Required Positional Arguments
# # 2. Default Arguments
# # 3. Keyword Arguments --- only for Acutal Arguments
# def hello(x,y,z,a = 100): # Formal Arguments
#     print(x + y + z + a)


# hello(12,13,14) # Actual Arguments
# hello('hello' , 'hey' , 'hi' , 'ReplacedA')
# hello([1,2,3,4] , [100,200,300] , [9.9,8.8,7.7] , [900,800,700])
# hello(a = 100 , x = 900 , z = 400, y = 210)
# # Variable Arguments
# # use * ---- Pack/Unpack Operator
# l = [1,2,3,4,5,6]
# print(*l)
# # Dict Unpack ---- use **
# d = {'a' : 100, 'b' : 200 , 'c' : 300}
# #print(a=100, b = 200, c = 300)
# #print(**d) # Not possible , problem with Print

# def dynamicFunc(*args , **kwargs): # Packing
#     # for i in args:
#     #     print(i , end = ' ')
#     # print()
#     print(args , kwargs)

# dynamicFunc()
# dynamicFunc(900,800,700)
# dynamicFunc('hey' , 'apple' , True , 1,2,3,4,5,6,7,8,9,0)
# dynamicFunc(1.2,2.3,3.4,4.5,90,70, key1 = 100, key2 = 200 , randomKey = 500)
# # Required Args > Default args > *args > **kwargs
# def specialFunc(x,y,z = 90, *a, **kw):
#     print(x,y,z,a,kw)

# specialFunc(12,13,34,10,20,30)
###### Return Statement
# Exit from a function ---- and destroys the local scope of a function
def returninFunc(arg):
    print(f"Gonna Return Something ... {arg}")
    return arg * 34 , arg * 10, arg * 89 , arg * 78

val = returninFunc(45)
print(val)
returninFunc(90)
x = 90 # Global Scope

def addX():
    # Local Scope
    global x  # Declaration only, no definition
    x += 10 # from global scope of whole module
    y = 900 # Local scope of addX

print(x)
addX()
print(x)
###### NameSpace
list_ = [44,33,22,11,77,66,88,99]
# Normal Approach
# newl = []
# for i in list_:
#     newl.append(i // 5)
# print(newl)
def divBy5(arg):
    return arg // 5
newl = []
for i in list_:
    newl.append(divBy5(i))
print(newl)
print(x)


# Anonymous Functions / Lambda Functions
# Single Statement Functions , self returning functions (no return, no loops, no if else inside)
#def name(arg1, arg2, arg3):
#    return arg1*arg2*arg3

ref = lambda a,b,c: a*b*c # Lambda Function
print(ref(12,131,44))
print((lambda x,y : x ** y)(12,13))
print((lambda arg: arg.swapcase())('HelloSwapCase'))
list_ = [44,33,22,11,77,66,88,99]
alist = []
for i in list_:
    alist.append((lambda i : i // 5)(i))

print(alist)

# map(callableobject-func obj, list)
def mulBy100(arg):
    return arg * 100
print(list(map(mulBy100 , list_)))

lists_ = ['apple' , 'green' , 'hello' , 'grey' , 'hue' , 'hi' , 'purple' , 'orange' , 'great']
print(list(map(lambda arg : arg * 3 , lists_)))

# Filter(callable, list)
newl = []
for i in lists_:
    if len(i) <= 4:
        newl.append(i)
    else:
        continue
newl = []
def checkLen(arg):
    return len(arg) <= 4
# for i in lists_:
#     if checkLen(i):
#         newl.append()
#     else:
#         continue
for i in lists_:
    if (lambda arg : len(arg) <= 4)(i):
        newl.append(i)

print(newl)
print(list(filter(lambda arg : arg[0] == 'h' , lists_)))