
# 2019.12.18 <ver_1>

# base ------------------------------
print('2019.12.18 <ver_1>')
print('-'*40)
a = [1,2,3,4,5]
while len(a) > 0:
    print(a.pop())
    print('반복작업')
print('-'*40)
#------------------------------------

# 2019.12.18 <ver_2>

# tuning ----------------------------
print('2019.12.18 <ver_2>')
print('-'*40)
a = [1,2,3,4,5]
while len(a) > 0 :
    print('조건을 확인하고 참이면 내려온다.')
    print('[0] 현재 멤버수', len(a))
    print(a.pop())
    print('[1]현재 멤버수 ', len(a))
   # print('-'*20)
#------------------------------------
print('-'*40)
print('2019.12.18 <ver_2_test>')
print('-'*40)
a = [1,2,3,4,5]
while a: 
    print('조건을 확인하고 참이면 내려온다.')
    print('[0] 현재 멤버수', len(a))
    print(a.pop())
    print('[1]현재 멤버수 ', len(a))
    #print('-'*20)
#------------------------------------
print('-'*40)
print('2019.12.18 <ver_2_test_2>')
print('-'*40)
a = [1,2,3,4,5]
while a :
    print(a.pop())
else:
    print('잘돌았다. 중단없이 종료')
#------------------------------------

# 2019.12.18 <ver_3>

# tuning ----------------------------
print('-'*40)
print('2019.12.18 <ver_3>')
print('-'*40)
Done = False 
a = [1,2,3,4,5]
while not Done:
    if len(a)> 0 :
        #print(a.pop())
        print(a.pop(),'반복작업')
    else:
        len(a) == 0
        print('끝')
        break
    Done
print('-'*40)
#------------------------------------