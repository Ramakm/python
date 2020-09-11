file = dict()
file["Name"] = "Ram"
file["Age"] = 5
print(file)

import collections


number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))

total_revenue = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)
f = {}
print(f)

counts = dict()
count =0
names = {"ram", "Shyam", "Hari", "ram","hari"}
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] =  counts[name] +1
print(counts)
