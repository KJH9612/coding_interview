"""
    괄호만 들어옴
    stack의 push pop만 알면 되는 문제
"""
import sys

s = sys.stdin.readline().rstrip()
stk = []
counter = 0

for i in range(len(s)):
    if s[i] == '(':     # ( 가 들어왔을 때 stk에 푸시
        stk.append('(')
    elif s[i] == ')' and len(stk):  # ) 가 들어오고 stk에 값이 있으면
        stk.pop()   # 데이터 꺼냄
    else:
        counter += 1    #둘 다 아닐 경우 고쳐야 하기 때문에 counter

counter += len(stk)     # 남은 여는 괄호가 남아있을 수 있으므로 stk의 길이를 구해서 더함

print(counter)