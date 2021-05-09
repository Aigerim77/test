class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
 
class KitchenTable(Table):
    def setPlaces(self, p):
        self.places = p
 
class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = KitchenTable(2, 2, 0.7)
t2 = DeskTable(1.5, 0.8, 0.75)
t3 = KitchenTable(1, 1.2, 0.8)

