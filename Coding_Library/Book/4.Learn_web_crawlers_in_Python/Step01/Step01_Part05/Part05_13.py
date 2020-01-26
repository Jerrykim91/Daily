# Part05_13.py
# PART 05 : 파이썬 중급 문법 익히기          

# 클래스 만들기 - 12 
# 객체지향 프로그래밍(OOP)

# 스태틱 메소드, 클래스 변수 
# 스태틱 메소드를 이용하면 함수의 공간을 부여 
# 함수명이 겹치는 현상을 방지

# 스태틱 메소드
class namespace1:

    @staticmethod
    def s1():
        print('namespace1 s1 스태틱 메소드')

    @staticmethod
    def s2():
        print('namespace1 s2 스태틱 메소드')


class namespace2:

    @staticmethod
    def s1():
        print('namespace2 s1 스태틱 메소드')  

    @staticmethod
    def s2():
        print('namespace2 s2 스태틱 메소드')


# 속성 설정 
print('='*40)
namespace1.s1()
namespace2.s2()
print('='*40)

# @staticmethod를 명시하면 클래스이름으로 해당 메소드에 접근할 수있음 
# @staticmethod로 명시된 메소드는 첫번째 인자 self를 받지 않음  
# => 단순히 네임스페이스 역할만 하기 때문 
# @staticmethod 명시된 메소드는 일반함수처럼 사용 
# => 클래스 내부에 속해있어서 [클래스.메소드]로 사용 

#print('='*40)
print(" =====program end====== ")