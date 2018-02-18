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
        self.cards[(x, y)] = LandCard(id)


island = Island()

island.add_land_card(1, 0, 1)
island.add_land_card(2, 0, 5)
island.add_land_card(0, 1, 9)
island.add_land_card(1, 1, 2)

print(island.cards)





