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

# 중첩된 리스트 
a = [1,2,3,4,5,[6,7,8,9]]

print(a)
print(a[3])
print(a[5][1])
print(a[5][2])
print(a[-2])

print(a[-1]) # [-1] = [6,7,8,9]
print(a[-1][0]) # [-1] 중에 처음꺼 => 6
#print(a[-2][0]) => 에러 

print('='*30)

# 리스트 연산 
# 리스트도 연산을 제한적으로 사용가능하다 

var1 = [1,2,3,4,5]
var2 = [6,7,8,9,10]
num = 3
# 리스트 * 숫자형 : 리스트 반복하기 
print(var1*num)
# 리스트 + 리스트 : 리스트 합치기 
print(var1+var2)
print('='*30)


# 리스트 수정, 삭제 
# 인덱싱과 슬라이싱을 이용해서 리스트를 수정 또는 삭제 할수 있음 

# 인덱싱을 이용해 리스트 수정 
var1 = [1,2,3,4,5]
print('수정 전  >>>',var1)
var1[2] = 10
print('수정 후1 >>>',var1)
var1[3] = [11,22,33]
print('수정 후2 >>>',var1)
print('='*30)

# 슬라이싱을 이용해 리스트 수정 
var1 = [1,2,3,4,5]
var2 = [1,2,3,4,5]
print('수정 전  >>>',var1)
var1[2:4] = [0,-1]
print('수정 후1 >>>',var1)
var2[2:4] = [0,-1,-2]
print('수정 후2 >>>',var2)
print('='*30)


# 리스트 요소 삭제 
# 두가지 1. 인덱스=> del 2. 슬라이싱=> [](해당범위를 삭제)
var1 = [1,2,3,4,5]
var2 = [1,2,3,4,5]

del var1[1]
var2[0:3] = []
print('수정 후1 >>>',var1)
print('수정 후2 >>>',var2)
print('='*30)


# 리스트 요소 추가하기 
var = [1,2,3,4,5]
var.append(10)
print(var)
# append()는 마지막에 요소를 추가 
var.append(20)
print(var)
print('='*30)


# 리스트 요소 제거 - 1 
var = [1,2,3,4,5]
print(var.pop())
print(var)

# 리스트 요소 제거 - 2 
var = [1,2,3,4,5, 1,2,3,4,5]
print(var.remove(4)) # None : pop()와 다르게 제거된 값을 변환시켜주지 않았기때문 
print(var) # 요소에서 4만 제거 
print('='*30)

# 리스트 정렬 - 1 
var = [3,5,4,1,2,6,9,7,8]
var.sort()
print(var)
var.sort(reverse=True)
print(var)
print('='*30)

# 리스트 정렬 - 2 
var = ['a','d','c','b']
var.sort()
print(var)
var.sort(reverse=True)
print(var)
print('='*30)

# 리스트 정렬 - 3 
# 대문자 우선 정렬 
var = ['A','d','c','b']
var.sort()
print(var)
var.sort(reverse=True)
print(var)
print('='*30)

# 리스트 정렬 - 4
var = [ 75,'d','A',99,100]
#print(var.sort()) # 타입에러 발생 => 하나의 타입으로 통일 필요 
print('='*30)

# 리스트 길이 
var = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(var))
print('='*30)

