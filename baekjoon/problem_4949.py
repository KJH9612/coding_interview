"""
    닫는 소괄호 또는 대괄호가 나올 때 현재 stk의 top이 맞는지 아닌지 확인
    안맞으면 no 맞으면 계속 진행
"""

import sys

while True:
    value = sys.stdin.readline().rstrip()
    lists = []

    if value == '.':
        break

    for i in range(len(value)):
        if value[i] == '[' or value[i] == '(':
            lists.append(value[i])

        elif value[i] == ']' or value[i] == ')':
            if len(lists) and lists[len(lists) - 1] != value[i]:
                print('no')
                break
            elif len(lists) and lists[len(lists) - 1] == value[i]:
                lists.pop()

    print('no' if len(lists) else 'yes')
