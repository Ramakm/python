class PartyAnimal:
    l = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.l = self.l + 1
        print(self.name,'party count',self.l)

class footballfan (PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name , "points", self.points)
q = PartyAnimal('Argentina')
q.party()

p = footballfan("IND")
p.party()
p.touchdown()