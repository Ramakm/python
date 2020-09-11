class Partyanimal:
    x=0
    def party(self):
        self.x=self.x +1
        print("So far", self.x)

a = Partyanimal()

a.party()
a.party()
a.party()
print(type(a))
print(dir(a))