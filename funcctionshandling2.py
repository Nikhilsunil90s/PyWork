# Closures
# Nested Functions
# return

# def myfunc(arg):
#     def levelOne():
#         def levelTwo():
#             print(arg)
#         return levelTwo
#     return levelOne


# # l1 = myfunc(23)
# # print(type(l1))
# # l2 = l1()
# # l2()
# myfunc(100)()()

# # Decorators ---- a function that takes a function object as argument and returns a function object as value, must have only 1 level of closure
# # Middlewares ---- a block of code which executes between a request and a response ---- As decorators


# def funcT(arg):
#     print('Starting FuncT...')
#     def closure():
#         print('*'*50)
#         arg() # fobj()
#         print('*'*50)
#     return closure

# @funcT
# def fobj():
#     print("Hello, World!".center(50))

# #funcT(fobj)()


# fobj() # funcT(fobj)

# def divideBy50(ufObj):
#     def closure(a,b):
#         a //= 50
#         b //= 50
#         ufObj(a,b)
#     return closure

# @divideBy50
# def userFunc(x,y):
#     print(x ** y)

# userFunc(900,400)

def replacer(fObj):
    def closure(i,j):
        i = i.translate(''.maketrans('aeiouAEIOU' , '@3!0$@3!0$'))
        j = j.translate(''.maketrans('aeiouAEIOU' , '@3!0$@3!0$'))
        print(fObj(i,j))
    return closure


@replacer
def func(a,b):
    return a.swapcase() + b.swapcase()

func('Hello' , 'Rediff')
func('Astring' , 'aString')


print(type(func))


# Generators --- functions which do not return but yield a value
# Should not give any print statement
def myfun(arg):
    for i in range(arg):
        yield i

print(myfun(5))
#print(list(myfun(4500)))
#for i in myfun('AnyValue'):
#    print(i)
print(list(myfun(6)))

def myrange(beg, end , steps = 1):
    while beg <= end:
        yield beg
        beg += steps


print(list(myrange(1,33)))
for i in myrange(1,5):
    print(i)

# Sorted() ---- to sort a homogenous list and returns a list
li = ['apple' , 'red' , 'orange' , 'hue' , 'pink' , 'purple' , 'bi' , 'un' , 'years' , 'delight']
#li.sort()
def funcObj(arg):
    return len(arg)

print(sorted(li, key=funcObj))

li = [66,33,11,99,88,77,43,55,12,32,89,56]
print(sorted(li, key = lambda arg : arg % 7))

print(__name__) # name of module for interpretor







