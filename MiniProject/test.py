# test.py

# 기본 틀
class Enermy:
    '''
    - SPEED, HP, EXP, LEVEL, COLOR, x, y 등 속성이 있다 
    - move, attack, demeage등의 행동을 가지고 있다
    - 이런 클레스를 구현하시오
    - 전제하지 않는 것들은 가정하시오
    '''
    # 맴버 변수
    SPEED, HP, EXP, LEVEL, COLOR, x, y = (0,0,0,0,0,0,0)
    
    # 맴버 함수 
    def move(self):pass
    def attack(self):pass
    def demeage(self):pass
    # 생성자
    def __init__(self):pass