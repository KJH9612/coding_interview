import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    " 입력받은 단어를 공백 단위로 나누어 리스트로 만듬 "
    s = sys.stdin.readline().rstrip().split()
    " 리스트를 한번 뒤집음"
    s.reverse()
    " join 으로 리스트를 다시 합침 "
    print(f'Case #{i + 1}: {" ".join(s)}')
