def is_even(value: int) -> bool:
    """ 약수의 개수가 홀수인지 짝수인지 구하는 함수 """
    if value % 2:
        return False  # 홀수일 경우
    return True  # 짝수일 경우


def divisor_count(value: int) -> int:
    """ 약수 개수를 구하는 함수 """
    return len([i for i in range(1, (value // 2) + 1) if value % i == 0]) + 1


def solution(left, right):
    """ 메인 ? """
    answer = 0

    for i in range(left, right + 1):
        get_count = divisor_count(i)
        answer += i if is_even(get_count) else -i

    return answer


result = solution(13, 17)
print(result)