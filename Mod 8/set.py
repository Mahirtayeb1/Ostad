# create a function that takes 2 sets and return their common value

def set_common(set1, set2):
    return set1.intersection(set2)

set1 = {1,2,3}
set2 = {3,5,6}
print(set_common(set1, set2))