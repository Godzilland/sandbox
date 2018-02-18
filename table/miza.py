class LandCard:

    def __init__(self, id):
        self.status = 2
        self.id = id
        self.name = 'zemlja' + str(id)
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


island = Island()

island.add_land_card(1, 0, 1)
island.add_land_card(2, 0, 5)
island.add_land_card(0, 1, 9)
island.add_land_card(1, 1, 2)
island.add_land_card(2, 1, 12)
island.add_land_card(3, 1, 10)

print(island.cards, flush=True)

# print(island.cards[(2, 0)], flush=True)

for x, y in island.cards.keys():
    print(island.cards[(x, y)])

if (1, 0) in island.cards.keys():
    print("veljavna koordinata")
else:
    print ("neveljavna koordinata")

print(island.sosedje(1, 1))




