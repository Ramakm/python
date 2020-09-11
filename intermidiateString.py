s = "Ramakrushna"
print(s[0:5])
print(s[6:20])

print(s[:6])   #from the start of the string to 6th position

print(s[6:])   #from 6th position to end of the string

print(s[:])    #print the whole string

# String Concatenation:

name ="heyla"

name2 = name + "mohapatra"

print(name2)
name3 = name +" " + "mohapatra"
print(name3)

# In as a logical Operator

fruit = "Apple"
'l' in fruit

# string Library

h = "hello Bob"
J = h.upper()
print(J)


#Search and replace method:

movie = "Pyar kiya toh darna kya"

m_replace = movie.replace("toh", "hello")
print(m_replace)

#remove strips from a string

school = "    DAV School  "
n_space = school.lstrip()
# n_space = school.replace(school)
print(n_space)

word = "bananana"
i = word.find("na")
print(i)