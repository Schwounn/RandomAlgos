import math
import random
import matplotlib.pyplot as plt
import numpy as np

seed = 0
alpha = 1
beta = 1
decay = 0.1
num_ants = 10
num_iter = 1000
q = 1

def generate_points(n):
    rand = random.Random(seed)
    return {i: (rand.random(), rand.random()) for i in range(n)}


def generate_graph(n=20):
    v = generate_points(n)
    d = {(i, j): dist(v[i], v[j]) for i, j in np.ndindex((n, n)) if i != j}
    p = {(i, j): 1 for i, j in np.ndindex((n, n)) if i != j}
    return v, d, p


def dist(p1, p2):
    dy = p1[0] - p2[0]
    dx = p1[1] - p2[1]
    return math.sqrt(dy**2 + dx**2)


def get_choice(current_v, unvisited, weights):
    choice_weights = [weights[(current_v, i)]**beta for i in unvisited]
    return random.choices(unvisited, choice_weights)[0]


def get_color(weight):
    return tuple((min((1/weight),1) for i in range(3)))


def plot(v, weights):
    plt.plot(*zip(*[p for k, p in v.items()]), 'o')
    for i1, (x1, y1) in v.items():
        for i2, (x2, y2) in v.items():
            if i1 == i2:
                continue
            plt.plot((x1, x2), (y1, y2), '-', 1, color=get_color(weights[(i1, i2)]))


def plot_path(v, path, weights=None):
    plt.plot(*zip(*[p for k, p in v.items()]), 'o')
    if weights:
        plot(v, weights)
    for i, j in path_to_edges(path):
        x1, y1 = v[i]
        x2, y2 = v[j]
        plt.plot((x1, x2), (y1, y2), '-', 1, color='b')
    plt.show()


def generate_solution(v, w):
    current_v = 0
    unvisited = [k for k in v if k != 0]
    path = [0]
    while unvisited:
        next_v = get_choice(current_v, unvisited, w)
        path.append(next_v)
        unvisited.remove(next_v)
        current_v = next_v
    return path

def path_to_edges(path):
    ret = []
    for i in range(-1, len(path) - 1):
        ret.append((path[i], path[i + 1]))
    return ret

def score_edges(edges, d):
    return sum((d[e] for e in edges))

def get_weights(d, p):
    return {k: (1/d[k])**beta * p[k]**alpha for k in d}


def ACO(v, d, p, plotted=False):
    best_path = None
    best_score = None
    for i in range(num_iter):
        iter_paths = []
        for ant in range(num_ants):
            path = generate_solution(v, get_weights(d, p))
            score = score_edges(path_to_edges(path), d)
            if best_score is None or score < best_score:
                best_path, best_score = path, score
            iter_paths.append(path)
        for k in p:
            p[k] = (1 - decay)*p[k]
        for path in iter_paths:
            edges = path_to_edges(path)
            score = score_edges(edges, d)
            for edge in edges:
                p[edge] += q / score
        if plotted and i % 100 == 0:
            plot_path(v, best_path, get_weights(d, p))
    return best_path


def main():
    v, d, p = generate_graph(n=40)
    plot_path(v, generate_solution(v, get_weights(d, p)))
    plot_path(v, ACO(v, d, p))


if __name__ == '__main__':
    main()
