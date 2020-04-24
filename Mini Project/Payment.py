# 급여 계산기 

'''
<< 급여계산 프로그램 >>
 시급을 입력해주세요
 일일 근무 시간 : 
 한달 근무 시간 : 

수습을 적용하나요?
1. 적용 
2. 미적용 

예상 월급 : 입니다. 

예상월급으로 할 수 있는일

PC방 (시간당 1200원 기준 ) :
점심 (한끼당 7000원 기준 ) :
영화 (한편당 11000원 기준) :
노래방( 20000원 기준 )     :

'''

# 1. 인풋 
Practice = input(" \n 1. 수습 적용 \n 2. 수습 미적용 ")

PerHour = input('시급을 입력해주세요')
DayTime = input('일일 근무 시간 :')
MonthTime = input('한달 근무 일 수 :')

payment = PerHour * DayTime * MonthTime
if Practice == 1 : 
    # 90 %
    Practice_pay = payment // 10
    print(Practice_pay)
else:
    payment








