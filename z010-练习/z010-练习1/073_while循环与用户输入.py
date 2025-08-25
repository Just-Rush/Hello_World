''
#7.8------因为列表里的数量是有限且已知的，所以其实用while和for循环都可以，且这种情况往往用for循环会更方便一些
# foods = ['口香糖','水','米饭']
# finished_foods = []
# for food in foods:
#     print(f'我为了你准备了{food}')
#     finished_foods.append(food)
# print(finished_foods)

foods = ['口香糖','水','米饭','芒果','芒果','芒果']
finished_foods = []
# while foods:
#     food = foods.pop()
#     finished_foods.append(food)
#     print(f'我为你准备了{food}')
# print(finished_foods)
# print(foods)

#7.9---芒果---感觉改的怪怪的，练习题就不去管了
# print('芒果已经没有了')
# while '芒果' in foods:
#     foods.remove('芒果')
# while foods:
#     food = foods.pop()
#     finished_foods.append(food)
#     print(f'我为你准备了{food}')
# print(finished_foods)

#7.10
active = True
venues = []
while active:
    venue = input('where do you want to go in 5.1?please enter q to terminate')
    if venue == 'q':
        active = False
    elif venue != 'q':
        venues.append(venue)
print(f'awesome!that\'s a great idea,i want to go to {venues},too' )




