#https://www.hackerrank.com/challenges/text-wrap/problem
def wrap(string, max_width):
    x=""
    for i in range(0,len(string),max_width):
        x=x+"".join(string[i:i+max_width]+"\n")
    return x
