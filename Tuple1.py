# name = dict()
# name["Ram"] = 45
# name["Hari"] = 95
#
# for (k,v) in name.items():
#     print(k,v)
#
# tups = name.items()
# print(tups)
#
#
# #Sorting List of tuples:
#
# d = {"m": 85, "N":96, "Q":75}
# li = d.items()
# tu = sorted(li)
# print(tu)
#
# for r,s in tu:
#     print(r,s)


#Sorting tuples using value from dict:
#
# c = {"nam":56, "mak":748, "kksjl":542}
# l1 = list()
# for k,v in c.items():
#     l1.append((v,k))
# print(l1)
#

#10Most common used words from a txt file:
fhand = open("FileSystemprogram.txt")
count1 = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count1[word] = count1[word].get(word,0)+1
# lis =list()
# for k,v in count1.items():
#     newtup = (v,k)
#     lis.append(newtup)
#
# lis = sorted(lis, reverse= True)
#
# for value, key in lis[:10]:
#     print(key, value)

print(sorted([(v,k) for k,v in count1.items()]))