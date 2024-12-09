# items = []
# items.append(1)
# items.append(3)
# items.append("gg")
# items.append([12, 15, 20])


# # for i, item in enumerate(items):
# #     print(i, item)

# lst = [100, 200, 300]
# items += lst    # items = items + lst
# print("after adding: ",items)

# li2 = [40, 50, 60]
# items.extend(li2)
# print("after extending: ", items)
# items.append(li2)
# print("after appending: ",items)

# for i, item in enumerate(items):
#     print(i, item, items[i])

list = [1,2,3,2,3,2,1,9,4,8]
uniq = []
dupli = []
for i in list:
    #print(i, list[i])
    if i not in dupli:
        uniq.append(i) 
    if i in uniq:  
        dupli.append(i)
print(uniq, dupli)