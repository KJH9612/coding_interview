# 큐

![QueueImage](https://ww.namu.la/s/b7785ff70f623fedbcae126015a3ae0a18b2f3a785bdd691d803aad2b10aee91f7b3fc438aadd3676cb84b9608ac18c4ce4dcc9a35eed34a61a2ffffff9b56ebe703f0f4992be754275c8a3a80cf88f073705e0c67c2fabcd4463e55d1b4df90)

###데이터 입출력 순서 : 선입선출(FIFO)


> Enqueue : 큐에 데이터를 추가 \
> Dequeue : 큐에 데이터를 추출 \
> Front : 데이터를 꺼내는 쪽을 말함 \
> Rear : 데이터를 빼는 쪽을 말함 \


<details>
    <summary>Fixed Queue</summary>

### [Fixed_Queue](./Fixed_Queue) 구현내용

#### 변수
> que : 리스트로 만든 큐 \
> capacity : 큐의 사이즈를 나타내는 int 형 정수 \
> front : 큐의 맨 앞을 가리킴 \
> rear : 큐의 맨 끝을 가리킴 \
> no : 큐 안에 있는 데이터의 개수를 나타냄 \

#### 메소드
> \_\_len\_\_ : 큐 안에 있는 데이터의 개수를 반환 \
> is_empty : 큐가 비어있는지 판단 비어있으면 True 아니면 False \
> is_full : 큐가 가득 차 있는지 판단 가득 차 있으면 True 아니면 False \
> enque : 큐에서 데이터를 넣는 작업 큐가 가득 차 있으면 FixedQueue.Full 발생 \
> deque : 큐에서 데이터를 꺼내는 작업 큐가 비어 있으면 FixedQueue.Empty 발생 \
> peek : 큐 안에 있는 데이터 중 맨 위에 있는 데이터를 반환합니다 비어 있으면 FixedQueue.Empty 발생 \
> find : 큐의 배열에서 x와 같은 데이터가 포함된 위치를 알아냅니다. \
> count : 큐에 있는 데이터 개수를 반환 \
> \_\_contains\_\_ : 큐에 데이터가 들어 있는지 확인 있으면 True 없으면 False \
> clear : 큐에 들어있는 데이터를 삭제합니다 \
> dump : 큐 안에 있는 데이터를 화면에 출력
</details>
<details>
    <summary>Priority Queue</summary>

> Enqueue 할 때 데이터에 우선순위를 부여
> Dequeue 할 때는 우선순위가 가장 높은 데이터를 꺼내는 방식 \
> 파이썬에서는 heapq 모듈에서 제공 \
> heap 에서의 Enqueue 는 heapq.heappush(heap, data)로 제공 \
> heap 에서의 Dequeue 는 heapq.heappop(heap)로 제공 \
</details>
<details>
    <summary>Ring Buffer</summary>

![Ring_Buffer](https://upload.wikimedia.org/wikipedia/commons/f/fd/Circular_Buffer_Animation.gif)
#### 설명
> 배열의 맨 끝의 원소와 맨 앞의 원소가 연결되는 자료구조 \
> Dequeue 할 때 원소를 옮기지 않는 큐 \
> 앞의 변수는 Front 뒤의 변수는 Rear로 구분


</details>

<details>
    <summary>deque</summary>

#### 설명
> 양방향 큐
> 앞이나 뒤 둘 다 Enqueue Dequeue 가능
> 파이썬에서는 collections.deque 제공
</details>