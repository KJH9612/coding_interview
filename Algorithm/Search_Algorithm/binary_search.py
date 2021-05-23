'''
    이진 탐색 알고리즘(Binary Search Algorithm)
    시간 복잡도 : O(log N)
    사용 용도 : 정렬이 된 배열에서 특정 원소를 찾을 때 사용
    동작 방식 : len(n - 1) // 2를 처음 위치로 두고 찾을 원소가
              idx보다 작을 경우 right의 값을 current - 1로 만듦
              idx보다 클 경우 left의 값을 current + 1로 만듦

'''

from typing import Any, Sequence


def binary_search(a: Sequence, key: Any) -> int:
    left = 0
    right = len(a) - 1
    while True:
        current = (left + right) // 2
        if a[current] == key:
            return current
        elif a[current] < key:
            left = current + 1
        else:
            right = current - 1
        if left > right:
            break

    return -1


if __name__ == '__main__':
    DataArr = [1, 2, 5, 3, 6, 4, 8, 10]

    idx = binary_search(DataArr, 8)

    if idx == -1:
        print("검색 실패")
    else:
        print(f"검색 성공 : {idx}")