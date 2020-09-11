# number = 7
# user_play = input("Type Y if you esnt to Play:").lower()
# if user_play == 'y':
#     user_number = int(input("Enter your no:"))
#     if user_number == number:
#         print(("Your no is matching"))
#     else:
#         print("not matching")
# # else:
#     print("game Over")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    evens.append(number)
    for num in evens:
        if num % 2 == 0:
            print()
print(evens)

