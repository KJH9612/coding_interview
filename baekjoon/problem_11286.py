"""
    heapq 라이브러리를 사용하여 문제 해결
    heapq는 최소 힙으로 구현되어 있음
    최소 힙에서 리스트로 직접 구현하면(귀찮아서 sort 막 사용) 시간초과 났었음..
"""
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lists = []

for i in range(n):
    value = int(sys.stdin.readline().rstrip())
    if value != 0:
        heapq.heappush(lists, (abs(value), value))  # 절댓값 힙을 구현하기 위해 abs메서드 사용
    else:
        try:
            print_v = heapq.heappop(lists)[1]
        except IndexError:
            print_v = 0
        print(print_v)


