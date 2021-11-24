import sys

# 입력 Knuth-Morris-Pratt
# 문자 -를 기준으로 문자열을 split
s = sys.stdin.readline().rstrip().split('-')

# 리스트 컴프리헨션을 사용하여 가장 앞 문자만 추출
# join으로 다시 합침
print(''.join([i[0] for i in s]))

# 이렇게 해도 잘됨
"""
for i in s:
    print(i[0], end="")
"""