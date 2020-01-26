# Part05_14.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 13 
# 객체지향 프로그래밍(OOP)

# 스태틱 메소드, 클래스 변수 
# 클래스에서 변수를 만들때 마다 독립적으로 변수부여 
# 모든 객체에서 클래스에 생성된 변수에 접근 => 클래스 변수 
# 클래스 변수 => 모든 객체에서 하나의 변수에 접근하는 것 

# cell_amt = 40
# form = '={0:^%s}=' % (cell_amt - 2)

# 클래스 변수 
class charactor:
    # 변수 설정 
    char_cnt = 0

    def __init__(self, hp, attack, defence):
        self.info = {
            'hp' : hp,
            'attack':attack,
            'defence': defence 
        }

        # 플레이어 생성 
        charactor.char_cnt += 1
        print('player가 생성 되었습니다. 생성된 유닛 수: %d' % (charactor.char_cnt))

    def __call__(self):
        print(" hp: %d, attack: %d, defence: %d " 
        % (self.info['hp'],self.info['attack'],self.info['defence']))


    def __del__(self):
        # 플레이어 제거 
        charactor.char_cnt -= 1
        print('player가 제거 되었습니다. 제거된 유닛 수: %d' % (charactor.char_cnt))

# 플레이어 생성(객체 생성)
print('='*40)
player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)
player_d = charactor(100,220,360)
player_e = charactor(500,400,200)

print('='*15,'플레이어제거','='*15)
# 플레이어 제거 
del player_d
print('='*40)

# 클래스 변수에 접근라기위해서는 self가 아닌 클래스명으로
# 클래스 변수는 해당 객체에 생성되는 것이 아니라 
# 클래스 자체에 한번 생성되기 때문에 클래스명으로 접근  

# 클래스 변수를 쓰는 대표적인 예
# 객체가 총 몇 개가 생성되었는지 확인할 때

# __init__메소드를 통해 char_cnt증가 , __del__이용해서 char_cnt 감소 
# 종료하기전 모든 객체가 지워지기 때문에 남아있는 객체에 대해서 __del__메소드가 호출 
print(" ===== program end ====== ")
# 그래서 이 이후에 플레이어가 제거 