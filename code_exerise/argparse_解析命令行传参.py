# 小练习：看看argparse解析命令行传来的参数
import argparse

parser = argparse.ArgumentParser(description="演示 argparse 如何把命令行参数传进脚本")
"""
parser = argparse.ArgumentParser(...)
# 模块/函数来自哪里：argparse 是 Python 标准库里的模块（不需要安装任何东西，Python 自带）。
# ArgumentParser 是它的一个类（像“蓝图”），用来定义你的脚本希望从命令行接收什么参数，
并负责解析（把用户在命令行输入的东西变成 Python 变量）。
# description="..."：这是给程序做的说明文字，用户在命令行用 -h 或 --help 时会看到这段描述，帮助别人知道脚本是干什么的。
结果：parser 变量现在是一个 “解析器对象”，你接下来会用它来声明需要哪些参数。
"""
parser.add_argument("source_root", help="输出文件夹路径（示例）")
"""
作用：告诉解析器“我要一个位置参数，名字叫 source_root”，也就是运行脚本时必须提供的第一个参数。

位置参数（positional argument）：不像 --flag 那样可选，位置参数是必须的，而且顺序重要——第一个位置参数对应 source_root。

help="..."：这只是帮用户看的说明文字（当 -h 被调用时显示）。

举例：如果你在命令行写 python script.py A B，那么 A 会被解析为 source_root。
"""
parser.add_argument("target_folder", help="目标文件夹路径（示例）")
parser.add_argument("-v", "--verbose", action="store_true", help="show verbose")
"""
这是“可选参数”，不是必需有的
"""
args = parser.parse_args()
"""
真正干活的一行：这个函数读取当前运行脚本时命令行里所有参数（Python 把这些存在 sys.argv），把它们解析成一个“结构化”的对象（叫 Namespace），并返回给 args。

如果用户没有按要求提供参数（比如少了一个），parse_args() 会自动：

在终端打印一条错误消息（告诉你哪个参数缺失），

并自动退出脚本（返回非零退出码）。

如果运行时带了 -h 或 --help，parse_args() 会打印帮助信息（包含 description 和每个 help），然后退出程序。
"""

if args.verbose:
    print("加载详细信息！")


print("args 对象：", args)
print("source_root 字符串：", args.source_root)
print("target_folder 字符串：", args.target_folder)
print(type(args))
print(type(args.source_root))
print(args.target_folder)