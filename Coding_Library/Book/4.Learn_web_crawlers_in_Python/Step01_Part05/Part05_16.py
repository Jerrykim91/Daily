# Part05_16.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 15 
# 객체지향 프로그래밍(OOP)

# 상속


# Super 활용 상속 
class unit:
    unit_cnt = 0

    def __init__(self):
        print('unit 생성')
        unit.unit_cnt += 1

    def move(self):
        print('unit move')


# bird 클래스 생성 - 유닛을 상속
class bird(unit):
    def __init__(self):
        print('bird 생성')
        super(bird, self).__init__()


# ground 클래스 생성
class ground(unit):
    def __init__(self):
        print('ground 생성')
        super(ground, self).__init__()


# 플레이어 생성(객체 생성)
print('='*40)
b1 = bird()
b3 = bird()
print('='*40)
# 객체 이동 
b1.move()
g1 = ground()

print(unit.unit_cnt)

print(" ===== program end ====== ")
# unit => 부모클래스

# super(해당 클래스명, self).__init__() 을 자식 생성자에 넣어주면 
# 자식 생성자가 호출 될때마다 부모 생성자를 호출 
# 부모 생성자가 호출될때 마다  unti_cnt가 1씩 증가 => 자식 생성자가 호출된 횟수를 알 수 있음  
