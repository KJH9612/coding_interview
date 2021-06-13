# 조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함 ( 위반 예 -> `if (value == i))` )
# 조건 2 : 같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호가 먼저 나와야 함 ( 위반 예 -> `if (value == i))` )
# 조건 3 : 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안됨 ( 위반 예 -> `value[idx + 1)` )

from stack import Stack


def CheckParentheses(string: str):
    stk = Stack()

    for i in range(len(string)):
        if string[i] in ['(', '[', '{']:  # 열리는 괄호이면
            stk.push(string[i])           # 열린 괄호 스택에 넣음
        elif string[i] in [')', ']', '}']:
            if stk.isEmpty():  # 스택이 비어있으면
                return False

            if (string[i] == ')' and stk.peek() == '(') or \
                (string[i] == ']' and stk.peek() == '[') or \
                (string[i] == '}' and stk.peek() == '{'):
                    stk.pop()
            else:
                return False

    if stk.isEmpty():
        return True
    else:
        return False


print(CheckParentheses('{[()]}'))