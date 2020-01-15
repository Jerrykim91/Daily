# Part05_12.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 11 
# 객체지향 프로그래밍(OOP)

# 특수형태의 메소드, 속성 접근 - 4
# 여러 개의 키값으로 하나의 속성에 접근 
# 조건분기를 매번 만드는것은 번거로울 수 있음 

# 속성 접근 -4 
class charactor:

    def __init__(self, hp, attack, defence):
        # self.info에 사전형으로 초기화 정보입력
        self.info = {
            'hp' : hp,
            'attack':attack,
            'defence': defence 
        }

        # self.hp = hp
        # self.attack = attack
        # self.defence = defence
        print('player가 생성 되었습니다.')

    def __call__(self):
        print("hp: %d, attack: %d, defence: %d " % (self.info['hp'],self.info['attack'],self.info['defence']))

    def __getitem__(self, name):
        if name in self.info.keys():
            return self.info[name]
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
print('player_a의 defence =', player_a['mung'])

print('='*40)

# 생성자에서 초기화 정보를 딕셔너리로 저장한 후 속성을 가져올 때 
# 키가 존재하는지 검사하여 디셔너리로부터 접근해서 리턴  

# 코드를 작성하는데는 정답이 없다. => 다양한 관점으로 코드를 볼것

print(" =====program end====== ")