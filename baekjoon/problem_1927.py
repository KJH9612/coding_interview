"""
    heapq 라이브러리를 사용하여 문제 해결
    리스트로 직접 구현하면 시간초과 났었음..
"""
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
lists = []

for i in range(n):
    value = int(sys.stdin.readline().rstrip())
    if value != 0:
        heapq.heappush(lists, value)
        try:
            print_v = heapq.heappop(lists)[1]
        except IndexError:
            print_v = 0
        print(print_v)


