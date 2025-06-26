# https://www.acmicpc.net/problem/5766

'''
N은 몇주인지, M은 몇명의 랭킨 정보인지.
0 0이 나오기 전까지 실행

다음오는 정보는 랭킹 정보. 
M명이 랭킹에 오름.
각 번호가 호출된 횟수를 확인 후, 2번째로 많이 호출 된 숫자를 입력.

시간 제한 1초, 메모리 제한 256MB, N,M 최대 500개

계산 10^9회 까지 가능
'''

import sys

input = sys.stdin.readline

end = True

def sol():
    N, M = map(int,input().split())
    scores = {i:[] for i in range(1,N+1)}
    for _ in range(N):
        winners = list(map(int,input.split()))
        for score in scores:                        #500회
            for winner in winners:                  #25*10^4회
                if winner in scores[score]:
                    winners.pop(winner)
                    

            

        

while end:
    sol()