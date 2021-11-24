"""
    2진수로 만든 뒤 1의 개수를 새고
    n + 1부터 시작하여 n + 1를 2진수로 바꾸어 1의 개수를 구했을 때
    개수가 같으면 return
"""


def solution(n):
    n_cnt = bin(n)[2:].count('1')
    counter = n + 1
    while True:
        if n_cnt == bin(counter)[2:].count('1'):
            return counter
        counter += 1
    return -1


print(solution(15))