# 딕셔너리 => 중괄호로 감싸서 표현  => 키와 값의 형태로 데이터를 저장 
# 키로 접근할때는 리스트처럼 대괄호가 아닌 키값을 이용해 접근  
# => 존재하지 않는 키에 접근하면 에러 발생 
var1 = dict({"key1":"vark1","key2":"vark2"})
var2 = {"key1":"vark1","key2":"vark2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])
print('='*30)

# 딕셔너리에 키 추가하기 => get()함수 이용
var = {"key1":"varl1"}
print(var.get('key1'))
print(var.get('key1','default value'))
print(var.get('key2')) # 키는 있지만 값은 없어서 None
print(var.get('key2','default value'))
print('='*30)

# 키(key) - 값(value) 생성 
# 딕셔너리도 리스트처럼 데이터를 추가 
var = {}
print(var)
var["key1"] = 10
print(var)
var["key1"] = 20
var["key2"] = 30
print(var)
print('='*30)

# 키(key) - 값(value) 생성 - 2 
# setdefault() 함수 사용 
var = {}
print(var)
var.setdefault('key1',10)
print(var)
var.setdefault('key1',20)
var.setdefault('key2',30)
print(var)
print('='*30)


# key 리스트 만들기
var2 = {"key1":"vark1","key2":"vark2","key3":"vark3"}
print(var2.keys())
# value 리스트 만들기 
print(var2.values())
# 페어로 리스트 만들기 
print(var2.items())

print('='*30)

# items()함수를 이용하면 (키,값)의 형태로 리스트처럼 만들어 줌 
# => 튜플이라고 하는 자료형태에 담겨서 출력
# keys(),values(),items() 는 리스트가 아님 => 인덱싱이나 슬라이싱은 불가능 
# 하지만 반복문은 돌릴수 있고 이를 이터레이터라고 표현 
# 만약 list()로 타입을 변경한다면 인덱싱이나 슬라이싱 가능 

# 딕셔너리 함수로 만든 리스트 인덱싱 -1
var2 = {"key1":"vark1","key2":"vark2","key3":"vark3"}
values = var2.values()
print(values)
# print(values[0]) #  타입에러 발생 => 리스트가 아니라서 

# 딕셔너리 함수로 만든 리스트 인덱싱 -2 (형변환해서 출력)
values = list(var2.values())
print(values)
print(values[0])


# 키 존재 유무 검사 
# 키 확인 
var2 = {"key1":"vark1","key2":"vark2","key3":"vark3"}
print('keys' in var2)
print('hi' in var2)
#[키 in 딕셔너리 변수]의 형태로 코드를 작성 
# => 존재하면 참 아니면 거짓을 반환
print('='*30)

# 튜플 
# 리스트와 흡사하지만 []가 아닌 ()를 사용
# 튜플은 수정하거나 삭제 할수 없음 => 변경의 제약 
var1 = tuple((1,))
var2 = tuple((1,2,3))
var3 = (1,)
var4 = (1,2,3)
print(var1)
print(var2)
print(var3)
print(var4)
print('='*30)

# 튜플생성
var1 = (1)
# 튜플생성시 요소가 하나일 경우 반드시 콤마를 붙여 줘야한다. 
# 붙이지 않으면 튜플이 아닌 정수나 문자열로 출력 !  
print(var1)
print('='*30)

# 튜플은 변경 삭제가 불가능하다 
# 튜플 - 인덱싱 
var = (1,2,3,4,5)
print(var[3])
# 튜플 - 슬라이싱
print(var[2:])
print('='*30)

# 연산 + , * 
var1 = (1,2,3)
var2 = (4,5)
print(var1)
print(var2)
print(var1+ var2)
print(var1*3)
print(var2*3)
print('='*30)

# 사칙 연산자
var1 =  1
var2 =  5
var1 += var2
print(var1)
print('='*30)

# 비교연산자 
print('False and False =', False and False)
print('False and True = ', False and True)
print('True and False =', True and False)
print('True and True =', True and True)
# 각각을 비교하기때문에  True and True 연산 
print(1 < 2 and 2 > 1)
# ()로 구분해서 좀 더 명확하게 확인 
print((1 > 2) and (2 > 1))
print('='*30)

# OR 연산
print('False or False =', False or False)
print('False or True =', False or True)
print('True or False =', True or False)
print('True or True =', True or True)
print(1 < 2 or 2 > 1)
print((1 > 2) or (2 > 1))
print('='*30)

# NOT 연산 
print(not False)
print(not True)
print(not 1)
print(not 2)
print(not 2 > 1)
print(not 1 > 2)
print('='*30)


# 조건 분기 if 문 
condition_good = True
condition_NG = False

if condition_good :
    print('hi')
    print('it works')
if condition_NG : 
    print('HI')
    print("it doesn't work")

print('Read all')
print('='*30)

# 조건 응용 분기 if ~ else
condition_s = True
condition_m = True
condition_l = True

if condition_s :
    print('조건1') # True
elif condition_m:
    print('조건2') # 이 아이만 True 일때

elif condition_l:
    print('조건3') # 이 아이만 True 일때

else:
    print('조건4') # 전부 False 일때 출력
print('='*30)


# 포함 여부에 따른 조건 분기 
if 'h' in 'hellow world':
    print('hellow world에 h가 포함 되어있습니다')
if 1 in [11,22,33,44,55,66]:
    print('[11,22,33,44,55,66]에 1이 포함 되어있습니다')
print('='*30)

# 반복문 
# while문을 이용한 반복문 
count = 0 
while count < 5 :
    print('%d 번째' %(count))
    count += 1 #  이거 안적어주면 무한루프에 빠짐 
print('='*30)

# for 문을 이용한 반복문 
# 2가지 방법으로 만들수있음 
# 1. range()를 이용해서 만듬 
# => 첫번째 인자부터 -1까지 반복 range(0,10) =>0 to 9까지
# 2. 라스트, 문자열과 같은 데이터 타입으로 반복문을 만들수 있음 

for i in range(0,5):
    print('%d  번째'%(i))
print('='*30)

# 문자열을 이용한 반복문 
for i in 'hello world':
    print(i)
print('='*30)
   
# 리스트를 이용한 반복문  
for i in [11,22,33,44,55,66] : 
    print(i)
print('='*30)

# 딕셔너리를 이용한 반복문
var = {"key1":"varl1","key2":"varl2","key3":"varl3"}

for key in var :
    print(key)
    print(var[key])

print('='*30)

# for문을 이용한 간단한 프로그램(구구단)
for i in range(2,5):
    for j in range(2,5):
        print('%d x %d = %d'%(i,j,i*j))
print('='*30)

# 문자열 빈도수 출력(중요)
BTS = """
According to the Gaon Music Chart, BTS has sold sixteen million albums domestically 
in physical sales and is the best-selling artist to debut in the 2010s.
They hold the best-selling album in Korean history with Map of the Soul: Persona. 
BTS were the second best-selling artists of 2018 worldwide according to the IFPI's Global Artist Chart, 
as well as the only non-English speaking artist to enter the chart. 
The group has won Top Social Artist three years in a row and Top Duo/Group at the 26th Billboard Music Awards. 
Featured on Time's international cover as "Next Generation Leaders", 
BTS has appeared in the magazine's 25 most influential people 
on the internet (2017–2019) and Time's 100 most influential people in the world (2019). 
Forbes Korea named BTS the most influential celebrities of Korea in 2018, 
and BTS ranked 43rd in the Forbes Celebrity 100 (2019) as one of the world's top-earning celebrities. 
BTS are ranked #4 of Billboard's Top Social Artist of the 2010s, and are the highest group on the list. 
During their Love Yourself World Tour, 
BTS became the first Asian and first non-English speaking act to headline and sell out Wembley Stadium; 
and broke the record for the single highest-grossing engagement in Rose Bowl Stadium history. 
Billboard ranked BTS at #45 on their Top Touring Artists of the 2010s list, 
being the highest-ranked Asian as well as the only non-English speaking act on the list. 
As of 2019, BTS are purportedly worth more than $4.65 billion 
to South Korea's economy each year, or 0.3 percent of the country's GDP. 
BTS attracted one in every 13 foreign tourists that visited 
South Korea and were cited as one of the key acts boosting global music sales to $19 billion in 2018.
"""
print('='*30)
# 정형식을 이용하면 더욱 간단하게 해결 가능
str_freq = BTS.replace(',','').replace('\n','').replace('.','').split(' ')

char_frequency = {}

for char in str_freq:
    char_frequency.setdefault(char, 0)
    char_frequency[char] += 1
print(char_frequency)

# split()는 띄워쓰기 단위로 아누어 단어 리스트를 생성
# 리스트를 이용하여 반복문을 돌린후 
# setdefault() 이용해서 char_frequency에 해당단어가 없다면 단어를 키로 0의 값을 만듬
# 그리고 +1 증가시켜줌 만약 키가있다면 0으로 바뀌지않고 1 증가 됨 
print('='*30)

