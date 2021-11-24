"""
    스택의 기본 지식을 물어보는 문제
    귀찮으면 이렇게 안하고 list로 처리하면 된다
"""
import sys
from typing import Any

n = int(sys.stdin.readline().rstrip())

class Stack:
    def __init__(self) -> None:
        self.stk = []

    def __len__(self) -> int:
        return len(self.stk)

    def is_empty(self) -> bool:
        return 1 if len(self.stk) <= 0 else 0

    def push(self, value: Any) -> None:
        self.stk.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            return -1
        return self.stk.pop()

    def top(self) -> Any:
        if self.is_empty():
            return -1
        return self.stk[-1]


stk = Stack()

for i in range(n):
    command = sys.stdin.readline().rstrip()
    lists = command.split(' ')

    if 'push' in lists:
        stk.push(int(lists[1]))
    elif 'pop' in lists:
        print(stk.pop())
    elif 'size' in lists:
        print(stk.__len__())
    elif 'empty' in lists:
        print(stk.is_empty())
    elif 'top' in lists:
        print(stk.top())
