def swap_tuples(tuples):
    swapped = [(b,a) for a, b in tuples]
    return swapped

t = [(1,2), (4,5), (8,9), ("apple","orange"),("banana", 2)]
print(swap_tuples(t))