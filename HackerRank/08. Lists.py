#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    final = []
    N = int(input())
    for i in range(N):
        tmp = input()
        tmp = tmp.split(' ')
        if 'insert' in tmp:
            
            final.insert(int(tmp[1]),int(tmp[2]))
        elif 'append' in tmp:
            
            final.append(int(tmp[1]))
        elif 'sort' in tmp:
            
            final.sort()
        elif 'print' in tmp:
            
            print(final)
        elif 'reverse' in tmp:
            
            final.reverse()
        elif 'remove' in tmp:
            
            final.remove(int(tmp[1]))
        elif 'pop' in tmp:
            
            final.pop()
      
