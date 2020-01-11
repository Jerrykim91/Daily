# Step01_Part04.py

# PART 04 : 파이썬 초급 문법 익히기  
# - 파이썬은 간단하고 직관적이며 인터프리터 언어에 다양한 라이브러리와 프레임워크를 제공 => 개발에 좀 더 집중할 수 있음
 
print('='*30)
# 변수 - 데이터가 저장되는 공간 
# 상수 - 변하지않는값 

# 변수를 사용하는 방법 
var = 10 
print('실행결과 >>', var)
print('='*30)
# 변수로 변수값 바꾸기 
var1 = 10
var2 = 20 
print('실행결과 >>', var1)
var1 = var2
print('실행결과 >>', var1)
print('='*30)

# 변수 생성없이 변수를 사용할 때 
novar = '''
변수 선언 없이 print(novar)을 출력하면  
아래와 같은 에러발생 에러발생 
Traceback (most recent call last):
File "c:/Users/JerryKim/Desktop/2.Learn web crawlers in Python/Step01_Part04.py", line 23, in <module>
    print(novar) 
NameError: name 'novar' is not defined
'''
print('실행결과 >>', novar, '='*30) 

# Name Error 해결 
novar = '문자열, 정수, 실수, 불린등을 담아 출력 하면 Name Error해결 '
print(novar)
print('='*30)

# 변수이름 생성시 주의사항 
var = """
1. 내장함수로 변수의 이름을 짓는 것은 피해야한다. 
2. 변수의 이름을 시작할 때는 숫자, 특수 문자의 사용을 피해야한다. 
3. 변수의 이름을 한글로 만들수있지만, 피하는것을 권장
4. return, not,try,while,for,if, import와 같은 파이썬 내부에서사용하는 키워드는 변수이름으로 사용할수없다. 
"""
print('실행결과 >>', var)
print('='*30)

# 데이터 타입 
# 숫자형 => 양수, 음수 모두 사용 가능 
print('숫자형 - 정수1 >>' , 25)
print('숫자형 - 정수2 >>' , -25)
print('숫자형 - 실수1 >>' , 25.0)
print('숫자형 - 실수2 >>' , -25.1)
print('='*30)

# 하나의 변수만 가지고 데이터를 바꿔가면서 출력 
var1 = 25
print('실행결과 >>', var1)
var1 = 25.0
print('실행결과 >>', var1)
var1 = 25.9
print('실행결과 >>', var1)
var1 = -21.5
print('실행결과 >>', var1)
print('='*30)

# 사칙연산 
v1, v2 = 10, 25

