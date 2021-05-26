from typing import Any

class FixedStack:
    """ 고정 길이 스택 클래스 """

    class Empty(Exception):
        """ stk가 비어있을 경우 예외 처리 """
        pass

    class Full(Exception):
        """ stk가 가득찼을 경우 예외 처리 """
        pass

    def __init__(self, capacity: int = 256) -> None:
        """ 스택 초기화 """
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """ 스택에 쌓여 있는 데이터 개수를 반환 """
        return self.ptr

    def is_empty(self) -> bool:
        """ 스택이 비어 있는지 확인 """
        return self.ptr <= 0

    def is_full(self) -> bool:
        """ 스택이 꽉 찼는지 확인 """
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """ 스택에 데이터를 넣음 """
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """ 스택에서 데이터를 꺼냄 """
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """ 스택에서 꼭대기 데이터를 들여다봄 """
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """ 스택을 비움 """
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """ 스택에서 value를 찾아 인덱스를 반환(없으면 -1 리턴)"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        """ 스택에 있는 value의 개수를 판단 """
        c = 0
        for i in range(self.ptr): # bottom부터 검색
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """ 스택에 value가 있는지 판단 """
        return self.count(value)

    def dump(self) -> None:
        """ 덤프 """
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
