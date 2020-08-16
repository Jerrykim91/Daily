# 2019.12.18 <ver_1>
# [실습]
# 3-7단까지만 구구단을 출력하시오 
# 출력 형식은 3x1 = 3 ... 한줄에 하나씩 
print('2019.12.18 <ver_2>')
print('-'*40)
# 배열이용 
# used array ----------------------------
a = [3,4,5,6,7]
for i in a:
    print('%d단'%i)
    for j in range(9):
        j=j+1
        print(i ,'x', j ,'=',i*j)
#----------------------------------------
### 문제점 : range()  잘 못다룬다 
print('-'*40)
# tuning --------------------------------
a = [3,4,5,6,7]
for i in range(3,8):
    print('%d단'%i,'\n','='*30 )
    for j in range(1,10):
        print(i ,'x', j ,'=',i*j)
#----------------------------------------
print('-'*40)
# tuning --------------------------------
for i in range( 3, 8 ):
    print( '%d단'%i,'\n','='*30 )
    for j in range( 1, 10 ):
        print( '%s x %s = %2s'% (i,j,i*j))
#----------------------------------------
print('-'*40)
# tuning --------------------------------
# 결과를 먼저 쓰고 내용을 확인하는 ?
['%s x %s = %2s' % (i,j,i*j) for i in range(3,8) for j in range(1,10)]
#----------------------------------------
print('-'*40)
print('5단만 제외하고 작업 (긍정)')
# 5단만 제외하고 작업 (긍정)
# tuning --------------------------------
results = []
for i in range( 3, 8 ): 
    if i == 5:
        #print(int(i.pop())
        continue
    #print( '%d단'%i,'\n','='*30 )
    for j in range( 1, 10 ):
        results.append(i*j)
print(results)#  프린트로 찍으면 옆으로  
print('총 개수:', len(results))

#----------------------------------------
print('-'*40)
print('5단만 제외하고 작업 (부정)')
# 5단만 제외하고 작업 (부정)
# tuning --------------------------------
results = list()
for i in range( 3, 8 ): 
    if i != 5:
        for j in range( 1, 10 ):
            results.append(i*j)
print(results,'\n총 개수:', len(results))
# tuning --------------------------------
print('== python 방식_ 리스트 내포 ==')
a = [(i*j) for i in range( 3, 8 ) if i != 5 for j in range( 1, 10 )]
print(a,'\n총 개수:',len(a))
#----------------------------------------
print('-'*40)