# 자료구조와 알고리즘 강의 
#  6~7강_ 배열과 파이썬 

# 꼭 알아둬야 할 자료구조 : 배열(Arrawy)
# -  데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# -  파이썬에서는 리스트 타입이 배열 기능을 제공

## 1. 배열이 왜 필요할까?
# - 같은 종류의 데이터를 효율적으로 관리하게 하기 위해 사용 
# - 같은 종류의 데이터를 순차적으로 저장

# 연관된 공간에 저장가능하고 데이터에 맞게 인덱스를 부여 
# => 연결된 데이터의 일부분에 바로 접근 

    # 장점
    # - 배열은 빠른 접근이 가능 

    # 단점 
    # - 연관된 데이터의 추가가 힘들다 
    # - 데이터가 가변적이라 삭제를 하게 되면 데이터가 손상된다. 
    # 그래서 데이터 삭제가 어렵다. 

## 2. 배열 with 파이썬 

# > c언어로 배열을 표현       
# ``` C
#     #include<stdio.h>

#     int main(int argc, char*argv[])
#     {
#         # 3개의 공간을 지정 
#         char country[3] ="US";
#         printf("%c%c\n", country[0],country[1]);
#         printf("%s\n", country);
#         return 0;
#     }
# ```
# - C언어는 배열의 사이즈를 미리 정한다. 

country = "US"
print(country)

# 내부정으로 배열을 쓰는데 c언어처럼 배열의 길이를 지정하지 않는다. 
country = country + 'A'
print(country)

data = [1, 2, 3, 4, 5]
# list(range(1,6))
print(data)
#>>>[1, 2, 3, 4, 5]

# 2차원 배열 : 리스트로 구현시 
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)
# >>> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#1차원 데이터의 접근 
print(data[0])
#>>> [1, 2, 3]

print(data[0][0])
print(data[0][1])
print(data[0][2])
print(data[1][0])
#>>> 1
#>>> 2
#>>> 3
#>>> 4

## 3. 프로그래밍 연습 
#### 연습 01 : 위의 2차원 배열에서 9,8,7 순서로 출력해보기 
print(data[2][2],data[2][1],data[2][0])
# >>> 9 8 7


#### 연습 02 : 다음 dataset에서 전체 이름안에 M이 몇번 나왔는지 빈도수 출력하기

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

# 어떻게 다음 dataset의 전체 이름안에서 M이 몇번 나왔는지 빈도수를 출력할것인가 
# 5분 고민 해보기 

# for문이 돌때마다 이름을 확인해서 M의 여부를 확인 
# 좋다 근데 어떻게 ''묶여있는 이름안에 M이있는지 확인할것인가 ? 
# 여기까지는 접근했어 근데 M인지아닌지는 어떻게 ?
print('dataset[0]자리 =',dataset[0], '\ndataset[0][1]자리 =',dataset[0][1])
# >>>  dataset[0]자리 = Braund, Mr. Owen Harris 
# >>>  dataset[0][1]자리 = r

for index in range(len(data)):
    print(index)
data[index]


# 데이터셋 안의 데이터를 포문을 돌려 나열한다 
# 그리고 또 포문을 돌리는데 데이터 길이의 인덱스를 나열하는데 
# 출력은 포문을 돌려 만든 인덱스의 숫자와 데이터의 인덱스와 매치되는 글자를 보여준다. 
for data in dataset:
    for index in range(len(data)):
        print(data[index])

m_count= 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count+=1
print(m_count)
