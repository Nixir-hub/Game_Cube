import random


def throws_dice(y):
    """
    :param y: number of walls in dice
    :return: random number in range(1, y)
    """
    throw_dice = random.choice((list(range(1, y + 1))))
    return throw_dice


def roll(x, y, z=0):
    """
    x =  simulate number of throws
    y = number of walls in dice
    z = extra modifer

    """
    all_throws_dice = sum([throws_dice(y) for x in range(x)]) + z
    dices = [3, 4, 6, 8, 10, 12, 100]
    try:
        if y not in dices:
            raise Exception
    except Exception:
        print("No such dice!")

    return(all_throws_dice)


roll(2, 5, -10)
