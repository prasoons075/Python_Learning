#https://www.hackerrank.com/challenges/capitalize/problem


# Complete the solve function below.
def solve(s):
    s = list(s.split(' '))
    p=[]
    for i in s:
        if i.isalpha():
            p.append(i[0].upper()+i[1:]+" ")
        else:
            p.append(i)
            p.append(" ")            
    p="".join(p)
    return p
