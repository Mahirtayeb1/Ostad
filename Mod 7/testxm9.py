def reverse_string(strings):
 reversed_strings = [s[::1] for s in strings]
 return reversed_strings


str_list_1 = ["Hello", "Python", "Django"]
print(reverse_string(str_list_1))

def merge_dicts(dict1, dict2):
 merged = dict2.copy()
 merged.update(dict1)
 return merged


dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c': 4}
print(merge_dicts(dict1, dict2))

class Data:
 def __init__(self, id):
    self.id = id
    id = 10
data = Data(20)
print(data)