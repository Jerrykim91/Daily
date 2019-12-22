# 8강__큐01

## 대표적인 데이터 구조 : 큐(Quene)

### 1. 큐 구조
# * 줄을 서는 행위와 유사
# * 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조 => 선입선출
#   - 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
#   - **FIFO(First-In, First-Out)** 또는 **LILO(Last-In, Last-Out)** 방식으로 스택과 꺼내는 순서가 반대


### 2. 알아둘 용어
# - Enqueue: 큐에 데이터를 **넣는** 기능     
# - Dequeue : 큐에 데이터를 **꺼내는** 기능     


### 3. 파이썬 queue 라이브러리 활용해서 큐 자료구조 사용해보기     
# - queue 라이브러리에는 다양한 큐 구조로 Queue(),LifoQueue(),PriorityQueue()제공
# - <font color='#BF360C'>프로그램을 작성할 때 프로그램에 따라 적합한 자료구조를 사용</font>     
#     - Queue() : 가장 일반적인 큐 자료구조 
#     - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)
#     - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터를 출력 
#         >  일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음 



### 3.1 Queue()로 큐 만들기(가장 일반적인 큐, FIFO(first-in,First-Out))
import queue

data_queue = queue.Queue()


data_queue.put("datacoding")
data_queue.put(1)
# data_queue 안에 두개가 들어 있다. 
data_queue.qsize()
# 가장 먼저 들어간데이터가 빠져 나온다. 
# 1회
data_queue.get()
# 2회
data_queue.get()
# check
data_queue.qsize()



# 9강__ 큐02
### 3.2  LifoQueue()큐 만들기 LILO(Last-In, Last-Out)
import queue

data_queue = queue.LifoQueue()


data_queue.put("datacoding")
data_queue.put(1)
# 두개가 들어있다 ! => 데이터를 뽑으면 
data_queue.qsize()
# 마지막에 넣은 것이 출력된다. 
data_queue.get()



### 3.3  Priority(우선순위)Queue()큐 만들기** 
# - **중요**
# - 데이터를 넣을때마다 우선순위를 매긴다. 
# - 꺼낼때는 우선순위대로 데이터를 꺼내온다.
import queue

data_queue = queue.PriorityQueue()


# 데이터는 하나인데 튜플로 들어감 
data_queue.put((10,"korea"))
data_queue.put((5,1))
data_queue.put((15,"china"))
# 들어있는데 이터가 3개라서 윗라인과 비교 
data_queue.qsize()

# 1st
# 우선순위가 높은거를 출력 
#  (앞,뒤) => 앞이 우선순위 
data_queue.get()
# 2nd
data_queue.get()


### 어디에 큐가 많이 쓰이는가 ?
# - 멀티 테스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용된다. => 운영체제 참조 
#     - 큐의 경우 장단점 보다는 특별히 언급되는 장점은 없다
#     -  큐의 활용의 예 => 프로세스 스케쥴링방식을 함께 이해해 두는 것이 좋다.


### 4. 프로그래밍 연습 
#### 연습 01 : 리스트 변수로 큐를 다루는 equeue, dequeue 기능 구현 
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data 

# for문으로 enqueue를 확인 
for i in range(10):
    enqueue(i)

len(queue_list)

# dequeue 확인 => 0번부터 순차적으로 출력된다. 
dequeue()
dequeue()


# 큐의 구조는 데이터 선입선출 
# 하지만 큐의 종류 중에서 
# 마지막의 것부터 출력하는 큐와
# 우선순위 먼저 출력하는 큐가 있다. 