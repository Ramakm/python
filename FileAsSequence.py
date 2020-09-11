#Read a file with no of lines in it:

xfile = open("FileSystemprogram.txt", "r")
xfile.read(5)
print(xfile)
count =0
for choose in xfile:
    count = count + 1
print(count)

#File Exception handling program

try:
    hfile = open("mousa.txt","r")
    print("file exist")
except:
    print("file is not there")
finally:
    print("always print this line")

# use of len() method in file syatem:

flenfile = open("FileSystemprogram.txt", "r")
print(len(flenfile.read()))

#Searching through a file

fsearch = open("FileSystemprogram.txt", "r")
for flen in fsearch:
    flen = flen.rstrip()
    if flen.startswith("origin	ssh:"):
        print(flen)
    elif not flen.startswith("https:"):
        print(flen)

#take a file from input and

file = input("Enter your file name:")
file_open = open(file, "r")
count = 0
for line in file_open:
    count = count +1
    if line.startswith("https:"):
        print(line, "count the lines are:", count)


