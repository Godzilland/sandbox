import random
from random import shuffle

class Card:
    # def __init__(self):
    #     pass

    def slice_shuffle(self, lst, imin, imax):
        lst[imin:imax] = sorted(lst[imin:imax], key=lambda x: random.random())
        return lst

class FloodCards(Card):
    def __init__(self):
        self.flood_cards = [i for i in range(1, 13)]
        self.flood_cards = self.slice_shuffle(self.flood_cards, 0, len(self.flood_cards))
        # shuffle(self.flood_cards)
        self.index = 0

    def next(self):
        if self.index == len(self.flood_cards):
            self.revert()
        self.index = self.index + 1
        return self.flood_cards[self.index - 1]

    def revert(self):
        self.flood_cards = self.slice_shuffle(self.flood_cards, 0, self.index)
        self.index = 0

    def remove(self, id):
        del self.flood_cards[id]


class LandCard(Card):

    def __init__(self, id):
        self.status = 2
        self.id = id
        self.name = 'o' + str(id)
        self.jpg = 'zemlja' + str(id) + '.jpg'

    def __repr__(self):
        return self.id

    def getLC(self, id):
        pass

class Island:

    def __init__(self):
        self.cards = {}
        land_cards = list(range(1, 25))
        i = 1
        for x in range(1, 5):
            for y in range(1, 5):
                land_card = random.choice(land_cards)
                self.add_land_card(x, y, land_card)
                land_cards.remove(land_card)
        # se robne ploscice
        border_coordinates = [(2, 0), (3, 0), (0, 2), (0, 3), (5, 2), (5, 3), (2, 5), (3, 5)]
        for x, y in border_coordinates:
            land_card = random.choice(land_cards)
            self.add_land_card(x, y, land_card)
            land_cards.remove(land_card)


    def add_land_card(self, x, y, id):
        """ add_land_card - uporablja se samo pri kreiranju mize -
        postavlja otok"""
        self.cards[(x, y)] = LandCard(id)


    def sosedje(self, x, y, r=1, explorer=False, additional_neighbours = None):
        """ sosedje - vrne listo tuplejev v radiju
         r rabi navigator, ki lahko premakne nekoga za 2"""
        neighbours = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        if additional_neighbours:
            neighbours = neighbours + additional_neighbours

        lista = []
        for dx, dy in neighbours:
            # dx, dy = neighbour
            if (x + dx, y + dy) in self.cards.keys() and self.cards[(x + dx, y + dy)]:
                lista.append((x + dx, y + dy))
        tmp_lista = list(lista)
        if r == 2:
            for land in lista:
                x, y = land
                # tmp_lista.append(self.sosedjeR(x, y))
                tmp_lista = tmp_lista + self.sosedje(x, y)
        return tmp_lista


    def _getXY(self, id):
        for card in self.cards.keys():
            # print(card)
            if self.cards[card].id == id:
                print("Nasel karto z id {}".format(id))
                return(card)

    def potopi(self, x, y = None):
        """ potopi karto za 1. Predvideva, da karta se ni cisto pod vodo (!= 0)"""
        """Ce je dan samo x je to id"""
        if not y:
            x, y = self._getXY(x)
            print("Koordinate: ({}, {})".format(x, y))

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

        print("{:12}".format(""), end="")
        self.__narisi_karto__(2, 0)
        self.__narisi_karto__(3, 0)
        print("")
        print("{:6}".format(""), end="")
        for x in range (1, 5):
            self.__narisi_karto__(x, 1)
        print("")

        for y in range(2, 4):
            for x in range(0, 6):
                self.__narisi_karto__(x, y)
            print("")

        print("{:6}".format(""), end="")
        for x in range (1, 5):
            self.__narisi_karto__(x, 4)
        print("")
        print("{:12}".format(""), end="")
        self.__narisi_karto__(2, 5)
        self.__narisi_karto__(3, 5)
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
    fc = FloodCards()
    engineer = decek(2, 2, 'red', 1)

    island.izrisi()
    island.potopi(12)

    print("Sosedje (1, 1)")
    print(island.sosedje(1, 1))

    # za test dveh sosedov. Napaka je, ce je vmes potopljeno polje
    print("Sosedje za explorerja (1, 1)")
    print(island.sosedje(1, 1, additional_neighbours= [(-1, 1), (0, 2), (1, 1), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, -2)]))

    # test dveh sosedov. Upostevati bi moralo tudi potopljeno polje
    print("Sosedje za explorerja (1, 1) z radij 2")
    print(island.sosedje(1, 1, r = 2))



    # for card in island.cards.values():
    #     print(card.id)


    # island.potopi(2)

    # print("Sosedje (1, 1)")
    # print(island.sosedje(1, 1))
    #
    # print("Potopi (2, 1)")
    # island.potopi(2, 1)
    # print(island.sosedje(1, 1))
    #
    # print("Potopi (2, 1)")
    # island.potopi(2, 1)
    # print(island.sosedje(1, 1))
    # island.izrisi()
    # eng = decek(2, 2, 'red', 1)
    # print("Potopi 1, 2")
    # island.potopi(1, 2)
    # island.potopi(1, 2)

    # island.izrisi()
    # v python 3 so keyi iteratable. v 2 so bili lista
    #  https://stackoverflow.com/questions/4512557/python-if-key-in-dict-vs-try-except
    # for i in range(1, 10):
    #     mm = random.choice(list(island.cards.keys()))
    #     if island.cards[mm]:
    #         print("ni potopljen: {}".format(mm))
    #     else:
    #         print("potopljen: {}".format(mm))

