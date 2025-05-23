#6.9
ab_places = ['西安','陕西']
gouge_places = ['北京','海淀']
ys_plaves = ['新疆','上海']
favorite_places = {'ab':ab_places,'狗哥':gouge_places,'晏世豪':ys_plaves,}
for name,places in favorite_places.items():
    # for place in places:
    #     print(name,place)#注意循环时应该注意的问题，print应该放哪个循环的地方
    print(f'{name}喜欢的城市如下')
    for place in places:
        print(place)
    #但是始终有个问题就是不能出现在一行里面------列表准换为字符串，还有+=也可以使用，都是让东西出现在一行的


#6.10
hgg = [1,2,3]
gg = [4,5,6]
ab = [7,8,9]
dict_figure = {'哈狗哥':hgg,'狗哥':gg,'ab':ab,}
for k in dict_figure:
    print(f'{k}喜欢')
    for number in dict_figure[k]:#字典中键k对应的值，即列表：在列表中循环
        print(number)
#下面这种方法和上面城市的方法一样，两者都可以实现。
for k2,n in dict_figure.items():
    print(f'{k2}喜欢')
    for nn in n:#n在for中被赋值为列表了，此时也是在列表中循环
        print(nn)

#6.11
chong_ping = {'food':'hotpot','population':'3200w'}
nan_jing = {'food':'none','population':'931w'}
bei_jing = {'food':'shit','population':'2185w'}
cities = {'重庆':chong_ping,'南京':nan_jing,'北京':bei_jing}
for city,attribute in cities.items():
    print(f'{city}的属性')
    for key,value in attribute.items():
        print(f'{key}:{value}')




