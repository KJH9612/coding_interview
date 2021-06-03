class MyMatrix:
    def __init__(self, value: int) -> None:
        self.base_value = value
        self.mat = [[value] * value] * value
        a = 1
        for i in range(1, value - a):
            for j in range(i, value - a + 1):
                self.mat[j][i] *= value
            a += 1

    def print(self) -> None:
        for i in self.mat:
            print(i)


my_mat = MyMatrix(5)

my_mat.print()
