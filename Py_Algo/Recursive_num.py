# Recursive

# 100명이 테이블에 착석해야함 
# 1명은 안됨 2명이상만 착석이 가능 

# 박스 
# 가로 : 테이블수 상한 => 10
# 세로 : 테이블에 앉을 사람 상한 => 100

# 10*100 => 1000

#m , n = 10, 100
m= 10
n = 10
# tab_cnt = [0] * (m+1)
# # print(tab_cnt, len(tab_cnt)) # [[1,0*100], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , 11
# for i in range(0, m+1):
#     # print(i) 
#     tab_cnt[i] = [0]*(n+1)
#     # print(tab_cnt[i],len(tab_cnt[i])) # i번수 만큼 한번씩 [0]*101을 출력
#     tab_cnt[i][0] = 1
#     # print(tab_cnt[i],len(tab_cnt[i])) # i번수 만큼 한번씩 리스트의 인텍스 0자리에 1을 할당
# # print(type(tab_cnt))

for i in range(1, m+1):
    # print(i) # 1 ~ 10 
    i = int(i)
    for j in range(2, n+1):
        j = int(j)
        # print(j) #2~ 100까지 순서대로 한번씩 i번 출력 
        # if((i >=2)and(j>=i)): # ??
        #     tab_cnt[i][j] = tab_cnt[i][j-1]
        #     # print(tab_cnt[i][j])
        #     if i > 2 : # ???
        #         tab_cnt[i][j] += tab_cnt[i-1][j]

# print(tab_cnt[8][:])


print(tab_cnt[m][n])

