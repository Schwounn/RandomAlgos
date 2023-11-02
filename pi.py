import math
import random
import matplotlib.pyplot as plt


class Pi_estimator():
    def __init__(self, seed=0):
        self.rand = random.Random()
        self.rand.seed(seed)

    def _get_point(self):
        return self.rand.uniform(-1, 1), self.rand.uniform(-1, 1)

    def _is_point_in_circle(self, p):
        x, y = p
        return (x ** 2 + y ** 2) < 1

    def _is_rand_point_in_circle(self):
        p = self._get_point()
        return self._is_point_in_circle(p)


    def run_plot(self, n=1_000_000):
        count_inside = 0
        series = []
        for i in range(n):
            count_inside += self._is_rand_point_in_circle()
            res = (count_inside / (i + 1)) * 4
            series.append(res)
        plt.plot((-1000, n), (math.pi, math.pi), '-', 1)
        plt.plot(range(n), series)
        plt.show()
        return (count_inside / n) * 4

    def plot_circle(self, n= 1_000_000):
        count_inside = 0
        series = []
        for i in range(n):
            p = self._get_point()
            count_inside += self._is_point_in_circle(p)
            series.append(p)
        figure, axes = plt.subplots()
        plt.plot(*zip(*series), 'o')
        unit_circle = plt.Circle((0, 0), 1, color='r', fill=False)
        axes.set_aspect(1)
        axes.add_artist(unit_circle)
        plt.show()
        return (count_inside / n) * 4


    def run(self, n=1_000_000):
        count_inside = 0
        for i in range(n):
            count_inside += self._is_rand_point_in_circle()
        return (count_inside / n) * 4


def main():
    est = Pi_estimator()
    print(est.run_plot())

if __name__ == '__main__':
    main()