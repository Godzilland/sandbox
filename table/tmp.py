class LandCard:

    def __init__(self, id):
        self.status = 2
        self.id = id
        self.name = 'zemlja' + id
        self.jpg = 'zemlja' + id + '.jpg'


    def getLC(self, id):
        return


class Island:

    def __init__(self):
        self.cards = {}

    def add_land_card(self, x, y, id):
        self.cards[(x, y)] = LandCard(id)


island = {(1, 0): 1,
          (2, 0): 5,
          (0, 1): 9,
          (1, 1): 3
          }

# x, y = 2, 0
# print(island.get((x, y)))

import random

def partial_shuffle(lst, imin, imax):
    lst[imin:imax] = sorted(lst[imin:imax], key=lambda x: random.random())
    return lst

lst = [1, 4, 2, 6, 12, 3, 7, 9, 23, 14]
print (partial_shuffle(lst, 3, 8))
