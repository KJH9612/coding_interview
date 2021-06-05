n = int(input('사이즈 : '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f'{cnt + 1} 번째 정수 : '))
    cnt += 1

    retry = input(f'계속 할까요(Y/N) : ')
    if retry in {'N', 'n'}:
        break

i = cnt - n
i = 0 if i < 0 else i

while i < cnt:
    print(f'{i + 1}번째 : {a[i % n]}')
    i += 1


