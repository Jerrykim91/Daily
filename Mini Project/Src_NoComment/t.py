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

# User_input_score  = input('점    수 :')
# User_input_grader = input('취득학점 :')

User_input_score = 'A-'
# func_loof
def func_loof(User_input_score ,case = score_case1): 
    f_loop = [gdr for gdr in case ]
    # print(f_loop)
    # Run = True
    # while Run :
    for num in range(len(f_loop)):
        # print(num)
        # print(User_input_score)
        # print('get num')
        if User_input_score == f_loop[num]:
            # print( case[f_loop[num]])
            # print('match')
            if case[f_loop[num]] == 'X':
                print('False')
            else:
                continue
                # Run = False
        
    return f_loop[num], case[f_loop[num]]     
        
        # break
                # print(f_loop[num], case[f_loop[num]])
    
    # return f_loop[num], case[f_loop[num]]

func_loof(User_input_score)