# 두 개의 리스트
list1 = ['W', 'B', 'W', 'W', 'B', 'B', 'W', 'B']
list2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

# 같은 위치에 같은 알파벳 개수 세기
count_same = sum(1 for x, y in zip(list1, list2) if x == y)

print("두 리스트에서 같은 위치에 같은 알파벳의 개수는:", count_same)
