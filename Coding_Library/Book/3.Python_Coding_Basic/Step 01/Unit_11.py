# 사용자 함수 
from fun_pkg.random_num import random_num # 랜덤 숫자 생성

# Unit_11.py
# 시퀸즈 자료형 활용하기

txt_sequence = """
# 시퀸즈 자료형 활용하기 
- 리스트 , 튜플 , range, 문자열 => 연속성(sequence)을 가짐 
- 시퀸즈 자료형 => ( 리스트 , 튜플 , range, 문자열)
- 시퀸즈 자료형의 공통기능 사용 
    - 시퀸스 자료형의 큰 특징을 공통동작과 기능을 제공 
    - 시퀸즈 자료형으로 만든 객체를 시퀴즈 객체라고 함 => 각 값을 요소라고 칭 함 
    - 특정 값을 확인 
        => 값 in 시퀸즈 객체
        => 값 not in 시퀸즈 객체
        => 값 in range(값)
    - 시퀸즈 객채 연결하기 
        - 시퀸즈 객체 1 + 시퀸즈 객체 2  
        - **range는 + , \* 연산자로 객체를 연결 할 수 없다.** 
            - 근데!  리스트, 튜플로 묶어서 연결하면 가능 => 아래 예시 참조
     - 시퀸즈 객체 반복 
         - 시퀸즈 객체 * 정수
         - 정수 * 시퀸즈 객체 
     - 시퀸즈 요소 개수 구하기 
         - len(시퀸즈 객체)
             -> 리스트, 튜플, 문자열도 마찬가지로 길이를 구할 수 있다. 
             - range의 숫자 생성 개수 구하기 =>len(range( 값 ))
"""
print(txt_sequence)
print('-'*40)

# 시퀸즈 객채 연결하기 -> 시퀸즈 객체 1 + 시퀸즈 객체 2  
a  = [1,2,3]
b  = [6,7,8]
print(a + b)
print('-'*40)

# 이렇게
a = list(range(0,5)) + list(range(6,12))
print(a)
print('-'*40)

# 시퀸즈 객체 반복 
b = [1,2,3] *5
print(b)
print('-'*40)

# 시퀸즈 요소 개수 구하기  -> 리스트 튜플도 구해짐 
a  = [1,2,3]
print(len(a))
print('-'*40)

# range의 숫자 생성 개수 구하기 
a = len(range(0,10,2))
print(a)
print('-'*40)

# 문자열 길이 구하기 - 영어 
hello = 'Hello, world!'
print('print_hello_len : ',len(hello))
print('-'*40)

# 문자열 길이 구하기 - 한국어 
hello = '안녕하세요'
print('print_안녕하세요_ 길이 : ',len(hello))
print('-'*40)

# 인덱스 사용하기 
txt_index = """
# 인덱스 사용하기 
    => 시퀸스 객체에 [](대괄호)를 붙이고 []안에 각 요소의 인텍스를 지정하면 해당 요소에 접근가능 
- 시퀸즈 객체에 들어있는 요소에 접근하는 방법을 확인 
- 시퀸즈 객체의 각 요소는 순서는 정해져 있으며 이 순서를 인덱스라고 함 

시퀸스 객체[인덱스]

## 인덱스( index, 색인 )
    - 위칫값을 뜻하는데 국어사전 옆면에 ㄱ, ㄴ, ㄷ으로 표시해 놓은것과 비슷 
    - 주의 ) 시퀸스 객체의 인덱스는 항상 0부터 시작한다는거 


""" 
print(txt_index)
print('-'*40)

# 인덱스 사용하기 - 1 

a = [38,26,53,72,19]
print('-'*20)

print(a[0])   # 리스트의 첫번째 요소를 출력 => 인덱스 0 
print('-'*20)

print(a[2])   # 리스트의 세번째 요소를 출력 => 인덱스 3
print('-'*20)

print(a[4])   # 리스트의 다섯번째 요소를 출력 => 인덱스 4
print('-'*20)

# 튜 플 
b = (38,26,53,72,19)
print(b[2])    # 튜플의 세번째 요소를 출력 => 인덱스 3
print('-'*20)

ran = range(0, 10, 2) # 0 부터 10 까지 2 단계씩 출력 
r = list(ran)

print(ran[2])
print('-'*20)

print( r ) # print(ran[2])가 제대로 출력된 것을 확인가능
print('-'*40)

# 문자열 인덱스 
hello = 'hello world!'

print( hello[2] )
print( hello[5] )   # 공백도 인식
print('-'*20)

hello = list(hello) # 확인 
print(hello)
print('-'*40)

# 시퀸즈 객체에 인덱스를 지정하지 않으면 
# c를 이용해서 확인 
c = [ 38, 26, 53, 72, 19]
print(c) # c를 그냥 불러오는것 => c에 담긴 리스트 내용의 전부를 출력 
print('-'*40)

# __getitem__ 메소드 

txt_getitem = """
#  __getitem__ 메소드
시퀸즈 객체에서 대괄호를 사용하면 
실제로는 __getitem__ 메소드가 호출되어 요소를 가져옴 

직접 호출도 가능 
시퀸스 객체. __getitem__(index)

__getitem__메서드를 이용한 추가적인 것은 
unit_39(이터레이터)에서 추가로 설명  

일단 아래에 __getitem__메서드를 이용해 호출 해보겠음
"""
print(txt_getitem)
print('-'*40)
 
# __getitem__ 메소드 - 실습  
a = list(range(10))
# print( a )
print(a.__getitem__(5))
print('-'*40)

# 음수 인덱스 지정하기 
ran = random_num(5)
print(ran, ran[-2], ran[-1])
print('-'*40)

# 튜플로 인덱스 지정하기 
ran_1 = tuple(ran)
print(ran_1,ran_1[-3])









print('-'*40)