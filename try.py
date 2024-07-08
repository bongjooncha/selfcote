import itertools

def find_next_number(n):
    # 주어진 숫자를 문자열로 변환하여 리스트로 만든다.
    digits = list(str(n))
    
    # 모든 순열을 생성하고 정렬한다.
    permutations = sorted(set(itertools.permutations(digits)))
    
    # 현재 숫자보다 큰 숫자를 찾는다.
    for perm in permutations:
        perm_number = int("".join(perm))
        if perm_number > n:
            return perm_number

    return -1  # 이 경우는 문제의 조건상 발생하지 않는다.

# 입력 받기
N = int(input().strip())
print(N)

# 다음날 풀 문제의 개수 출력
print(find_next_number(N))
