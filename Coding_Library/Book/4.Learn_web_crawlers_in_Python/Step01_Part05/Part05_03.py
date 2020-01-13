# Part05_03.py

#PART 05 : 파이썬 중급 문법 익히기          


# 클래스 만들기 -2 
# 객체지향 프로그래밍(OOP)

# self : 참조자 
# self는 객체가 메소드를 호출할 때 어느 객체가 호출한 것인지 알려주는 키워드 
# 클래스에 메소드를 만들 떄 첫번째 인자는 self를 받아줘야함 



# 객체의 메소드 사용 
class charactor:
    def move(self):
        print( self,'move' )

    def attack(self):
        print( self,'attack' )

# 객체를 생성하는 부분 
player_a = charactor()
player_b = charactor()

# 호출 
player_a.move()
player_a.attack()
player_b.move()
player_b.attack()

# 객체가 메소드 및 속성을 호출할 때 마침표(.)이용 
# 메모리 주소를 통해서 누가 호출한 것인지를 알려주는 키워드 => self 
# 객체가 메소드를 호출할 때는 생성된 객체가 직접 호출학 때문에 self를 사용할 필요가 없음 
# but 메소드를 호출하고 객체로부터 직접 호출 된 메소드가 다른 메소드를 호출할 때는 
# self를 명시해줘야 해당 객체의 속성을 사용가능함 
  