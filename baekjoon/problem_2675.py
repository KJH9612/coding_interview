"""
    파이썬의 특징(?)을 알면 간단한 문제
"""

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    r, s = sys.stdin.readline().rstrip().split()
    r = int(r)
    answer = ''
    for j in range(len(s)):
        answer += s[j] * r

    print(answer)