s = ["l", "e", "t", "t", "e", "r"]
lst = []
count = 0
for i in s:
    if i in lst:
        count+=1
        #print(i)
        if count > 1:
            break
        else:
            print(i)
    else:
        lst.append(i)

def appearce_twice_first(s):
    lst = []
    count = 0
    for i in s:
        if i in lst:
            count+=1
            if count > 1:
                break
            else:
                return i
        else:
            lst.append(i)

g = ["g", "u", "a", "r", "a", "n", "t", "e", "e"]
print(appearce_twice_first(g))
