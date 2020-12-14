#https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    if query_name in student_marks.keys():
        pp=student_marks.get(query_name)
        sum=0
        avg=0.0
        for i in pp:
            sum=sum+i
        avg=sum/len(pp)
    print("{0:.2f}".format(avg))