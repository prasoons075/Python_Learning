from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("G:\python_tut\After_4_Feb_2020\wordninja_words.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
import csv
w = csv.writer(open("G:\python_tut\After_4_Feb_2020\output.csv", "w"))
for key, val in wordcost.items():
    w.writerow([key, val])
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        #for pp,jj in enumerate(reversed(cost[max(0, i-maxword):i])): print('k=',pp,'c=',jj,wordcost.get(s[i-pp-1:i]),cost)
        # for k,c in candidates:
        #     print(k,c)
        #     print(min(c + wordcost.get(s[i-k-1:i], 9e999), k+1))
        #     #print(minimum)
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        best_match(i)
        #print(s[i-1],i-1,c,k)
        #cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        best_match(i)
        #print(c,k,cost[i])
        # assert c == cost[i]
        # out.append(s[i-k:i])
        # i -= k

    return " ".join(reversed(out))
s = 'thumbgreenappleactiveassignmentweeklymetaphor'
print(len(s))
print(infer_spaces(s))