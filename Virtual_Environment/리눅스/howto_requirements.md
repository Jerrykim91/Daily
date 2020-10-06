<br>

# 가상환경 구축 후 버전통일

## 환경구성

### 폴더 생성 

FinalProject 

Emotion (감정분석) 

- README.md

Food_Img (이미지)

- README.md

Food_rec(추천)

- README.md

README.md

requirements.txt

<br>
<br>

## 가상환경 생성

텐서는 두가지 버전으로 진행 해야 할 수 있어서 가상환경을 둘로 나눌께요

추가로 사용하는 페키지 생기면 알려주세요  다같이 추가하거나 버전 바꿀겁니다 

- 가상환경 이름

    - fmfa_m

        - 텐서 1.5

    - fmfa_t

        - 텐서 2

requirements.txt => 기본 + 알파

### 절차

1. 콘다네비게이터에서 가상환경 fmfa_m(기본), fmfa_t생성 <br>
   
    1-1) 가상환경 fmfa_m기반 주피터 설치

2. fmfa_m가상환경에서 open terminal 구동

3. requirements.txt 작업 환경으로 이동 

4. requirements.txt 파일이 존재하는 곳까지 현재 디렉토리 이동

5. terminal에서  `$ conda install --file requirements.txt` 

6. 텐서 플로우는 따로 설치

    ```bash
    $ conda install tensorflow==1.15.0
    $ conda install tensorflow==2.0
    ```

7. conda에 없는 패키지는 제거후 따로 설치
예 )$ pip install pymysql 
    $ pip install folium==0.10.0

산출물 : requirement.txt


```bash

pandas == 1.0.3
requests==2.18.4
beautifulsoup4==4.8.2
numpy==1.18.1
scikit-learn==0.22.1
matplotlib==2.2.2
seaborn==0.10.0

```