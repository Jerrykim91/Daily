# Part05_04.py

#PART 05 : 파이썬 중급 문법 익히기          


# 클래스 만들기 -3 
# 객체지향 프로그래밍(OOP)


# 호출된 메소드가 다른 메소드를 호출 
class charactor:
    def move(self):
        print( self,'move' )
        self.attack()

    def attack(self):
        print( self,'attack' )

# 객체를 생성하는 부분 
player_a = charactor()
player_b = charactor()

player_a.move()
player_b.move()

