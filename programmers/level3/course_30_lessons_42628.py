"""
    우선순위 큐는 데이터가 삽입될 때마다 정렬이 됨
    리스트로 간단하게 풀 수 있음
"""

def solution(operations):
    hq = []
    for operation in operations:
        com = operation.split(' ')  # 명령어 공백 단위로 구분
        if com[0] == 'I':   # Input이면
            hq.append(int(com[1]))  # 값 저장
            hq.sort()  # 리스트 정렬
        elif len(hq) > 0:   # 그 외 추출이면 여기로 오는데 hq에 값이 들어있어야 함
            if com[1] == '1':   # 1이면 최대값 삭제
                hq.pop()
            else:               # -1이면 최소값 삭제
                hq.pop(0)

    return [0, 0] if len(hq) == 0 else [max(hq), min(hq)]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))