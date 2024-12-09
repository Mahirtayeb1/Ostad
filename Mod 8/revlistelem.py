# ['abc', 'hello'] output ['cba', 'olleh']

str_list = ['abc', 'hello']
revlist = []

for str in str_list:
    print(str)
    revlist.append(str[::-1])
print(revlist)

'''The code will produce an error because strings in Python are immutable, 
meaning you cannot modify them in place. The reverse() method is used for lists, 
not strings, and does not work directly on strings.'''

def revstrings(strlst):
    revlst = []
    for str in strlst:
        revlst.append(str[::-1])
    return revlst
print(revstrings(str_list))

def reversestrings(strlst):
    revlst = [str[::-1] for str in strlst]
    return revlst

print(reversestrings(str_list))