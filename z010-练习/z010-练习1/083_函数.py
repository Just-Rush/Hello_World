#8.12---题的意思应该不是说要input，而是自己输入实参。但是可以搞成用户输入
def sandwich(*ingredient):
    '''三明治食材输入统计'''
    print(f'你添加的食材有{ingredient}')

sandwich('a','b','c')

ingredients = []
while True:
    a = input('输入你想加入的食材,输入 q 退出')
    # ingredients = []------这个地方把ingredients 重新赋值了,最后结果就始终是空集
    if a != 'q':
        ingredients.append(a)
    else:
        break
# ingredient = ",".join(str(element) for element in ingredients)
# 加不加上面那行代码都不能是纯字符串，不加是[()]，加了是（）,而且字符串都带引号。不想管这个了，感觉不是重点
sandwich(ingredients)


#8.13
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last#中括号这种形式是个字典添加键值对，中括号里的是键，= 的是值
    #将前两个参数转化为第三个参数的键值对,理解好理解，用可能不太熟练
    return user_info#retuen 赋值之后返回函数调用行，------return 的作用就是将赋值后的user_info返回函数调用行，之前看到的什么返回值的说法感觉有点被误导了，返回值这三个字感觉有点误导性。类似的break的作用就是终止循环返还循环开始行（或者理解为开始行的下一行也行，就结束循环，或是结束函数调用）
user_profile = build_profile('c','jr',high='180',weight='83')
print(user_profile)
#'''因为first\last name是晚于high等被添加进字典的，所以顺序上在他们后面'''

#8.14
def car_profile(manufacturer,model,**car_info):
    '''同#8.13的那个函数，那个是让复制的，这个是自己写的'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info#car_info中增加了两个键值对，所以返回增加的两个
car = car_profile('a','b',color='red',price='100000')
print(car)