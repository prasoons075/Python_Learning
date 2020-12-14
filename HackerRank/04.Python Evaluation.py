#https://www.hackerrank.com/challenges/python-eval/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.

For example:

>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
Here, eval() can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.

For example:

>>> type(eval("len"))
<type 'builtin_function_or_method'>
Without eval()

>>> type("len")
<type 'str'>
Task
You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var)."""

p=str(input())
p=p.split('print')
print(p)
print(eval(p[1]))