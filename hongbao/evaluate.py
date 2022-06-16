import matplotlib.pyplot as plt

from hongbao import Hongbao

if __name__ == '__main__':
    ITER = int(1e6)
    hongbao_number = 4
    total_money = 1

    history: list[list[float]] = [[] for _ in range(hongbao_number)]
    history_sum: list[float] = [0 for _ in range(hongbao_number)]
    for _ in range(ITER):
        hongbao = Hongbao(total_money, hongbao_number)
        history.append([])
        for i in range(hongbao_number):
            money = hongbao.open()
            history_sum[i] += money
            history[i].append(money)
    print([i / ITER for i in history_sum])
    for i in range(hongbao_number):
        plt.hist(history[i])
        plt.show()
