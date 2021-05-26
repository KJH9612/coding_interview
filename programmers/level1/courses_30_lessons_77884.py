"""
    left부터 right까지 n // 2 + 1번만 돌면서 나머지를 구했을 때 0이 나오면
    카운트를 증가시켜 짝수면 더하고 홀수면 빼서 return하는 간단한 문제
"""


def is_even(value: int) -> bool:
    """ 홀수인지 짞수인지 알기 위해 만든 함수 """
    if value % 2:
        return False
    return True


def divisor_count(value: int) -> int:
    """ value의 약수 개수를 구하기 위한 함수 """
    return len([i for i in range(1, (value // 2) + 1) if value % i == 0]) + 1


def solution(left, right):
    """ 문제 해결을 위한 함수 """
    answer = 0

    for i in range(left, right + 1):
        get_count = divisor_count(i)
        answer += i if is_even(get_count) else -i

    return answer

solution(13, 17)