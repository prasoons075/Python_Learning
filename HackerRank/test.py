def count_substring(string, sub_string):
    count=0
    a=len(string)
    b=len(sub_string)
    if len(string)%2!=0:
        a=len(string)+1
        # if len(sub_string)%2!=0:
        #     b=len(sub_string)+1
        # else:
        #     b=len(sub_string)
    else:
        a=len(string)    
    for i in range(0,a,b):
        if sub_string in string[i:]:
            count+=1
    return count

if __name__ == '__main__':
    string = 'ABCDCDC'.strip()
    sub_string = 'CDC'.strip()
    count = count_substring(string, sub_string)
    print(count)