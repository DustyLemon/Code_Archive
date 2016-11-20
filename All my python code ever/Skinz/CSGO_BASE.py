__author__ = 'Theo'
import random


class Skin:                         # a simple class with two instance attributes: skin value and skin name. It also has
                                    # a class attribute called skin count just to count no. skins constructed.
    skin_count = 0

    def __init__(self, name, value ):
        self.name = name
        self.value = value
        self.one_month_fluctuation = random.random()
        Skin.skin_count = Skin.skin_count + 1

    def display_name(self):
        print(self.name)

    def display_value(self):
        print(self.value)


class User:

    def __init__(self, username, inventory):
        self.username = username
        self.inventory = inventory
        self.coin_balance = 0

    def change_balance(self, value):
        self.coin_balance = self.coin_balance + value

    def send_trade_offer(self, offered, pot,):
        invalid_skins = []
        for item in offered:
            if pot.is_valid(item) == False:
                invalid_skins.append(item)
        if len(invalid_skins) > 0:
            print('The following skins are invalid:\n')
            for skin in invalid_skins:
                print(skin)
            print('\nPlease remove these skins from the trade offer and try again')
            return 0
        else:
            print('The trade offer is valid and has been sent')
            return offered, self.username


def create_random_skin_list(total_skins, min_value, max_value):          # function which creates a  list of skins with random values,
    skin_list = []                          # the parameter deciding how many skins are created
    for n in range(1, total_skins):
        value = random.uniform(min_value, max_value)
        skin_list.append(Skin('test_skin' + str(value), value))
    return skin_list


def simple_round_of_betting(coins):         # function which simulates a round of betting taking no. of coins as input
                                            # and returning a skin chosen from a list
    mean = coins*0.95                       # the coefficient 0.95 is the customer's profit- they lose on average 5%/bet
    skins_greater_than_mean = []
    skins_less_than_mean = []
    for skin in create_random_skin_list(1000):
        if skin.value >= mean:
            skins_greater_than_mean.append(skin)
        else:
            skins_less_than_mean.append(skin)
    skin_less = random.choice(skins_less_than_mean)
    skin_greater = random.choice(skins_greater_than_mean)
    n = ((mean - skin_greater.value)/(skin_less.value - skin_greater.value))
    if random.random() <= n:
        print('You have made a loss, receiving skin' + skin_less.name)
        return skin_less.value
    else:
        print('You have made a profit, receiving skin' + skin_greater.name)
        return skin_greater.value



