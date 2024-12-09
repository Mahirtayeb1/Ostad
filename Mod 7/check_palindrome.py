n = int(input())
s = str(n)
# slice(start, stop, step)
#print(s[::-1])
#print(s[::])
if s[::] == s[::-1]:
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")