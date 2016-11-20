from ARCHIVE.CSGO_BASE import *


class Pot:

    unique_id = 0

    def __init__(self,parameters):
        Pot.unique_id = Pot.unique_id +1
        self.unique_id = Pot.unique_id
        self.parameters = parameters

    def is_valid(self,skin):
        if skin.value < self.parameters[0] or skin.value > self.parameters[1] :
            return False
        elif skin.one_month_fluctuation > 0.95:
            return False
        else:
            return True


#def add_to_pot(player,skins):
#1.  put items in pot inventory
#2.  add to pool dictonary containg players and their values of skins put in
#3   send message saying pot no longer accepts skins.
#4  add up values in dictonary to get total pot value.
#drawing:
#5 ake a list of players and player chance.
#6 agragate player chances to make a chance thing up to 1
#7make a random number 0-1
#8 check in range

#player_chance = player/staketotal_pool




Theo = User('Theo', create_random_skin_list(10, 10, 100))

test_pot = Pot([15, 95])

Theo.send_trade_offer(Theo.inventory, test_pot)
