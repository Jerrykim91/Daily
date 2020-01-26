# Part05_10.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 9 
# 객체지향 프로그래밍(OOP)

# 특수형태의 메소드, 속성 접근 - 2
# 딕셔너리에서 데이터를 사용하는 것처럼 [] 사용해서 속성에 접근
 
# 속성 접근 -2
class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성 되었습니다.')

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.hp, self.attack, self.defence))
    # [] 속성에 접근 할때 호출 되는 메소드 => ['']인자로 받음 
    def __getitem__(self, name):
        print(name)

# 속성 설정 
print('='*40)
player_a = charactor(10,20,30)
print('='*40)

# player_a
print('player_a의 hp =', player_a['hp'])
print('player_a의 attack =', player_a['attack'])
print('player_a의 defence =', player_a['defence'])
print('='*40)

# __getitem__에 리턴이 없어서 출력값 모두 None
print(" =====program end====== ")