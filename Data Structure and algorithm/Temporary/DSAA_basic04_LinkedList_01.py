# 대표적인 데이터 구조 
## 링크드 리스트 (Linked list) 구조

### 링크드 리스트 (Linked list) 구조

 - 연결리스트 
 - 배열 : 순차적 연결된 공간에서 데이터를 나열하는 데이터구조 
 - 링크드 리스트 : 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
 - 원래는 C언어에서 주요한 데이터 구조 
    - 파이썬은 리스트 타입이 링크드 리스트기능을 모두 지원 

- 링크드 리스트 기본 구조와 용어
    - 노드(Node) : 데이터의 저장단위 (데이터값, 포인터)로 구성
    - 포인터(Pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결정보를 가지고 있는 공간 

# why Array? : STR을 저장하려면 ? => 미리 예약을 해야해 
```
내부주소  :  | 0000h | 0001h | 0002h | 0003h | 0004h | 0005h |
데이터    :  |   S   |   T   |   R   |   I   |   N   |   G   |
인덱스    :  |   0   |   1   |   2   |   3   |   4   |   5   |
```

# 배열은 미리 특정 공간을 예약을 해놓고 거기에 데이터를 쓰고 읽지만 
# 링크드 리스트는 예약이 필요없이 사용가능하다.-> 자유롭다.

# 일반적인 링크드 리스트 형태 -> 데이터가 주소를 가지고 있다
# a가 50(b) 주소값 -> B(50)가 60(c)-> C
```
-    :  |   12   | 포인터 |   99   | 포인터  |   37   | 포인터  |      |
-    :  |        |   ->   |        |   ->   |        |   ->   |      |
```

### 간단한 링크드 리스트 예
- 노드 구현
    - 보통 파이썬에서 링크드 리스트 구현시, 파이썬 클래스를 활용함
        - 파이썬 객체지향 문법 이해 필요 
             - 참고 :https://www.fun-coding.org/PL&OOP1-3.html

class Node1:
    def __init__(self,data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data, next=None):
    self.data = data
    self.next = next

#### Node와 Node 연결하기 (포인터 활용)

# 인자 하나에 디폴트 None 
# 별도로 객체를 두개를만듬 -> 하지만 연결은 안됨 
node1 = Node(1)
node2 = Node(2)
#  포인더 
# node1(head) -> node2
node1.next = node2
head = node1

#### 링크드 리스트로 데이터 추가하기
class Node: #next=None**
    def __init__(self, data, next=None)
        self.data = data
        self.next = next

# 별도 함수 => 마지막 노드를 찾기 위한 코드
def add(data):
    node = head #헤드의 값을 저장 
    # 링크드리스트가 저장하는 데이터 위치는 맨 뒤 
    
    # 노드가 가르치는 주소로 노드를 따라가는 구조 
    # node1 -> node2 -> node3 ->
    while node.next:
        # 다음 노드로 가는 주소 저장되어 있다 그러므로 
        # 다시 노드 = 경로 저장 
        # 다시 while 노드가 가진 경로를 반복하면서 노드 위치값을 추적 반복
        node = node.next
    #마지막 노드를 찾기 위한 코드    
    node.next = Node(data)

#
node1 = Node(1)
#node2 = Node(2)
#node1.next = node2
head = node1
for index in range(10):
    add(index)

#
for i in range(10):
    add(i)