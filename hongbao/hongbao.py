import random


class Hongbao:
    def __init__(self, sum: float, number: int):
        self._remainder = sum
        self._number = number

    def open(self) -> float:
        if self._number <= 0:
            return 0
        get = self._get_money()
        self._remainder -= get
        self._number -= 1
        return get

    def _get_money(self):
        get_money = self._remainder

        if self._number == 2:
            get_money = random.random() * (self._remainder - 0.02) + 0.01
        elif self._number > 2:
            avg = self._remainder / self._number
            if random.random() < 0.5:
                get_money = random.random() * (avg - 0.01) + 0.01
            else:
                get_money = random.expovariate(2 / (avg - 0.01)) + avg
                max_money = self._remainder - self._number * 0.01 + 0.01
                if get_money > max_money:
                    get_money = max_money
        return round(get_money, 2)


if __name__ == '__main__':
    hongbao = Hongbao(1, 3)
    print(hongbao.open())
    print(hongbao.open())
    print(hongbao.open())
    print(hongbao.open())
