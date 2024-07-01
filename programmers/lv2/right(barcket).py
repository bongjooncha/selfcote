#https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if s[0] == ")": return False
    else:
        match = 0
        for i in s:
            if match < 0: return False
            if i == "(":
                match += 1
            else: match -= 1
    if match != 0: return False       

    return True

#   s   	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false