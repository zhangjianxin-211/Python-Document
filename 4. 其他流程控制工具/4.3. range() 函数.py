# 如果你确实需要遍历一个数字序列，内置函数 range() 会派上用场。它生成算术级数:
for i in range(5):
    print(i)


# 给定的终止数值并不在要生成的序列里；range(10) 会生成10个值，并且是以合法的索引生成一个长度为10的序列。
# range也可以以另一个数字开头，或者以指定的幅度增加（甚至是负数；有时这也被叫做 '步进'）
print(range(5, 10))
print(range(0, 10, 3))
print(range(-10, -100, -30))


# 要以序列的索引来迭代，您可以将 range() 和 len() 组合如下:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 然而，在大多数这类情况下，使用 enumerate() 函数比较方便，请参见 循环的技巧 。
# 如果你只打印 range，会出现奇怪的结果:

