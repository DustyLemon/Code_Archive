def canBuy():
    print('You can buy the following movies:\n')
def alsoBuy():
    print('You can also buy:\n')
def ageU():
    print("""Universal films:
Toy story
Battle royale
A bugs life
Saw 3""")
def age12():
    print(""" Cert 12 films:
Harry potter
random film no.3
terminator
lemons be cray""")
def age15():
    print(""" Cert 15 filmz:
how i met your face
return of hitler- zombie nightmare
are you still reading my code?
I know where you live""")
def age18():
    print("""Cert 18 filmerinoes
Extreme gore bathtub party
Elmo
Decapithon marathon
A nightmare before Christmas 2 - time to die""")

print('Welcome to the movie store, weirdo moviestore frequenter :)')
age = input("How old is youz?")

while True:
    try:
        age = int(age) 
        break
    except ValueError or age < 0:
        print('That\'s not a number, douchard')
        age = input("Actually imput a valid number this time")


if age < 12:
    canBuy()
    ageU()
elif age >= 12 and age < 15:
    canBuy()
    ageU()
    alsoBuy()
    age12()
elif age >= 15 and age < 18:
    canBuy()
    ageU()
    alsoBuy()
    age12()
    alsoBuy()
    age15()
elif age >= 18:
    canBuy()
    ageU()
    alsoBuy()
    age12()
    alsoBuy()
    age15()
    alsoBuy()
    age18()

