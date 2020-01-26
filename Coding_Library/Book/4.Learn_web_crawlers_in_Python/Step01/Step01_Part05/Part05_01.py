# Part05_01.py

#PART 05 : 파이썬 중급 문법 익히기          

# 함수 만들기 
# f(x)=x 는 y=x 표현  1차방정식 
def f(x): # (x)는 파라미터 
    # def는 함수의 키워드
    return x # 반환 값 

# f(x) 출력은 없다. 
print('='*30)

# 함수 호출 
var = f(10)
print(var)
# f()함수는 x라는이름으로 파라미터를 하나 받고 그대로 반환해주는 코드
# 10을 받고 10을 반환(return) 
print('='*30)


# return 
# 값 반환 / 함수 종료 
# 함수가 인자를 받고 값을 돌려줄때 
# 해당 함수를 끝낼 때 사용하는것이 return => return을 넣는것은 중요한 포인트 

# 홀수와 짝수를 구분하는 함수 생성 
def division(x):
    # 2개의 리턴값이 존재 
    if x%2:
        return True
    else:
        return False
    # 출력 되지 않는 running
    print('running')

var1 = division(10)
var2 = division(11)

print(var1)
print(var2)
print('='*30)

# 만약 리턴이 없다면 
# 함수는 꼭 반환이 있을 필요가 없음

def a(x):
    print('running ' + str(x))
    pass
var3 = a(10)
print(var3)
# a()함수는 반환이 없음
# 반환이 없는 함수를 출력하면 None 값을 반환
print('='*30)

# 인자(parameter-파라미터)
# 함수를 호출할때 데이터를 넘길수 있으며 
# 함수는 넘어온 데이터를 인자(parameter-파라미터)를 받는다라고 표현 
# 함수를 정의하고 해당 함수를 사용할때 인자를 맞추것은 **매우 중요 

def fy(x, y=20):
    # 함수를 만들때 미리 값을 넣어주면 
    # 호출시 해당 인자를 맞추지 않아도 미리넣어둔 값이들어감
    print('running ' + str(x) +' '+str(y))
    return x + y
# 첫번째 인자만 들어가서 두번째 인자는 y=20 
var1 = fy(10)
# 두번째 인자는 전달 했기때문에 y = 20 이 아니라 40 
var2 = fy(10, 40)

print(var1)
print(var2)
print('='*30)

