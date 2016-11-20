import time
import msvcrt
unlocked_items = ['Fire','Water','Earth','Wind']
recipes = {'Steam':['Water','Fire','Steam'],'Lava':['Earth','Fire','Lava'],'Necromancer':['Corpse','Wizard','Necromancer']}

def option(x):
    if x == 'R':
        rules()
    elif x == 'X':
        recipe_combiner()
    elif x == 'P':
        print_unlocked_items()

def rules():
    print(' You can input letters to do certain things on this game')
    time.sleep(1)
    print('X = Make a recipe\nP = Show unlocked items\nS = Sugest a recipe\nR = Rules')

def recipe_combiner():
    print('input two items')
    item_1 = input()
    item_2 = input()
    for item_u in unlocked_items:
        if item_u == item_1:
            for item_r in recipes:
                if item_1 == recipes[item_r][0] and item_2 == recipes[item_r][1] or item_1 == recipes[item_r][1] and item_2 == recipes[item_r][0]:
                    unlocked_items.append(recipes[item_r][2])
                    print('You\'ve unlocked ' + recipes[item_r][2] +'!')
                else:
                    continue
def print_unlocked_items():
    print(unlocked_items)

#def organise():
    #deletes duplicates and orders





print('enter R to bring up rules')
while true:
    x = input()
    option(x)
    
