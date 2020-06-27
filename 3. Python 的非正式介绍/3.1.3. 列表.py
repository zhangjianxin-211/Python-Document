# Python 中可以通过组合一些值得到多种 复合 数据类型。
# 其中最常用的 列表 ，可以通过方括号括起、逗号分隔的一组值（元素）得到。
# 一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同:
# >>> squares = [1, 4, 9, 16, 25]
# >>> squares
# [1, 4, 9, 16, 25]

squares = [1, 4, 9, 16, 25]
print(squares)

# 和字符串（以及各种内置的 sequence 类型）一样，列表也支持索引和切片:
# >>> squares[0]  # indexing returns the item
# 1
# >>> squares[-1]
# 25
# >>> squares[-3:]  # slicing returns a new list
# [9, 16, 25]
print(squares[0], squares[-1], squares[-3:])

# 所有的切片操作都返回一个包含所请求元素的新列表。
# 这意味着以下切片操作会返回列表的一个 浅拷贝:
# >>> squares[:]
# [1, 4, 9, 16, 25]

print(squares[:])

# 列表同样支持拼接操作:
# >>> squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(squares + [36, 49, 64, 81, 100])

# 与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
# >>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
# >>> 4 ** 3  # the cube of 4 is 64, not 65!
# 64
# >>> cubes[3] = 64  # replace the wrong value
# >>> cubes
# [1, 8, 27, 64, 125]

cubes = [1, 8, 27, 65, 125]
print(4 ** 3)
cubes[3] = 64
print(cubes)

# 你也可以在列表末尾通过 append() 方法 来添加新元素（我们将在后面介绍有关方法的详情）:
# >>> cubes.append(216)  # add the cube of 6
# >>> cubes.append(7 ** 3)  # and the cube of 7
# >>> cubes
# [1, 8, 27, 64, 125, 216, 343]

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)


# 给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:

# >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> # replace some values
# >>> letters[2:5] = ['C', 'D', 'E']
# >>> letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# >>> # now remove them
# >>> letters[2:5] = []
# >>> letters
# ['a', 'b', 'f', 'g']
# >>> # clear the list by replacing all the elements with an empty list
# >>> letters[:] = []
# >>> letters
# []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)


# 内置函数 len() 也可以作用到列表上:
# >>> letters = ['a', 'b', 'c', 'd']
# >>> len(letters)
# 4

letters = ['a', 'b', 'c', 'd']
print(len(letters))

# 也可以嵌套列表 (创建包含其他列表的列表), 比如说:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x, x[0], x[0][1])


