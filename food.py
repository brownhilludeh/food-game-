import random

Food = ['chin chin', 'hi', 'fufu', 'nothing', 'human being', 'spoilt rice']
List = random.choice(Food)

comp = random.choice(Food)


def yeah():
    List = input(f'Gush a chouce : ')

    if List != comp:
        print('hurray we have a champion')
    else:
        print('yeah your choice is the same as mine')

# print(Food)
# print(List)
# print(Comp)

using this method will print the function of Yeah and return none as result 
print(yeah())

yeah()
