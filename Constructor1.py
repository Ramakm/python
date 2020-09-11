class partyanimal:
    x=0
    def __init__(self):
        print("Hello to Constructor")

    def party(self):
        self.x = self.x + 10
        print(self.x)
    def __del__(self):
        print("Bye Constructor")
an = partyanimal()

an.party()
# an.__init__()
an.party()