items = []
items.append(1)
items.append(2.5)
items.append(" Mahir Faisal")
items.append([1, 50, 7, 11])

print(items)

for item in items:
    print(item, type(item))

for i in range(0, len(items)):
    print(i, items[i])

#using enumerate function

for i, item in enumerate(items):
    print(i, item)
    
emptylst = []

for i in range(1, 6):
    print(f'adding {i} element in the empty list')
    emptylst.append(i)
for element in emptylst:
    print(f'elements of the emptylst was: {element}')

# using while loop
i = 0
lst = []
while(i<6):
    print(f"At the top of i is {i}")
    lst.append(i)
    i+=1
    print(f"list now: {lst}")
    print(f"At the bottom i is {i}")

print(f"the numbers are: ")

for elements in lst:
    print(elements)


# def reverse_string(strings):
#  reversed_strings = [s[::1] for s in strings]
#  return reversed_strings


# str_list_1 = ["Hello", "Python", "Django"]
# print(reverse_string(str_list_1))