#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    s = list(s)
    p=[]
    for i in s:
        if i.islower():
            p.append(i.upper())
        elif i.isupper():
            p.append(i.lower())
        else:
            p.append(i)
    p= "".join(p)
    return p

