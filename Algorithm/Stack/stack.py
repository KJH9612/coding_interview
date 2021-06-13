class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def dump(self):  # 전체 데이터를 확인하기 위해 따로 추가함
        print('[ ', end='')
        for value in range(len(self.top)):
            print(value, end=' ')
        print(']', end='\n')

