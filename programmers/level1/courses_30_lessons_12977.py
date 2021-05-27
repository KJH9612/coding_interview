"""
    itertools 안에 있는 combinations 함수를 이용하여
    조합을 구한 뒤 에라토스 테네스의 체로 미리 구해둔 소수 리스트를 이용하여
    소수인지 판별하고 소수이면 answer += 1

"""
# 조합을 구하기 위한 메소드
from itertools import combinations

prime = [False, False] + [True] * 3000


def eratos() -> None:   # 에라토스 테네스의 체
    for i in range(2, 3000):
        if prime[i]:
            prime[i] = True
            for j in range(2 * i, 3000, i):
                prime[j] = False


def solution(nums):
    answer = 0
    cc = list(combinations(nums, 3))

    eratos()
    for d_list in cc:
        if prime[sum(d_list)]:
            answer += 1

    return answer


print(solution([1, 2, 7, 6, 4]))
print(solution([1, 2, 3, 4]))