# ExamGradeProgram_ver_01.py


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


# Step00. 사용자에게 값을 입력 받아야 한다 -> input() 사용
# # 과목, 점수, 취득학점
User_input_name   = input('과 목 명 :')
User_input_score  = input('점    수 :')
User_input_grader = input('취득학점 :')


# 만점이 몇점인지 묻는다
log_txt = {
    'calculating_way':'몇점 만점인가요? \n 1. 4.5점 \n 2. 4.3점 \n 입력하시오 :',
        } 


Grader_calculate = input(log_txt['calculating_way'])
# print(type(Grader_calculate)) # str


# func_loof
def func_loof(case):
    f_loop = [gdr for gdr in case ]
    for num in range(len(f_loop)):
        if User_input_score == f_loop[num]:
            print(f_loop[num], case[f_loop[num]])

    return f_loop[num], case[f_loop[num]]

# func_loof(score_case1)



# 다중 조건문
if Grader_calculate == '1':
    print('='*50,'\n',str(4.5)+'점')
    func_loof(score_case1 )

elif Grader_calculate == '2':
    print('='*50,'\n',str(4.3)+'점')
    func_loof(score_case2 )



# ======
# 본문

def main():pass

if __name__ == '__main__':
    main()

# 수정 해야하는거 
# 취득 학점을 입력한 경우 =>  get 한 학점 / 총학점 아닌가 ? 
#  