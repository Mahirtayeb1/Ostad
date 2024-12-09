# create a func that merge 2 dict into 1. If a key exists in both dict then the value from the 2nd dict will be used:

def merge_dict(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {"a" : 1, "b" : 2}
dict2 = {"a" : 4, "d" : 6}

print(merge_dict(dict1, dict2))