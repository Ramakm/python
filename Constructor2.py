class partyanimal:
    x=0
    name = ""
    def __init__(self, z):
        print("Hello to Constructor")
        self.name = z
        print(self.name,"name of that person")

    def party(self):
        self.x = self.x + 10
        print(self.x)
    def __del__(self):
        print("Bye Constructor")
an = partyanimal("Haguli")

an.party()
an.party()


class PartyAnimal:
    l = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.l = self.l + 1
        print(self.name,'party count',self.l)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()