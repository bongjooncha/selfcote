from itertools import combinations

def generate_combinations_sum(nums):
    result = []
    # 1부터 nums 리스트의 길이만큼의 조합 생성
    for r in range(1, len(nums) + 1):
        # combinations 함수로 조합 생성 후 각 조합의 합 계산하여 리스트에 추가
        for comb in combinations(nums, r):
            comb_sum = sum(comb)
            print(comb_sum)
            result.append(comb_sum)
    return result

# 예시 리스트
numbers = [1, 2, 3, 4]

# 조합의 합 생성 및 출력
combinations_sum_list = generate_combinations_sum(numbers)
print(combinations_sum_list)
