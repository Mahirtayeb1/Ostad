def get_even_nums(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0 and num!=0 ]  # Printing even nums without 0s
    return even_numbers 
    
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_nums(list1))

s = {1, 1, 2, 3, 4} #Set
print(s)