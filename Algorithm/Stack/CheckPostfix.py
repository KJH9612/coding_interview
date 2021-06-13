from stack import Stack
from Postfix import evalPostfix

# 중위 표기식 후위 표기식으로 변환
# 우선순위가 높은 연산자는 모두 먼저 출력
# 우선순위가 같은 경우도 먼저 출력 ( ex -> `a-b+c` => ab-c+ )


def precedence(op):
    if op in ['(', ')']: return 0
    elif op in ['+', '-']: return 1
    elif op in ['*', '/']: return 2
    else: return -1


def Infix2Postfix(expr):
    stk = Stack()
    output = []
    for term in expr:
        if term in '(':
            stk.push('(')
        elif term in ')':
            while not stk.isEmpty():
                op = stk.pop()
                if op == '(': break
                else:
                    output.append(op)
        elif term in '+-*/':
            while not stk.isEmpty():
                op = stk.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    stk.pop()
                else: break
        else:
            output.append(term)

    while not stk.isEmpty():
        output.append(stk.pop())

    return output


expr = '8/2-3+(3*2)'
postfix = Infix2Postfix(list(expr))
result = evalPostfix(postfix)

print(f'중위 표기식 : {expr}')
print(f'후위 표기식 : {postfix}')
print(f'계산 결과 : {result}')
