# 스택
![StackImage](http://lh4.ggpht.com/-yPC1y5pyEK8/UI5YdsZz_oI/AAAAAAAAA1Y/zSzytUOxVWA/clip_image001_thumb%25255B1%25255D.gif?imgmax=800)

데이터 입출력 순서 : 후입선출(LIFO)

push : 스택에 데이터를 넣는 작업 \
pop : 스택에서 데이터를 꺼내는 작업 \
top : 가장 마지막에 들어온 값을 가르킴 \
bottom : 가장 처음에 들어온 값을 가르킴\
<details>
    <summary>Fixed Stack</summary>

### [Fixed Stack](./fixed_stack) 구현 내용
#### 변수
> `stk` : 스택으로 사용할 변수명 \
> `capacity` : 스택의 최대 크기 len(stk)랑 같음 \
> `ptr` : 스택 포인터


#### 메소드
> `pop` : 가장 마지막에 들어온 원소 삭제 \
> `push` : 가장 마지막에 들어온 데이터 위에 삽입 \
> `is_empty` : 스택이 비어 있으면 True 아니면 False \
> `is_full` : 스택이 가득 차 있으면 True 아니면 False \
> `find` : 데이터를 검색 있으면 해당 index 반환 없으면 -1\
> `count` : 데이터의 개수를 구함\
> `dump` : 덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)\
> `__contains__` :
> `__len__` : 스택에 들어있는 데이터의 개수를 반환 \
> `__init__` : capacity 만큼의 크기를 가진 리스트형 스택 skt 를 생성
</details>

<details>
    <summary>Deque Stack</summary>

### [Deque Stack](./deque_stack) 구현 내용
#### 변수
> `__stk` : 스택으로 사용할 변수명 \
> `capacity` : 스택의 최대 크기 len(stk)랑 같음 \
> `ptr` : 스택 포인터


#### 메소드
> `pop` : 가장 마지막에 들어온 원소 삭제 \
> `push` : 가장 마지막에 들어온 데이터 위에 삽입 \
> `is_empty` : 스택이 비어 있으면 True 아니면 False \
> `is_full` : 스택이 가득 차 있으면 True 아니면 False \
> `find` : 데이터를 검색 있으면 해당 index 반환 없으면 -1\
> `count` : 데이터의 개수를 구함\
> `dump` : 덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)\
> `__contains__` :
> `__len__` : 스택에 들어있는 데이터의 개수를 반환 \
> `__init__` : capacity 만큼의 크기를 가진 리스트형 스택 skt 를 생성
</details>