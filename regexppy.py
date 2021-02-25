# Regular Expressions --- module --- only for strings type
# Match
# Search
# Sub

s = 'parallelogram'
#in, not in
'llel' in s
si = s.index('llel')
se = s.index('llel') + len('llel')
print(si, se)
import re

s = 'Hey, this is a string'
#match(pattern , string) --- check only in the begining
pattern = 'hey'
x = re.match(pattern, s , re.I)# Ignorecase
print(x)
pattern = 'hello'
st = 'this Hello is a string. hello is another example.'
print(re.search(pattern, st , re.I))

st = 'hello, world'
pattern = 'x'
print(re.sub(pattern, '#' , st))


#st = input()
# Dynamic patterns --- use Metacharacters
# period sign - ( . ) ---- any single char can come in its place except \n
# choice ( | )
#pattern =  'gr(a|e)y'
pattern = 'gr(a|e|i|o|u)y'
st = 'this string is groy in color'
print(re.search(pattern, st))

# ^ (beg)
# $ (end)
st = 'An Amazing module!'
#pattern = '^An'
pattern = 'ule[.]$'
print(re.search(pattern, st))

# Repeat Metachars
# * ---- it can come either 0 time or any no. of times
# + ---- can come 1 or any no. times
# ? ---- can come 0 or 1 time
# {min,max}
st = 'this string is in brown colouuuur'
pattern = 'colo(u){1,3}r'
print(re.search(pattern , st))

# Character Classes ----- no metachar holds its functionality inside character class
# ^ ---- to invert a class , but only in the begining
pattern = '[A-Z]'
pattern = '[a-z]'
pattern = '[0-9]'
pattern = '[A-Za-z0-9]'
pattern = '[p-y]'
pattern = '[FRAHJKLOP]'
pattern = '[AEIOUHY]'
pattern = '[^$#.%&^+?*}{]'
st = 'hsdgfkjshdgfkshgdfksghdfkRsdf0'
st = '$#.%&^+?*}{a'
print(re.search(pattern, st))

# Symbols
# \w --->  [A-Za-z0-9]
# \W ---> [0-9]
# \d ---> digits
# \s ---> special chars
# \S ---> white space
# sample09@email.com
email = '\w{8,12}@{1}(gmail|yahoo|rediff|email)(?=.com)'# follows # raw string
print(re.findall(email, 'rediff12@email.com'))