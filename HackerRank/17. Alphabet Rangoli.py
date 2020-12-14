#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string
alpha = string.ascii_lowercase
def print_rangoli(size):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        pp=(s[::-1]+s[1:])
        L.append(pp.center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
