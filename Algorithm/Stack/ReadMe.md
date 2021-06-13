# Stack

![Stack Image](https://user-images.githubusercontent.com/44572131/121797295-5cbdd600-cc5a-11eb-8d5e-a86c37688e3f.gif)

> Stack 은 LIFO구조

> #### LIFO?
> > 데이터를 넣고 꺼내는 통로가 한곳인것 \
> > 가장 마지막에 들어간 데이터가 가장 처음에 나옴 \

### 스택은 어디에서 사용하는가?
> - 문서나 그림, 수식 등의 편집기에서 사용하는 되돌리기 기능 \
> - 이전 페이지 이동 \
> - 함수 호출에서 복귀주소를 기억 \
> - 계산기 프로그램 \
> - 괄호 검사
### 스택 기본 자료형

#### 연산(메서드)
> isEmpty() : 스택이 비어있는지 확인(비어있으면 True 아니면 False) \
> push(value) : 스택에 데이터를 넣음(스택 상단에 데이터 추가) \
> pop() : 스택에서 데이터 하나를 꺼냄(공백이면 None 아니면 top value) \
> size() : 현재 스택에 있는 데이터의 개수를 반환(int) \
> peek() : top에 어떤 데이터가 있는지 알려줌(공백이면 None 아니면 top value) \
> clear() : 스택을 비움 \
> dump() : 스택의 맨 아래 데이터부터 top까지 출력

#### 변수
> top : 스택의 데이터, 항목을 위한 공백 리스트 


#### 응용
> - [괄호검사](./CheckParentheses.py)
> - [후위표기연산(진행중)](./CheckPostfix.py)