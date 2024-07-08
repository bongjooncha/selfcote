# https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=python3

n = 100
def solution(n):
    ans = []
    ans.append(0)
    ans.append(1)
    if n >=2:
        for i in range(2,n+1):
            ans.append(ans[i-2]+ans[i-1])
    
    answer = ans[n]
    print(ans)
    return answer
print(solution(n))