#for 变量名 in 可迭代的对象:
#对每一个变量做一些事情
list={"1":36,"2":37,"3":36,"4":35,"5":38}
for ID,temp in list.items():
    if temp>36:
        print(ID)
"""
在字典名.items（）中，变量ID被自动复制为键，变量temp被自动赋值为值
在字典名.items（）中，变量被赋值为键和值组成的元组
如果有3个变量的话会是怎么样呢？
"""
#注意一定是list.item(),因为这表示list中所有的键值对，如果不加，就单指清单
#一个是对字典中的键值对循环，一个是对字典循环，没有指定对字典里的什么东西循环
for staff_temp in list.items():
    ID=staff_temp[0]
    temp=staff_temp[1]
    if temp>=37:
        print(ID)

for tempe in list.values():
    temperature=tempe
    if tempe>36:
        print(temperature)
"""这个就只查找了异常温度但是没有锁定员工"""

#for+range
#range表示整数数列，可认为是左闭右开，range(5，10，2)，表示从5到9，步长为2，步长省略时默认为1
number=0
for i in range(1,101):
    number=number+i
"""要注意这个地方的=是赋值的意思，==才是等于
number初始值为1，i=1时循环一次后，number=0+1=1,i=2时再循环时，number=1+2=3,一直循环，直到循环到i=100
"""
print(number)

number=0
for number in range(1,101):
    number=number+1
    print(number)
"""
这个地方问题就比较多了，一个是循环时是number在range里循环，虽然一开始赋值number为0，
但是循环时又从1开始循环了，循环一次后number=number+1=1+1=2,所有是从2开始了
第二这个print放在循环里了，所有每计算一次就会打印一个值
"""