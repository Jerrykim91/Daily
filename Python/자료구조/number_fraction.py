# number_fraction.py

##  복소수 

# 파이썬에서 복소수는  z= 3+4j 같이 생긴 복소수점 한쌍을 갖는 불변형이다. 

# z.real() ->  실수부 
# z.imag() -> 허수부
# z.conjugate() -> 컬레 복수부

# 복수수를 사용하기위해서는 cmath 모듈을 임포트 해야야한다. 
# cmath 는 math 모듈에 들어 있는 대부분의 삼각 함수, 로그함수의 복소수 버전을 제공한다. 



from fractions import Fraction  # 분수모듈


def rounding_floats(num1,plc):
    return round(num1,plc) # 까운 짝수값으로 올림 연산

def float_to_fractions(num):
    return Fraction(*num.as_integer_ratio())

def get_denominator(num1,num2):
    """
    분모를 반환한다.
    """
    a = Fraction(num1,num2)
    return a.denominator

def get_numerator(num1,num2):
    """
    분자를 반환한다.
    """
    a = Fraction(num1,num2)
    return a.numerator

def test_testing_floats():
    """
    동작함수

    """
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num6 = 6

    #
    assert()
    print('mas')



































## Fraction

## Fractions는 분수 모듈이다.
# - 유리수를 나타내는 Fraction클래스와 최대공약수(GCD:Greatest Common Divisor)를 구하는 모듈 함수
# 유리수 -> 두 정수의 분수 형태로 나타낼 수 있는 실수 두 정수의 분수 형태로 나타낼수 없는 실수를 무리수라고 한다. π(파이_, √2 는 대표적인 무리수

## assert : 가정 설정문
# assert 는 뒤의 조건이 true가 아니면 AssertError가 발생 
# assert 가 필요한 이유
# [가정 설정문(assert)](https://wikidocs.net/21050)
# [참조1](https://iissgnoheci.tistory.com/7)
# [참조2](https://brownbears.tistory.com/135)

# 참조 
# https://m.blog.naver.com/PostView.nhn?blogId=dudwo567890&logNo=130165177493&proxyReferer=https:%2F%2Fwww.google.com%2F