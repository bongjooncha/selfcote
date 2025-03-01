## 문자 type에 따른 변경 속도

int, float, str, tuple, bool의 경우는 immutable한 객체이다.
따라서 이들을 수정하는 것은 이들의 memory에서 수정하는 것이 아닌 새로운 memory 공간에 변화한 이들을 넣고 그 변수의 위치를 변수에 저장하는 것이다.
그러다 보니 이들을 변경하는 것은 이들 자체를 새로 생성하는 속도와 동일하다.

반면 list, set, dict의 경우는 일정 부분만 변경하는 것이 가능하기 때문에 이들을 수정하는 속도는 매우 빠르다.

## .split()

map(int, input().split())을 할시 0으로 시작을 한다면 0을 인식하지 못함.

---

#DFS/BFS

## 스택(stack)

선입후출 구조 == 후입선출 구조
.append(n)으로 넣고 .pop()으로 제거

## 큐(Queue)

선입선출 구조
from collections import deque 사용 필요
queue = deque() 를 통해 Q생성
queue.append(n)을 통해 삽입, queue.popleft()통해 제거

DFS => Depth-First Search로 깊이 우선 탐색. 그래프에서 깊은 부분을 우선 탐색
풀이방식
가능한 모든 경우를 넣을 수 있는 graph 생성 후 주어진 조건을 입력
이 후, 주어진 조건을 활용해서 남은 부분 입력

BFS => Breadth First Search로 넓이(폭) 우선 탐색. 그래프에서 근처에 있는 부분 부터 탐색
풀이방식
queue를 사용. 먼저 방문 가능한 곳 처리.
방문한 곳에서 갈수 있는곳 입력. 그리고 방문했던곳 제거
