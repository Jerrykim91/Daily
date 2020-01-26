# Part05_06.py
#PART 05 : 파이썬 중급 문법 익히기          


# 클래스 만들기 - 5 
# 객체지향 프로그래밍(OOP)

# 생성자, 소멸자 

# 생성자의 활용
class charactor:
    # 특수 메소드 언더바(__)양쪽에 2개씩
    # __init__ 객체가 생성될 때 자동으로 호출되는 함수  
    # 생성된 객체는 호출하지 말라는 의미 = 이유 => 파이썬은 모든것이 public(어디서든 호출)이 되기 때문  
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성 되었습니다. ')

    def move(self):
        print( self,'move' )
        self.attack()

    # def attack(self):
    #     print( self,'attack' )
    
    def show_info(self):
        print("hp: %d, attack: %d, defence: %d "% (self.hp, self.attack, self.defence))
    

# 객체를 생성하는 부분 
print('='*40)
player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
print('='*40)


player_a.show_info()
player_b.show_info()
print('='*40)

