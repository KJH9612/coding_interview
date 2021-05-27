"""
    A나 B 한쪽을 거꾸로 정렬하고 하나씩 곱하면 되는 문제
"""


def solution(A, B):
    A.sort()  # 오름차순 정렬
    B.sort(reverse=True)  # 내림차순 정렬

    # zip 관련 정보
    # https://www.daleseo.com/python-zip/
    return sum([a * b for a, b in zip(A, B)])


print(solution([1, 4, 2], [5, 4, 4]))
