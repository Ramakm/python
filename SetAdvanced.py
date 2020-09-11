Friends = {"Ram", "Shyam", "Hari"}
Abroad = {"Bob", "Ram", "Shyam"}

Local_Friends = Abroad.difference(Friends)
print(Local_Friends)
Local_Friends = Friends.difference(Abroad)

Union_Friends = Friends.union(Abroad)
print(Union_Friends)

intersection_Friends = Friends.intersection(Abroad)
print(intersection_Friends)
