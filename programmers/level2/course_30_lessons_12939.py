"""
    1. 문자열 분리 후 리스트 컴프리헨션으로 정수형 리스트 생성
    2. 정수형 리스트를 오름차순으로 정렬
    3. 처음 인덱스와 마지막 인덱스 출력
"""


def solution(s: str):
    # List Comprehension
    ans = [int(i) for i in s.split(' ')]
    # Sort Ascending
    ans.sort()
    # Return 'FirstIdx LastIdx'
    return f'{ans[0]} {ans[-1]}'


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
