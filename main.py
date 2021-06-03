def pow(value, exp):
    res = 1
    while exp:
        if exp & 1:
           res *= value
        exp >>= 1
        value *= value
    return res


class Matrix:
    def __init__(self, value: int) -> None:
        self.lit = [[1 for j in range(value)] for i in range(value)]
        self.count = 1
        self.target = value // 2 + 1

        while self.count <= self.target:
            for i in range(self.count - 1, value - self.count + 1):
                for j in range(self.count - 1, value - self.count + 1):
                    self.lit[i][j] = pow(value, self.count)
            self.count += 1
            print()

        for i in self.lit:
            print(i)


s = Matrix(9)
