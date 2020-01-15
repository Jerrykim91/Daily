# Part05_09.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 8 
# 객체지향 프로그래밍(OOP)

# 특수형태의 메소드, 속성 접근 - 1

# 속성 접근 -1
class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성 되었습니다.')


# 속성 설정 
print('='*40)
player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
print('='*40)

# player_a
print('player_a의 hp =', player_a.hp)
print('player_a의 attack =', player_a.attack)
print('player_a의 defence =', player_a.defence)
# player_b
print('player_b의 hp =', player_b.hp)
print('player_b의 attack =', player_b.attack)
print('player_b의 defence =', player_b.defence)
print('='*40)

print(" =====program end====== ")