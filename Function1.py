def usersagein_Sec():
    users_age = int(input("Enter user age in years"))
    agein_sec = users_age *12 *365 * 24
    print(f"Age in sec is {agein_sec}")

print("Welcome to function project 1 ")
usersagein_Sec()

# Never use same name in anywhere inside a function program. else going to get error.

friends = []

def friend():
    friends.append("Ram")

friend()
friend()
friend()

print(friends)



