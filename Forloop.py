Friends = ["Ram","Shyam","Jadu"]

for friend in Friends:
    print(f"{friend} is my friend.")
    print(friend)


grades = [50,20,30,85,96,45]
amount = len(grades)
aveg = sum(grades) / amount

# print no of iterator and with smallest number:

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

# Count no of element with print no sidewise
count = 0
for i in [20,30,50,24]:
    count = count + 1
    print(count, i)

# take a list as input and print the largest number from that
list1 = int(input("Enter numbers of elements:"))
num =[]
for i in range (0,list1):
    ele = int(input())
    num.append(ele)
    # print(num)
print("larget element is:", max(num))


print("program End!")

count1 = 0

for i2 in [20,24,12,52,54]:
    count1 = count1 + i2
    print(count1, i2)
print("After",count1)

