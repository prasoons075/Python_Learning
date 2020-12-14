#https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zenif __name__ == '__main__':
n = []
s = []
ans=[]
for _ in range(int(input())):
    name = input()
    n.append(name)
    score = float(input())
    s.append(score)            
a=max(s)
b=min(s)
for i in range(len(n)):
    if s[i]<a and s[i]>b:
        a=s[i]

for j in range(len(n)):
    if s[j]==a:
        ans.append(n[j])
ans=sorted(ans)
for i in ans:
    print(i)