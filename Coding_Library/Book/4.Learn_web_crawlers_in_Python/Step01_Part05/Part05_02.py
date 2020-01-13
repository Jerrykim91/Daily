# Part05_02.py

#PART 05 : 파이썬 중급 문법 익히기          


# 클래스 만들기 - 1
# 객체지향 프로그래밍(OOP)

# 클래스를 사용하는 이유 
# 변수와 함수의 집합체를 이용하여 미리 정의된 변수와 함수를 사용할 수 있도록 하는것
# 클래스로 할당한 값을 객체(인스턴스)라고 부름 
# 객체는 스스로 속성을 가지며 특정 행동을 할 수 있음 

# 클래스를 이용하면 중복 코드를 작성할 필요가 없음

# 캐릭터를 움직이는 함수 
def A_move():
    print('A charactor moved') 

def B_move():
    print('B charactor moved') 

# 위 처럼 코드를 생성하면 캐릭터의 종류가 늘수록 코드의 양이 많아질것     

# 클래스 생성   
class charactor:
    def move(self):
        print('move')

    def attack(self):
        print('attack')

# 클래스는 내부적으로 함수 및 변수를 가질수 있습니다. 
# 함수를 메소드, 변수를 속성 


# 객체를 생성하는 부분 
player_a = charactor()
player_b = charactor()

# 객체는 클래스에 의해 메모리에 할당된 상태를 의미 
 



