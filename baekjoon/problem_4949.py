"""
    닫는 소괄호 또는 대괄호가 나올 때 현재 stk의 top이 맞는지 아닌지 확인
    안맞으면 no 맞으면 계속 진행
"""

import sys

is_correct = True


def cor_chk(p_lists: list, p_char: str) -> bool:
    length = len(p_lists)

    if length <= 0 or p_lists[length - 1] != ('[' if p_char == ']' else '('):
        return False
    return True


while True:
    value = sys.stdin.readline().rstrip()
    lists = []
    is_correct = True
    if value == '.':
        break

    for i in range(len(value)):
        lens = len(lists)
        if value[i] == '[' or value[i] == '(':
            lists.append(value[i])
        elif value[i] == ']' or value[i] == ')':
            if cor_chk(lists, value[i]) is not False:
                lists.pop()
            else:
                is_correct = False

        if is_correct is False:
            break

    print('no' if is_correct is False or len(lists) else 'yes')