print('실행결과 >>','v1+v2 = ',v1+v2)
print('실행결과 >>','v1-v2 = ',v1-v2)  
print('실행결과 >>','v1*v2 = ',v1*v2)
print('실행결과 >>','v1/v2 = ',v1/v2)
print('실행결과 >>','v1//v2 = ',v1//v2)
print('='*30)

# 문자열 
var1 = "파이썬은 인터프리터(interpreter)"
print('실행결과 >>', var1)
var2 = '1000원'
print('실행결과 >>', var2)
var3 = """ 긴 문장 """
print('실행결과 >>', var3)
var4 = ''' 단어, 짧은 문장  '''
print('실행결과 >>', var4)
print('='*30)
# 문자열 연산하기
var1 = '문자열'
var2 = '연산하기'

print('실행결과 >>', var1+" "+var2)
print('='*30)

# 문자열 치환하기 
# => replace()함수사용 " "띄워쓰기를 => "?" 변경
var = "배고파 "
print(var)
var = var.replace(" ","?")
print(var)
print('='*30)

# replace()함수사용해서 특정문자 없애기 
var = "제리는 많이 안 먹는다"
print(var)
var.replace("안","")
print(var)
print('='*30)

# 가격 처리하기 => 변수에 담아야한다 => 앞에 있는 내용을 엎어줘야해 
price = '19,000원'
print(price)
price = price.replace(',','').replace('원','')
print(price)
print('='*30)

# find를 이용해서 문자열 찾기 -1
var1 = '겅은사막은 존잼'
print(var1)
var1 = var1.replace('겅','검')
finded = var1.find('검')
print(finded)
print('='*30)

# find를 이용해서 문자열 찾기 -2 
print(var1,'에서 사 & 잼 위치출력 >> ')
print(var1.find('사'))
print(var1.find('잼'))
print('='*30)

# 문자열 인덱싱, 슬라이싱하기 
var = "인덱싱은 명시한 문자만 가지고 온다."
# 인덱싱하기
print(var[5])
print(var[6])
print(var[7])
print(var[9])
print(var[10])
# print(var[5,6,7,8,9,10])=> 불가
print('='*30)

# 슬라이싱하기
var = "슬라이싱은 부분적으로 필요한 부분만 잘라온다."
print(var[12:19])
print('='*30)

# 슬라이싱 고급스킬 
var = "슬라이싱 고급스킬"
print(var[:])
print(var[:4]) # 4 미만 
print(var[5:])
print('='*30)

# 인덱싱을 더한게 슬라이싱이라고 보면될 듯 
# var[:4] = (var[0] + var[1] + var[2] + var[3])

# 인덱싱, 슬라이싱 고급스킬 
var = "인덱싱, 슬라이싱 고급스킬"
print(var[-1])
print(var[-2])
print(var[3:-2])
print('='*30)

# 인덱싱과 슬라이싱을 할 때 (-)값을 주면 처음부터가 아닌 마지막을 의미 => -0은 존재 안하기 때문
var = "범위를 벗어나면?"
#print(var[20])

err = """
아래와 같은 인덱스 에러 발생  
IndexError: string index out of range
"""
print(err)
print('='*30)

# Split을 이용해서 문자열 나누기
var = "split을 이용해서 문자열 나누기"
print(var.split())

var1 = "split을 이용해서! 문자열 나누기"
print(var.split('!'))
print('='*30)

# 문자열의 다양한 함수 
var = "i love you"
print('대문자로 >>> ',var.upper())
var = "YOU LOVE ME"
print('소문자로 >>>',var.lower())
print('='*30)

# 문자열 개수 
print('YOU LOVE ME : 몇글자인가요? >>>',len(var))
print('='*30)

# 공백제거
var1 = "     공백 제거     "
print('우측 공백 =>',var1.rstrip())
print('좌측 공백 =>',var1.lstrip())
print('좌우측 공백 =>',var1.strip())
print('='*30)

# 문자열 포맷팅 
var1 = 'I am' +' '+'사랑이'
print('문자열 연산 >>> ', var1)
var1 = "i am {name}".format(name = '사랑이')
print('format()사용 >>>', var1)

new = "i am {0} i love {name}".format("제리", name ='사랑이') 
print(new)
print('='*30)

# 문자열 + 연산의 단점 => 타입에러 
# 타입에러 해결법 
age = 30
var1 = 'my age '+ str(age)
print(var1)
var2 = 'my age {0}'.format(age)
print(var2)
print('='*30)

# Tip
txt= """
'format()을 사용하면 굳이 str()을 사용하지 않고 숫자형과 문자형을 합칠 수 있다.'
"""
print(txt)
print('='*30)

# 리스트 
txt = """
 파이썬의 연속된 데이터를 표현하기 위해서 리스트형이라는 자료형을 사용  
"""
print(txt)
print('='*30)

var = list([1,2,3,4,5])
print(var)
var = [1,2,3,4,5]
print(var)
print('='*30)

# 리스트로 인덱싱, 슬라이싱하기
var = [1,2,"3",4,5]

print(var[0])
print(var[1])
print('여러가지 타입의 자료형 가능 >>>',var[0:4])
print('='*30)

# join을 이용하여 리스트를 문자열로 만들기 
a = ['가','나','다','라 ','마' '바','사'] 
b = '.'.join(a)
print(b)
print('='*30)

# 88page