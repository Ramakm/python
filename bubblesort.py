# def bs(a):  # a = name of list
#     b = len(a) - 1  # minus 1 because we always compare 2 adjacent values
#
#     for x in range(b):
#         for y in range(b - x):
#             if a[y] > a[y + 1]:
#                 a[y], a[y + 1] = a[y + 1], a[y]
#     return a
#
#
# a = list(map(int, input().split()))
# bs(a)
# print(a)

a=input("enter sequence:"+ "")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("Not a Palindrome")