#https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numbers = list(map(int,s.split()))
    numbers.sort()
    answer = f"{numbers[0]} {numbers[-1]}"
    return answer

# s	                 return
# "1 2 3 4"	         "1 4"
# "-1 -2 -3 -4"	    "-4 -1"
# "-1 -1"	        "-1 -1"