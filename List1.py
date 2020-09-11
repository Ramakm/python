# x = [50,30,60,40,20,50,40,40]
# for y in x:
#     print ("The marking apperances are :", y)
# print("Binga!")
#
# print( range(5) )
#
# friends =["ram", "Shyam","jadu","atharb"]
# for i in range (len(friends)):
#     friend = friends[i]
#     print(friend)
# #List Concatination: duplicate values also gets concatinate
#
# l1 = [2,45,12,56,14]
# l2 = [65,96,54,621,66,12]
# l3 = l1 +l2
# print(l3)
#
# # List Sliced (upto but not including)
#
# print(l1[1:4])
# print((l2[:5]))
# print(l3[:])
# l3.sort()
# print(l3)
# l4 = l3.extend(52)
# print(l4)
#
# stuff = list()
# stuff.append("book")
# stuff.append(69)
# print(stuff)`

#
Book = ["Gaha", "Bishnu", "Ramakrushna","Rama", "Hari"]
Book.sort()
print(Book)

numlist = list()
while True:
    inp = input("Enter a number:")
    if inp == "Done":
        break
    value = float (inp)
    numlist.append(value)

Average = sum(numlist)/len(numlist)
print("Average:", Average)

abc = "Rama is a good Bouy"
bcd = abc.split()
print(bcd)
for w in bcd:
    print(w)


abc2 = "Rama:is:a:good:Bouy"
abc1 = abc2.split(":")
print(abc1)

