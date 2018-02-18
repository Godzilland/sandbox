class LandCard:

    def __init__(self, id):
        self.status = 2
        self.id = id
        self.name = 'o' + str(id)
        self.jpg = 'zemlja' + str(id) + '.jpg'

    def __repr__(self):
        return self.name

    def getLC(self, id):
        pass

class Island:

    def __init__(self):
        self.cards = {}

    def add_land_card(self, x, y, id):
        """ add_land_card - uporablja se samo pri kreiranju mize -
        postavlja otok"""
        self.cards[(x, y)] = LandCard(id)

    def sosedje(self, x, y, r=1, explorer=False):
        """ sosedje - vrne listo tuplejev v radiju
         r rabi navigator, ki lahko premakne nekoga za 2"""
        lista = []
        if (x, y - 1) in island.cards.keys():
            lista.append((x, y - 1))
        if (x - 1, y) in island.cards.keys():
            lista.append((x - 1, y))
        if (x + 1, y) in island.cards.keys():
            lista.append((x + 1, y))
        if (x, y + 1) in island.cards.keys():
            lista.append((x, y + 1))
        return lista

    def potopi(self, x, y):
        """ potopi karto za 1. Predvideva, da karta se ni cisto pod vodo (!= 0)"""
        self.cards[(x, y)].status = self.cards[(x, y)].status - 1
        if self.cards[(x, y)].status == 0:
            del self.cards[(x, y)]

    def dvigni(self, x, y):
        """ dvigne karto na 2. Predvideva, da je status karte 1"""
        self.cards[(x, y)].status = 2

    def izrisi(self):
        print("    {}  {}".format(self.cards[(1, 0)], self.cards[(2, 0)]))


class decek:
    def __init__(self, x, y, color, id):
        self.actions = 3
        self.cards = []
        self.x = x
        self.y = y
        self.color = color
        self.id = id

    def potopi(self, x, y):
        if (x, y) in island.sosedje(self.x, self.y):
            island.potopi(x, y)
            self.actions = self.actions - 1
            print("potopil {}".format((x, y)))

    def dvigni(self, x, y):
        if (x, y) in island.sosedje(self.x, self.y):
            island.dvigni(x, y)
            self.actions = self.actions - 1
            print("dvignil {}".format((x, y)))


island = Island()

island.add_land_card(1, 0, 1)
island.add_land_card(2, 0, 5)
island.add_land_card(0, 1, 9)
island.add_land_card(1, 1, 2)
island.add_land_card(2, 1, 12)
island.add_land_card(3, 1, 10)
island.add_land_card(0, 2, 4)
island.add_land_card(1, 2, 3)
island.add_land_card(2, 2, 7)
island.add_land_card(3, 2, 6)
island.add_land_card(1, 3, 11)
island.add_land_card(2, 3, 8)

# print(island.cards, flush=True)

# print(island.cards[(2, 0)], flush=True)

# for x, y in island.cards.keys():
#     print(island.cards[(x, y)])

if (1, 0) in island.cards.keys():
    print("veljavna koordinata")
else:
    print ("neveljavna koordinata")

print("Sosedje (1, 1)")
print(island.sosedje(1, 1))

print("Potopi (2, 1)")
island.potopi(2, 1)
print(island.sosedje(1, 1))

print("Potopi (2, 1)")
island.potopi(2, 1)
print(island.sosedje(1, 1))

engineer = decek(2, 2, 'red', 1)
print("sosedje inzenirja na 2, 2: {}".format(island.sosedje(2, 2)))
engineer.potopi(1, 2)
print("sosedje inzenirja na 2, 2: {}".format(island.sosedje(2, 2)))
engineer.potopi(1, 2)
print("sosedje inzenirja na 2, 2: {}".format(island.sosedje(2, 2)))
