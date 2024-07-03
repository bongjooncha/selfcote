# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        zip_string = ''
        prev = s[0:i]
        count = 1
        for a in range(i,len(s),i):
            if prev == s[a:a+i]:
                count +=1
            else:
                zip_string += str(count) +prev if count >1 else prev
                prev = s[a:a+i]
                count = 1
        zip_string += str(count) + prev if count > 1 else prev
        print(zip_string)
        answer = min(answer, len(zip_string))    
        
    return answer
