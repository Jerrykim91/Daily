# Part05_08.py
#PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 7 
# 객체지향 프로그래밍(OOP)

# 특수형태의 메소드, 속성 접근 

# call 활용 
class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성 되었습니다.')
        
    # 객체를 호출할 때 실행되는 메소드
    # 클래스가 동작하는 기능을 __call__메소드에 작성하면 함수이름을 고민하는 시간을 줄일수있음  
    def __call__(self):
        print("hp: %d, attack: %d, defence: %d "% (self.hp, self.attack, self.defence))

#    def show_info(self):
#         print("hp: %d, attack: %d, defence: %d "% (self.hp, self.attack, self.defence))


# 객체를 생성하는 부분 
print('='*40)
player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
print('='*40)


player_a()
player_b()
print('='*40)

print(" =====program end====== ")
