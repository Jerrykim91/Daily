# Part05_11.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 10 
# 객체지향 프로그래밍(OOP)

# 특수형태의 메소드, 속성 접근 - 3
# 키 값에 따라 맞는 속성을 return 해서 정상적으로 실행 
# 존재하지 않는 키를 접근할 떄 카가 존재 여부를 알려줌  

# 속성 접근 -3 
class charactor:

    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성 되었습니다.')

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.hp, self.attack, self.defence))

    def __getitem__(self, name):
        if name == 'hp':
            return self.hp
        elif name == 'attack':
            return self.attack
        elif name == 'defence':
            return self.defence
        else:
            print('존재하지 않는 키값입니다.')

# 속성 설정 
print('='*40)
player_a = charactor(10,20,30)
print('='*40)

# player_a
print('player_a의 hp =', player_a['hp'])
print('player_a의 attack =', player_a['attack'])
print('player_a의 defence =', player_a['defence'])
print('='*40)

# 접근하고자 하는 키값에 조건분기를 만든 후 리턴 
print(" =====program end====== ")