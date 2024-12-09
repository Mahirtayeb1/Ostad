"""  Problem Statement
Write a program where user will give an array of elements. You will have to print the sum of elements where each element will be less than median element.

Input
The input consists of size of the array and the elements of the array. Every input will be unsigned integer number.

Output
The output will be sum of elements that are lesser than median element.

Constraints
0 ≤ |S| ≤ 109
Example:
Enter size of the array and the elements.
Input:
6
30 10 5 40 60 15
Output:
30                 """


# n = int(input())
# lst = []
# for i in range(n):
#     g = int(input())
#     lst.append(g)
# print(lst)
# lst.sort()
# print(lst)
# q = sum(lst)/n
# #print(len(lst))
# #g = sorted(lst)
# #print(g)
# # print(lst[n//2])
# # print(lst[(n//2)+1])
# if n % 2 == 1:
#     sum = 0  
#     for i in range(0, n//2 + 1):   # 0 1 2 3 4 5 
#         #print(lst[i])
#         if lst[i]<q:
#             sum+=lst[i]
#         else:
#             continue
#     print(sum)
# else: 
#     sm = 0 
#     for i in range(0, n//2):
#         #print(lst[i])
#         if lst[i]<q:
#             sm+=lst[i]
#         else:
#             continue
#     print(sm)


# for i in range(4):
#     print(i)

# # Step 1: Input the size of the array and the elements
n = int(input("Enter the size of the array: "))
lst = list(map(int, input("Enter the elements of the array: ").split()))

lst.sort()
q = sum(lst)/n
if n % 2 == 1:
    sum = 0  
    for i in range(0, n//2 + 1):   # 0 1 2 3 4 5 
        #print(lst[i])
        if lst[i]<q:
            sum+=lst[i]
        else:
            continue
    print(sum)
else: 
    sm = 0 
    for i in range(0, n//2):
        #print(lst[i])
        if lst[i]<q:
            sm+=lst[i]
        else:
            continue
    print(sm)

# if n % 2 == 1:
#     sum = 0  
#     for i in range(0, n//2 + 1):   # 0 1 2 3 4 5 
#         #print(lst[i])
#         sum+=lst[i]
#     print(sum)
# else: 
#     sm = 0 
#     for i in range(0, n//2):
#         #print(lst[i])
#         sm+=lst[i]
#     print(sm)


