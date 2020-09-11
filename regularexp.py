# file = open("FileSystemprogram.txt")
# for line in file:
#     line = line.rstrip()
#     if line.find("From:") >0:
#         print(line)
#
#
#
# # Using re
# file = open("FileSystemprogram.txt")
# for line in file:
#     line = line.rstrip()
#     # if re.search("https:", line):
# #         print(line)
#
# file = open("FileSystemprogram.txt")
# for line in file:
#     line = line.rstrip()
#     if line.startswith("From"):
#         print(line)


data = "from: itsramakrushna@gmail.com mail to help you in python"

selct = data.find("@")
sp = data.find(" ", selct)
print(sp)

held = data[selct+1 : sp]
print(held)

host = " From: itsramakrushna@nbnco.am.ha.r  is the host file of the account"

part1 = host.find('@')
print(part1)

