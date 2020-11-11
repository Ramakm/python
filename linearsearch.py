def linears(li,x):
    # count = 0
    for i in range(0,len(li)):
        if li[i] ==x:
            return i
    return -1

li = [20,36,54,6,32]
x = 6
result = linears(li,x)
if result == -1:
    print("The value is not present inside the list")
else:
    print("the value is present there in the list", result)