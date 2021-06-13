from stack import Stack

def evalPostfix(expr):
    stk = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = stk.pop()
            val1 = stk.pop()
            if token == '+': stk.push(val1 + val2)
            elif token == '-': stk.push(val1 - val2)
            elif token == '*': stk.push(val1 * val2)
            elif token == '/': stk.push(val1 / val2)
        else:
            stk.push(float(token))

    return stk.pop()