"""自守数是指一个数的平方的尾数等于该数自身的自然数。例如：5**2 = 25，25**2 = 625，76**2 = 5776 ，求100000以内的自守数"""
import time
st = time.time()
for i in range(1000001):
    ii = i**2
    si = str(i)
    sii = str(ii)
    # print(si, sii)
    # print(sii[-1:-3:-1], sii[:])  # 因为默认步长是1，所以想要从右向左取就要主动设置步长为-1
    if si[-1:-len(si)-1:-1] == sii[-1:-len(si)-1:-1]:  # 切片这个索引真的杀我，有什么好理解的方法吗；目前只能两个相减得到的是我要的位数
        # print(si[-1:-len(si):-1], sii[-1:-len(si):-1])
        print(si)
end = time.time()
print(end - st)

"""比答案那个人的速度快了有10倍，他那个太复杂了"""

