from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key  # 키
        self.value = value  # 값
        self.next = next  # 뒤쪽 노드 참조


class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""

        if isinstance(key, int):
            return key % self.capacity

        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""

        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""

        hash = self.hash_value(key)                     # 추가하는 key의 해시값
        p = self.table[hash]                            # 노드를 주목

        while p is not None:
            if p.key == key:
                return False                            # 추가 실패
            p = p.next                                  # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])       # 노드 생성
        self.table[hash] = temp                         # 노드를 추가
        return True                                     # 추가 성공