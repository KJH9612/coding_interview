# math.factorial() 함수가 있음

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    n = int(input('Factorial : '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
