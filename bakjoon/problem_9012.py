"""
    list를 이용하여 스택의 기능 append와 pop으로 해결
"""

import sys


def is_perfect(value: str) -> str:
    stk = []
    for ch in list(value):
        if ch == '(':           # 값이 ( 일 경우 stk에 데이터를 넣음
            stk.append('(')
        elif ch == ')':         # 값이 ) 일 경우
            if len(stk):        # stk안에 데이터가 있으면
                stk.pop()       # 데이터 꺼냄
            else:
                return 'NO'     # stk안에 데이터가 없을 경우

    return 'YES' if len(stk) == 0 else 'NO'  # stk가 비었으면 YES 아니면 NO


n = int(sys.stdin.readline().rstrip())

for i in range(n):
    string = sys.stdin.readline().rstrip()
    print(is_perfect(string))
