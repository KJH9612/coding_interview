'''
    선형 검색 알고리즘(Linear Search Algorithm)
    시간 복잡도 : O(n/2)
    사용 용도 : 정렬이 안된 배열에서 원소를 찾을 때 사용
    동작 방식 : 앞에서부터 순차적으로 하나씩 찾는 값이 있는지 검색
'''

from typing import Any, Sequence
import random


def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    lens = len(a)
    for i in range(lens):
        if a[i] == key:     # 성공시 idx 리턴
            return i
    return -1               # 검색 실패시 -1 리턴


if __name__ == '__main__':
    DataArr = [1, 2, 5, 3, 6, 4, 8, 10]

    idx = seq_search(DataArr, 6)

    if idx == -1:
        print("검색 실패")
    else:
        print(f"검색 성공 : {idx}")
