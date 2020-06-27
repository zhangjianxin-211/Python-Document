"""
除了数字，Python 也可以操作字符串。
字符串有多种形式，可以使用单引号（'...'），双引号（"..."）都可以获得同样的结果 2。
反斜杠 \ 可以用来转义:

"""
# >>> 'spam eggs'  # single quotes
# 'spam eggs'
# >>> 'doesn\'t'  # use \' to escape the single quote...
# "doesn't"
# >>> "doesn't"  # ...or use double quotes instead
# "doesn't"
# >>> '"Yes," they said.'
# '"Yes," they said.'
# >>> "\"Yes,\" they said."
# '"Yes," they said.'
# >>> '"Isn\'t," they said.'
# '"Isn\'t," they said.'

"""
在交互式解释器中，输出的字符串外面会加上引号，特殊字符会使用反斜杠来转义。 
虽然有时这看起来会与输入不一样（外面所加的引号可能会改变），但两个字符串是相同的。 
如果字符串中有单引号而没有双引号，该字符串外将加双引号来表示，否则就加单引号。 
print() 函数会生成可读性更强的输出，即略去两边的引号，并且打印出经过转义的特殊字符:
"""

# >>> '"Isn\'t," they said.'
# '"Isn\'t," they said.'
# >>> print('"Isn\'t," they said.')
# "Isn't," they said.
# >>> s = 'First line.\nSecond line.'  # \n means newline
# >>> s  # without print(), \n is included in the output
# 'First line.\nSecond line.'
# >>> print(s)  # with print(), \n produces a new line
# First line.
# Second line.


# 如果你不希望前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可:

# >>> print('C:\some\name')  # here \n means newline!
# C:\some
# ame
# >>> print(r'C:\some\name')  # note the r before the quote
# C:\some\name



# 字符串字面值可以跨行连续输入。
# 一种方式是用三重引号："""...""" 或 '''...'''。
# 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。
# 如下例:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 将产生如下输出（注意最开始的换行没有包括进来）:
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to


# 字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:
# >>> 3 times 'un', followed by 'ium'
# >>> 3 * 'un' + 'ium'
# 'unununium'


# 相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.

# >>> 'Py' 'thon'
# 'Python'


# 把很长的字符串拆开分别输入的时候尤其有用:

# >>> text = ('Put several strings within parentheses '
# ...         'to have them joined together.')
# >>> text
# 'Put several strings within parentheses to have them joined together.'


# 只能对两个字面值这样操作，变量或表达式不行:

# >>> prefix = 'Py'
# >>> prefix 'thon'  # can't concatenate a variable and a string literal
#   File "<stdin>", line 1
#     prefix 'thon'
#                 ^
# SyntaxError: invalid syntax
# >>> ('un' * 3) 'ium'
#   File "<stdin>", line 1
#     ('un' * 3) 'ium'
#                    ^
# SyntaxError: invalid syntax


# 如果你想连接变量，或者连接变量和字面值，可以用 + 号:


# >>> prefix + 'thon'
# 'Python'


# 字符串是可以被 索引 （下标访问）的，第一个字符索引是 0。
# 单个字符并没有特殊的类型，只是一个长度为一的字符串:
# >>> word = 'Python'
# >>> word[0]  # character in position 0
# 'P'
# >>> word[5]  # character in position 5
# 'n'

word = 'Python'
print(word[0])
print(word[5])


# 索引也可以用负数，这种会从右边开始数:
# >>> word[-1]  # last character
# 'n'
# >>> word[-2]  # second-last character
# 'o'
# >>> word[-6]
# 'P'

print(word[-1], word[-2], word[-6])
print(word[-0])  # P   等于 0
# 注意 -0 和 0 是一样的，所以负数索引从 -1 开始。


# 除了索引，字符串还支持 切片。索引可以得到单个字符，而 切片 可以获取子字符串:

# >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
# 'Py'
# >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
# 'tho'

print(word[0:2], word[2:5])


# 注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
# >>> word[:2] + word[2:]
# 'Python'
# >>> word[:4] + word[4:]
# 'Python'

print(word[:2] + word[2:])
print(word[:4] + word[4:])


# 切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:
# >>> word[:2]   # character from the beginning to position 2 (excluded)
# 'Py'
# >>> word[4:]   # characters from position 4 (included) to the end
# 'on'
# >>> word[-2:]  # characters from the second-last (included) to the end
# 'on'
# 您也可以这么理解切片：将索引视作指向字符 之间 ，第一个字符的左侧标为0，最后一个字符的右侧标为 n ，其中 n 是字符串长度。例如:
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
# 第一行数标注了字符串 0...6 的索引的位置，第二行标注了对应的负的索引。那么从 i 到 j 的切片就包括了标有 i 和 j 的位置之间的所有字符。
#
# 对于使用非负索引的切片，如果索引不越界，那么得到的切片长度就是起止索引之差。例如， word[1:3] 的长度为2。
#
# 试图使用过大的索引会产生一个错误:
# >>> word[42]  # the word only has 6 characters
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# 但是，切片中的越界索引会被自动处理:
# >>> word[4:42]
# 'on'
# >>> word[42:]
# ''

# Python 中的字符串不能被修改，它们是 immutable 的。
# 因此，向字符串的某个索引位置赋值会产生一个错误:

# >>> word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> word[2:] = 'py'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment


# 如果需要一个不同的字符串，应当新建一个:
#
# >>>
# >>> 'J' + word[1:]
# 'Jython'
# >>> word[:2] + 'py'
# 'Pypy'


# 内建函数 len() 返回一个字符串的长度:
#
# >>>
# >>> s = 'supercalifragilisticexpialidocious'
# >>> len(s)
# 34


# 参见
# 文本序列类型 --- str
# 字符串是一种 序列类型 ，因此也支持序列类型的各种操作。
#
# 字符串的方法
# 字符串支持许多变换和查找的方法。
#
# 格式化字符串字面值
# 内嵌表达式的字符串字面值。
#
# 格式字符串语法
# 使用 str.format() 进行字符串格式化。
#
# printf 风格的字符串格式化
# 这里详述了使用 % 运算符进行字符串格式化。
