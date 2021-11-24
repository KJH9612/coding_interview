"""
    리스트형 스택을 이용하여 풀 수 있는 간단한 문제
"""


def solution(s):
    stk = []
    for i in range(len(s)):
        lens = len(stk)
        if lens != 0 and stk[lens - 1] == s[i]:  # 스택안에 데이터가 있고 top과 s의 현재 idx와 같으면
            stk.pop()       # pop
        else:
            stk.append(s[i])

    return 0 if len(stk) != 0 else 1