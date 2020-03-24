# ExamGradeProgram.py
# ver_01



# class_code = {
#     103 : ['문학',float(3)],

# }

# 과목명을 수치화해서 입력 => class_code 
class_code = {
    # 과목 코드 : ['과목명', 학점] 
    100 : ['문학'      , float(3)],
    101 : ['비문학'    , float(3)],
    102 : ['선형대수'  , float(3)],
    103 : ['확률과통계', float(3)],
    104 : ['논리학'    , float(3)],
    105 : ['가정의학'  , float(2)], 
    106 : ['언어의이해', float(2)], 
    107 : ['토익실전'  , float(2)],
    108 : ['정역학'    , float(3)],
    109 : ['공업수학'  , float(3)]
}


# print(class_code[103])

# 변수 
score_case1 = {
    'A+' : '4.5',
    'A'  : '4.0',
    'A-' : 'X' ,
    'B+' : '3.5',
    'B'  : '3.0',
    'B-' : 'X'  , 
    'C+' : '2.5', 
    'C'  : '2.0',
    'C-' : 'X',
    'F'  : '0'  }

# print(score_case1['X'])
score_case2 = {
    'A+' : '4.3',
    'A'  : '4.0',
    'A-' : '3.7',
    'B+' : '3.5',
    'B'  : '3.0',
    'B-' : '2.7', 
    'C+' : '2.5',
    'C'  : '2.0',
    'C-' : '1.7',
    'F'  : '0'  }

# func_loof
def func_loof(case):
    f_loop = [gdr for gdr in case ]
    for num in range(len(f_loop)):
        if User_input_score == f_loop[num]:
            if score_case1.values() == 'X':
                print('False') 
            else:
                continue
            print(f_loop[num], case[f_loop[num]])

    return f_loop[num], case[f_loop[num]]

# func_loof(score_case1)

# Step00. 사용자에게 값을 입력 받아야 한다 -> input() 사용
# 과목, 점수, 취득학점
# User_input_name   = input('과 목 명 :')
User_input_score  = input('점    수 :')
User_input_grader = input('취득학점 :')


# 만점이 몇점인지 묻는다
log_txt = {
    'calculating_way':'몇점 만점인가요? \n 1. 4.5점 \n 2. 4.3점 \n 입력하시오 :',
        } 
Grader_calculate = input(log_txt['calculating_way'])
# print(type(Grader_calculate)) # str


# 다중 조건문
if Grader_calculate == '1':
    print('='*50,'\n',str(4.5)+'점')
    func_loof(score_case1 )

elif Grader_calculate == '2':
    print('='*50,'\n',str(4.3)+'점')
    func_loof(score_case2 )

# 1개짜리 계산함수 생성 
def test():pass
    # 사용자로 부터 값을 받아온다 
        # 교과코드(과목 코드 : ['과목명', 학점] )
    # 계산 방식을 정한다 
    # 방식에 따라 연산한다. 
    # 사용자에게 연산 내용을 돌려준다 
    # 받아야 하는것

    # 1. 
    # 2. 

# return 





# class_code = {
#     '100' : '문학',
#     '101' : '비문학',
#     '102' : '선형대수' ,
#     '103' : '확률과통계',
#     '104'  : '논리학',
#     '105' : '가정의학'  , 
#     '106' : '언어의이해', 
#     '107'  : '토익실전',
#     '108' : '정역학',
#     '109'  : '공업수학'
# }