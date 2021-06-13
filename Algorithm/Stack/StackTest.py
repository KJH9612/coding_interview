from stack import Stack

stk = Stack()

for i in range(10):
    stk.push(i + 1)
    stk.dump()


while not stk.isEmpty():
    stk.pop()
    stk.dump()