# Part05_15.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 14 
# 객체지향 프로그래밍(OOP)

# 상속
# 상속을 사용하는 이유 => 클래스의 기능을 그대로 가져다가 쓰려고 
# 게임에서 공중유닛과 지상유닛을 생성 => 공중유닛과 지상유닛은 서로 독립적인 클래스** 
# 그래서 유닛이라는 클래스를 상속받아 사용 


# 상속
class unit:
    # 변수 설정 
    unit_cnt = 0

    def __init__(self):
        print('unit 생성')
        # 유닛 생성
        unit.unit_cnt += 1

    def move(self):
        print('unit move')


# bird 클래스 생성 - 유닛을 상속
class bird(unit):
    def __init__(self):
        print('bird 생성')


# ground 클래스 생성
class ground(unit):
    def __init__(self):
        print('ground 생성')


# 플레이어 생성(객체 생성)
print('='*40)
b1 = bird()
b2 = bird()
b3 = bird()
print('='*40)
# 객체 이동 
b1.move()
print(unit.unit_cnt)

print(" ===== program end ====== ")
# unit => 부모클래스
# bird,ground => 자식클래스 
# bird()에는 move가 없음  부모클래스의 상속을 받기 때문에 사용가능 

# 이 코드에는 문제가 있음!
# 자식클래스는 부모클래스로부터 상속을 받아 사용 

# unit 총 개수를 unit에서 관리하기위해 unit클래스에 unit_cnt를 클래스 변수로 생성 
# 문제 !!!  unit의 생성자가 제대로 실행이 되지 않음  
# => 자식클래스의 생성자가 호출될 때 부모클래스도 같이 호출되어져야 함  