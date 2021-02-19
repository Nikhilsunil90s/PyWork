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
