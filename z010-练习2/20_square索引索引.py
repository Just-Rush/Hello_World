"""打印所有不超过n（取n<256）的其平方具有对称性质的数（也称回文数）"""
import time
st = time.time()
for i in range(256):
    ii = i**2
    sii = str(ii)
    if sii[0:int(len(sii)/2)] == sii[-1:-int(len(sii)/2+1):-1]:  # int是为了向下取整(不管正负，直接去除小数部分)
        print(i, ii)
end = time.time()
print(end - st)
# 这个索引问题真的好烦，一开始是sii[1:int(len(sii/2))]
"""这里 初始应该是从0开始，不是1，错了;所以后面+1也错了。是看索引对应的元素，索引对应的元素就是第索引+1个元素，不是第索引个元素"""
