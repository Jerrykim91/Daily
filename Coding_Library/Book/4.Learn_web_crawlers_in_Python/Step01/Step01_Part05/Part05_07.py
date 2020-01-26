# Part05_07.py
#PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 6 
# 객체지향 프로그래밍(OOP)


# 생성자, 소멸자 
# 소멸자의 활용 
class charactor:

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
    # 메모리공간에서 지워질 때 호출되는 것이 __del__() 메소드
    def __del__(self):
        print('player가 죽었습니다.')

# 객체를 생성하는 부분 
print('='*40)
player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)
print('='*40)


player_a.show_info()
player_b.show_info()
player_c.show_info()
print('='*40)

# del을 이용하면 객체를 없앨수 있음 
# => 사용했던 메모리를 반환하면서 해당 객체를 지움
del player_a
del player_b

print(" =====program end====== ")
