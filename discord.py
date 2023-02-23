import time
import random


def run():
    tick = random.randrange(0, 4)
    while tick > 0:
        tock = random.randrange(60, 70)
        sleep(tock)
        tick -= 1
    return True


if __name__ == '__main__':
    val = run()
    if val is True:
        print('/hunt')
