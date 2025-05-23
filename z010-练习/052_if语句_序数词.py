#5.11
figure_lists = [1,2,3,4,5,6,7,8,9,]
for figure in figure_lists:
    if figure == 1:
        print('1st')
    if figure == 2:
        print('2nd')
    if figure == 3:
        print('3rd')
    if figure == 4:
        print('4th')
'''
网上的别人写的
哎
'''
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    if number == 2:
        print(str(number) + 'nd')
    if number == 3:
        print(str(number) + 'rd')
    if number > 3:
        print(str(number) + 'th')