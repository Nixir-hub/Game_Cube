import random

def dice(y):
    """

    :param y:walls of dice
    :return: number of dice
    """
    dice_y = [3, 4, 6, 8, 10, 12, 20, 100]
    if y in dice_y:
        return y

def throw_dice(y):
    """

    :param y dice walls
    :return: number  of dice wall
    """
    return random.choice((list(range(1, dice(y)))))

def game_dice_sum(z=0):
    """

    :param z: extra modifer
    :return: sum of throws dice of y walls + extra modifer
    """
    while True:
        try:
            x = int(input("Chose throw number: "))
            y = int(input("Chose dice type: "))
            z = int(input("Chose extra modifer: "))
            all_dice_throws = [throw_dice(y) for x in range(x)]
            if type(x) == ValueError:
                break
            elif type(y) == ValueError:
                break
            elif type(z) == ValueError:
                break
            elif x < 1:
                print("If you want to throw u must set >0 in throw number ")
            elif y < 3:
                print("Dices starts from d3")
            else:
                break
        except Exception:
            print("All parms must be numbers!")
    return f'Sum of throws is: {sum(all_dice_throws) + z}'

print(game_dice_sum())
