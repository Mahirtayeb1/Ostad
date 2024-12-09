s = ["l", "e", "t", "t", "e", "r"]
lst = []

for i in s:
    if i not in lst:
        lst.append(i)
    else:
        print("Printing all the twice appeared letters: ", i)

# for i in s:
#     if i in lst:
#         print(i)
#     else:
#         lst.append(i)