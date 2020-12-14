#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    string = list(string)
    string[position]= character
    string = ''.join(string)
    return string

