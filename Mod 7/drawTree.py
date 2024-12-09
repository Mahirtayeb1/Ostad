#         *              1
#        ***             3
#       *****            5
#      *******           7
#     *********          9
#    ***********        11
#         *
#
#
# height = 6
# 6x2 = 12-1 = 11
#
# def tree(height):
#     length = height * 2 - 1
#     stars = 1
#     for i in range(1, height + 1):
#         print(("*" * stars).center(length))
#         stars += 2
#     print("*".center(length))

# tree(6)

def is_palindrome(s):
    return s == s[::-1]

def show_palindromic_substrings(s):   
    n = len(s)
    palindromic_substrings = set()  
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromic_substrings.add(substring)

    for substring in palindromic_substrings:
        print(substring)


input_s = input("Enter a string: ")

if is_palindrome(input_s):
    print(f"{input_s} is a palindrome")
else:
    print(f"{input_s} is not a palindrome")

print("Palindromic substrings:")
show_palindromic_substrings(input_s)
