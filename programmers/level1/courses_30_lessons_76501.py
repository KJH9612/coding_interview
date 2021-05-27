'''
    signs의 idx값이 True면 더하고 False면 뺌

'''
def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer

print(solution([4, 7, 12], [True, False, True]))