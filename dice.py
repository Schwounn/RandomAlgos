
import random
import collections
import statistics

def roll_zero_or_one():
    return random.randint(0, 1)


def roll_zero_to_six():

    def roll_zero_to_seven():
        ret = 0
        for i in range(3):
            ret += roll_zero_or_one() * 2**i
        if ret == 7:
            ret = None
        return ret

    while (roll := roll_zero_to_seven()) is None:
        pass
    return roll


def verify_roll(n=1_000_000):
    rolls_gen = (roll_zero_to_six() for i in range(n))
    var = statistics.variance(rolls_gen)
    return var


def main():
    print(verify_roll())


if __name__ == '__main__':
    main()