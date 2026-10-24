"""
解包操作符 * 必须明确知道它解包后的元素去向（是传给函数了，还是装进另一个列表了）
"""

# 得到生成器
a = (i for i in range(3))
# * 解包生成器
print(a, "\n", *a)
a = (i for i in range(3))
b = [*a]
print(b)
a = (i for i in range(3))
c = (*a,)
print(c)
