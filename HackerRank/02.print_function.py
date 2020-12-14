#https://www.hackerrank.com/challenges/python-print/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""The included code stub will read an integer,n, from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example
n=5
Print the string 12345"""

n = int(input("enter a number"))
a=[]
if n>=1 and n<=150:
    for i in range(1,n+1):
        a.append(str(i))
    print(''.join(a))