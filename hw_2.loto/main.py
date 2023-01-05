import random
import sys
import pprint

draft = [None, None, None, None, None, ..., ..., ..., ...]


class Card:
    def __init__(self, player_id):
        self._id = 0 if player_id == "AI" else player_id
        self.data = [random.sample(draft, 9),
                     random.sample(draft, 9),
                     random.sample(draft, 9)]
        self.all_numbers = sorted(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                 21, 22, 23, 24, 25,
                                                 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                                                 44, 45, 46, 47, 48,
                                                 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                                                 67, 68, 69, 70, 71,
                                                 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                                                 90], 27))


    def fill_data(self):
        for i in range(27):
            if not self.data[i // 9][i % 9]:
                self.data[i // 9][i % 9] = self.all_numbers[i]

        self.draw()


    def draw(self):
        sys.stdout.write(f"----Карточка игрока {self._id}----\n") if self._id != 0 else sys.stdout.write(f"----Карточка компьютера----\n")
        for j in self.data:
            for i in j:
                if i == Ellipsis:
                    sys.stdout.write("  ")
                elif i // 10 < 1:
                    sys.stdout.write(f" {i}")
                else:
                    sys.stdout.write(str(i))
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        sys.stdout.write("\n")


class Barrel:
    def __init__(self):
        self.all_barrels = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                          23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
                                          42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                                          61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                                          80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], 90)
        self.index = -1

    def next(self):
        self.index += 1
        return self.all_barrels[self.index], 90 - self.index


def main():
    first_cards = Card("Ann")
    second_cards = Card("AI")
    barrel = Barrel()

    first_cards.fill_data()
    second_cards.fill_data()
    is_first_player = True

    loop_bool = True

    while loop_bool:
        cur_barrel, left_barrels = barrel.next()

        sys.stdout.write(f"Новый бочонок: {cur_barrel} (осталось {left_barrels})\n")
        first_cards.draw()
        second_cards.draw()



        if left_barrels == 1:
            loop_bool = False



if __name__ == '__main__':
    main()
