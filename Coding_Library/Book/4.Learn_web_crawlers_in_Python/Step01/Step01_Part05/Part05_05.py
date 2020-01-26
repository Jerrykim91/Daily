# Part05_05.py
#PART 05 : 파이썬 중급 문법 익히기          


# 클래스 만들기 - 4 
# 객체지향 프로그래밍(OOP)


# 개체의 속성 설정 
class charactor:

    def create(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def move(self):
        print( self,'move' )
        self.attack()

    # def attack(self):
    #     print( self,'attack' )
    
    def show_info(self):
        print("hp: %d, attack: %d, defence: %d " %(self.hp, self.attack, self.defence))
    

# 객체를 생성하는 부분 
player_a = charactor()
player_b = charactor()

print('='*40)
player_a.create(10,20,30)
player_b.create(100,200,300)
print('='*40)


player_a.show_info()
player_b.show_info()

