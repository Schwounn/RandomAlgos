import math
import random
import matplotlib.pyplot as plt

seed = 0

def generate_points(n=10):
    rand = random.Random(seed)
    return [(rand.random(), rand.random()) for i in range(n)]


def dist(p1, p2):
    return math.sqrt(p1**2, p2**2)


def get_color(weight):
    return tuple((1 - weight for i in range(3)))

def plot(v, weights):
    plt.plot(*zip(*v), 'o')
    for i1, (x1, y1) in enumerate(v):
        for i2, (x2, y2) in enumerate(v):
            if i1 == i2:
                continue
            plt.plot((x1, x2), (y1, y2), '-', 1, color=get_color(weights[i1][i2]))
    plt.show()


def main():
    n = 10
    v = generate_points(n)
    weights = [[random.Random().random() for i in range(n)] for y in range(n)]
    plot(v, weights)

if __name__ == '__main__':
    main()
