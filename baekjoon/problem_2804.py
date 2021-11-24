import sys

A, B = sys.stdin.readline().rstrip().split(' ')

idx = [-1, -1]  # 위치를 지정하기 위한 리스트 [A위치, B위치]

A_len = len(A)
B_len = len(B)


ans = [['.' for i in range(A_len)] for j in range(B_len)]

# 문자가 맞는곳을 찾아봄
for i in range(A_len):
    for j in range(B_len):
        if A[i] == B[j]:
            idx[0], idx[1] = i, j
            ans[idx[1]] = list(A)  # 찾은 위치에 가로 문자열(A) 삽입
            break

    if -1 not in idx:
        break


for i in range(B_len):
    ans[i][idx[0]] = B[i]

for i in ans:
    print(''.join(i))
