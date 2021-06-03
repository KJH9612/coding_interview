def pow(value, exp):
    res = 1
    while exp:
        if exp & 1:
           res *= value
        exp >>= 1
        value *= value
    return res


class Matrix:
    def __init__(self, value) -> None:
        try:
            value = int(value)
            self.lit = [[1] * value] * value
            limit = value // 2
            for i in range(limit):
                for j in range(limit):
                    self.lit[i][j] *= value
                    self.lit[-(i + 1)][-(j + 1)] *= value
            print(self.lit)
        except:
            print(-1)


s = Matrix(5)
