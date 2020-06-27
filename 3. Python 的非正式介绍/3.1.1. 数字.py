"""
解释器就像一个简单的计算器一样：你可以在里面输入一个表达式然后它会写出答案。 表达式的语法很直接：运算符 +、-、*、/ 的用法和其他大部分语言一样（比如 Pascal 或者 C 语言）；括号 (()) 用来分组。比如:

>>>
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
整数（比如 2、4、20 ）的类型是 int，有小数部分的（比如 5.0、1.6 ）的类型是 float。 在这个手册的后半部分我们会看到更多的数字类型。

除法运算 (/) 永远返回浮点数类型。如果要做 floor division 得到一个整数结果（忽略小数部分）你可以使用 // 运算符；如果要计算余数，可以使用 %

>>>
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
在Python中，可以使用 ** 运算符来计算乘方 1

>>>
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
等号 (=) 用于给一个变量赋值。然后在下一个交互提示符之前不会有结果显示出来:

>>>
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
如果一个变量未定义（未赋值），试图使用它时会向你提示错误:

>>>
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
Python中提供浮点数的完整支持；包含多种混合类型运算数的运算会把整数转换为浮点数:

>>>
>>> 4 * 3.75 - 1
14.0
在交互模式下，上一次打印出来的表达式被赋值给变量 _。这意味着当你把Python用作桌面计算器时，继续计算会相对简单，比如:

>>>
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
这个变量应该被使用者当作是只读类型。不要向它显式地赋值——你会创建一个和它名字相同独立的本地变量，它会使用魔法行为屏蔽内部变量。

除了 int 和 float，Python也支持其他类型的数字，例如 Decimal 或者 Fraction。Python 也内置对 复数 的支持，使用后缀 j 或者 J 就可以表示虚数部分（例如 3+5j ）。

"""
