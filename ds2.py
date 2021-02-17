# list , tuple, set, dict
# list comprehensions
# dict comprehensions
l = [x for x in range(5)]
d = {x:x**2 for x in range(5)}
print(d)
# copies
t = (9,8,7,6)
dt = t
l1 = [1,2,3,4,5]
l2 = ['red' , 'blue' , 'green' , 'pink' , 'grey']
d = {}
len(l1) == len(l2)
for i in range(len(l1)):
    d.setdefault(l1[i],l2[i])
print(d)
print(type(zip(l1,l2)))
print(dict(zip(l1,l2)))

#Packing/Unpacking
l = [1,2,3,4,5] # Packing of a list
t = (1,2,3,4,5) # Packing of a tuple
s = {11,22,33,44} # packing of a set
d = { 1: 100, 2 : 200 } # Packing of a dict object

# Unpack
# Way One ---->
l = [100,200,300]
a,b,c = l
print(a,b,c)
print(l)
t = (90,80)
x,y = t[0],t[1]
x,y = t
#z = 
s = {11,44,22,55}
i,j,k,l = s
print(i,j,k,l)
# Way Two ---> use *(pack/unpack) 
l = ['a' , 'bbbb' , 'ccccccc']
print(*l)
t = (88,55,22)
print(*t)
s = {100,33,22}
print(*s)

# d = { 1: 100, 2 : 200 } # Packing of a dict object
# p1,p2 = d
# print(p1,p2)

# print()
# type(12)
# len([])
# max()
#print()

#def myfunc(arg,arg1,arg2,arg3):
    #body

def myprint(*arg): # * performs packing here
    print(arg)

myprint()
myprint(1,2,3,4,5,6,7)
myprint('hello,' , 'hey,', "bye,", "8.9","77")
myprint(1)
    