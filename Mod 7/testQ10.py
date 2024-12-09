# def is_palindrome(s):
#     if s == s[::-1]:
#         print(f"{s} is a palindrome")
#     else:
#         print(f"{s} is not a palindrome")

# def show_palindromic_substrings(s):
#     n = len(s)
#     palindromic_substrings = set()

# s = input()
# # print(s[::-1])
# # print(s[0::])
# is_palindrome(s)
"""Question:"""

"""Create a program that checks if a given string is a palindrome. Also, print all the palindrome substrings of that string. 

A palindrome string is a string that is the same in forward or backward. Example: "madam".
A substring is a part of a string. Example: for a string "abc", substrings are: "a", "ab", "bc".


Input String:
Take a string as input.


Check for Palindrome:
Write a function is_palindrome(s) that checks if a given string s is a palindrome.

Find All Palindromic Substrings:
Write a function show_palindromic_substrings(s) that prints all substrings that are palindrome in the given string."""

def is_palindrome(s):
    return s == s[::-1]

def show_palindromic_substrings(s):   
    n = len(s)
    palindromic_substrings = set()  # using set() to avoid duplicates

    # generate all substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromic_substrings.add(substring)
                
    # Print all unique palindromic substrings
    for substring in palindromic_substrings:
        print(substring)


input_s = input("Enter a string: ")

if is_palindrome(input_s):
    print(f"{input_s} is a palindrome")
else:
    print(f"{input_s} is not a palindrome")

print("Palindromic substrings:")
show_palindromic_substrings(input_s)