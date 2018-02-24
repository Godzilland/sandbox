import random

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
        self.add_land_card(1, 0, 1)
        self.add_land_card(2, 0, 5)
        self.add_land_card(0, 1, 9)
        self.add_land_card(1, 1, 2)
        self.add_land_card(2, 1, 12)
        self.add_land_card(3, 1, 10)
        self.add_land_card(0, 2, 4)
        self.add_land_card(1, 2, 3)
        self.add_land_card(2, 2, 7)
        self.add_land_card(3, 2, 6)
        self.add_land_card(1, 3, 11)
        self.add_land_card(2, 3, 8)

    def add_land_card(self, x, y, id):
        """ add_land_card - uporablja se samo pri kreiranju mize -
        postavlja otok"""
        self.cards[(x, y)] = LandCard(id)

    def sosedje(self, x, y, r=1, explorer=False):
        """ sosedje - vrne listo tuplejev v radiju
         r rabi navigator, ki lahko premakne nekoga za 2"""
        lista = []
        if (x, y - 1) in self.cards.keys() and self.cards[(x, y - 1)]:
            lista.append((x, y - 1))
        if (x - 1, y) in self.cards.keys() and self.cards[(x - 1, y)]:
            lista.append((x - 1, y))
        if (x + 1, y) in self.cards.keys() and self.cards[(x + 1, y)]:
            lista.append((x + 1, y))
        if (x, y + 1) in self.cards.keys() and self.cards[(x, y + 1)]:
            lista.append((x, y + 1))
        return lista

    def potopi(self, x, y):
        """ potopi karto za 1. Predvideva, da karta se ni cisto pod vodo (!= 0)"""
        self.cards[(x, y)].status = self.cards[(x, y)].status - 1
        if self.cards[(x, y)].status == 0:
            # del self.cards[(x, y)]
            self.cards[(x, y)] = None

    def dvigni(self, x, y):
        """ dvigne karto na 2. Predvideva, da je status karte 1"""
        self.cards[(x, y)].status = 2

    def __narisi_karto__(self, x, y):
        if self.cards[(x, y)]:
            print("{:6}".format(self.cards[(x, y)].name), end="")
        else:
            # print("           ", end="")
            print("{:6}".format(""), end="")


    def izrisi(self):
        print("      ", end="")
        self.__narisi_karto__(1, 0)
        self.__narisi_karto__(2, 0)
        print("")
        self.__narisi_karto__(0, 1)
        self.__narisi_karto__(1, 1)
        self.__narisi_karto__(2, 1)
        self.__narisi_karto__(3, 1)
        print("")
        self.__narisi_karto__(0, 2)
        self.__narisi_karto__(1, 2)
        self.__narisi_karto__(2, 2)
        self.__narisi_karto__(3, 2)
        print("")
        print("      ", end="")
        self.__narisi_karto__(1, 3)
        self.__narisi_karto__(2, 3)
        print("")


class decek:
    def __init__(self, x, y, color, id, name="Engineer", updiag=False):
        self.actions = 3
        self.hand = []
        self.x = x
        self.y = y
        self.name = name
        self.dvignidiag = updiag
        self.color = color
        self.id = id

    def get_xy(self):
        print ('({}, {})'.format(self.x, self.y))


    def __action_complete(self):
        self.actions = self.actions - 1
        print("{} actions left".format(self.actions))

    # def potopi(self, x, y):
    #     if (x, y) in island.sosedje(self.x, self.y):
    #         island.potopi(x, y)
    #         self.actions = self.actions - 1
    #         print("potopil {}".format((x, y)))
    #         self.__action_complete()

    def dvigni(self, x, y):
        if (x, y) in island.sosedje(self.x, self.y):
            island.dvigni(x, y)
            print("dvignil {}".format((x, y)))
            self.__action_complete()

    def move(self, x, y):
        if (x, y) in island.sosedje(self.x, self.y):
            self.x = x
            self.y = y
            self.__action_complete()

if __name__ == '__main__':
    island = Island()


    # print(island.cards, flush=True)

    # print(island.cards[(2, 0)], flush=True)

    # for x, y in island.cards.keys():
    #     print(island.cards[(x, y)])

    island.izrisi()

    print("Sosedje (1, 1)")
    print(island.sosedje(1, 1))

    print("Potopi (2, 1)")
    island.potopi(2, 1)
    print(island.sosedje(1, 1))

    print("Potopi (2, 1)")
    island.potopi(2, 1)
    print(island.sosedje(1, 1))
    island.izrisi()
    eng = decek(2, 2, 'red', 1)
    print("Potopi 1, 2")
    island.potopi(1, 2)
    island.potopi(1, 2)

    island.izrisi()
    # v python 3 so keyi iteratable. v 2 so bili lista
    #  https://stackoverflow.com/questions/4512557/python-if-key-in-dict-vs-try-except
    for i in range(1, 10):
        mm = random.choice(list(island.cards.keys()))
        if island.cards[mm]:
            print("ni potopljen: {}".format(mm))
        else:
            print("potopljen: {}".format(mm))

