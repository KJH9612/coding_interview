import sys

n = int(sys.stdin.readline().rstrip())
lists = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    lists.append(num) if num else lists.pop()

print(sum(lists))