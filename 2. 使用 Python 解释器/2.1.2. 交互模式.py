"""
在终端（tty）输入并执行指令时，我们说解释器是运行在 交互模式（interactive mode）。在这种模式中，它会显示 主提示符（primary prompt），提示输入下一条指令，通常用三个大于号（>>>）表示；连续输入行的时候，它会显示 次要提示符，默认是三个点（...）。进入解释器时，它会先显示欢迎信息、版本信息、版权声明，然后就会出现提示符：

$ python3.8
Python 3.8 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
多行指令需要在连续的多行中输入。比如，以 if 为例：

>>>
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
有关交互模式的更多内容，请见 交互模式。


"""