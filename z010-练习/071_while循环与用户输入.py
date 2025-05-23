#7.4
''
#pizza = input('请输入你想添加的配料选择完成后请输入:\'quit\'\n')
# message = ''
# while message != 'quit':
#     message = input('请输入你想添加的配料，选择完成后请输入:\'quit\'\n')
#     print(message)
'''
这个地方input必须放在下面对变量进行赋值的地方，
若在上面对pizza赋值为input，
再把 message 赋值为pizaa，因为input不在循环内，则message的值被第一次赋为输入时就不会再变了
'''
#改进:最终打出一个列表，并且让quit不打印出来，不添加进列表
message = ''
pizza_list = []
while message != 'quit':
    message = input('请输入你想添加的配料，选择完成后请输入:\'quit\'\n')
    if message != 'quit':
        pizza_list.append(message)
        print(message)
print(pizza_list)
for a in pizza_list:
    print(f'请确认你的配料包含：{a}')#这里如何可以使为1句话包含所有输入的配料------见070写的将列表转换为字符串应该就可以了

