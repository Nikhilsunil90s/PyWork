# Dictionaries
# Array Like Object --- but unindexed, Mutable
# C R U D
# Create
ed = {}
# keys (left) ---- must be uniqe, only from immutable type --- int, float, bool, str, tuple
# values (right) --- can repeat, can b from mutable types
d = {
    'a' : 100,
    1 : 300,
    2.2 : [1,2,3,4,5,6,7],
    False: "Hello, World",
    (11,22): "This is a tuple",
    1: 900,
    1: 1900,
    True: 2900,
}
print(d)
# Create a dict
print(dict(a=100,b=200,c=300))
#dict()

# Read --- use keys
print(d['a'] , d[True], d[(11,22)])

# Update
d['a'] = 'Apple'
print(d)

# delete
del d[1]
print(d)

# Membership Operations --- only on keys
print(2.2 in d)
print('Apple' in d)

# Iterable --- only on keys
for i in d:
    print(i)

# Operations via functions/Methods
#type()
print(len(d))
# dict()
#print(dict([1,2,3,4,5,6,7]))

d = {
    'a' : 100,
    1 : 300,
    2.2 : [1,2,3,4,5,6,7],
    False: "Hello, World",
    (11,22): "This is a tuple",
    1: 900,
    1: 1900,
    True: 2900,
}

copyd = d.copy()# shallow copy
copyd['a'] = 'A'
print(copyd)
print(d)

deepd = d # deep copy
deepd['a'] = 'AAAAAAAA'
print(deepd)
print(d)

#d.clear()
#print(d)

print(d.get('a'))

d.setdefault('mykey' , 'myvalue') # to add a new key value pair in dict
print(d)

d1 = {1 : 100, 2 : 200, 3 : 300}
d2 = {2 : 400, 5 : 500}
d1.update(d2)
print(d1)

print(d1.pop(3))
print(d1)
print(d1.popitem())
print(d1)

print(d1.keys())
print(d1.values())
print(d1.items())

d1 = {1 : 100, 2 : 200, 3 : 300}
d2 = {3 : 300, 1 : 100, 2 : [ 200 , 300, 400, ]}
print(d1 == d2)
newd = dict.fromkeys(d1 , "Default")
print(newd)











