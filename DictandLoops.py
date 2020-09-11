count = dict()
print("Enter a line of text:")
line =  input('')
words = line.split()
print(words)
for word in words:
    count[word] = count.get(word,0)+1
print('count', count)

chulk = {"Ram": 100, "hari":65, "pj":47}
for key in chulk:
    print(key,chulk[key])

#retreiving Keys and values froma dict()

counts = {"Ram": 100, "hari":65, "pj":47}
print(counts.keys())
print(counts.values())
print(counts.items())
for a,b in counts.items():
    print(a,b)







name = input("Enter a file name:")
handle = open(name, 'r')

count1 = dict()
for word in handle:
    words = word.split()
    for w in words:
        count1[w] = count1.get(w,0)+1
    # print(count1)

big_counts = None
big_words = None
for count2, word2 in count1.items():
    if big_counts is None or count2 > big_counts:
        big_counts =count2
        big_words =word2
print(big_words, big_counts)


