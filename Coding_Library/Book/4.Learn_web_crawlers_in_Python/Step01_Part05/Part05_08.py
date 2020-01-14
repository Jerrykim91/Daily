# Part05_07.py
#PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 7 
# 객체지향 프로그래밍(OOP)


# call 활용 
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

del player_a
del player_b

print(" =====program end====== ")
