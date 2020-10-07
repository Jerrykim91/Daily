<br>

#### 0?. R - R 패키지 정리

<br>

# R 패키지 정리

<br>


## 1. 데이터 로드 

<br>

### 1) `RMySQL, RPostgresSQL, RSLite`

<br>

데이터베이스(DB)로부터 직접 데이터를 읽을 때 사용하는 패키지로     
R[데이터베이스명] `RMySQL`은 `MySQL`의 데이터들을 직접 `R`로 불러올 수 있다. 

<br>

```R
# RMySQL
install.packages("RMySQL") # 설치
library(RMySQL)  # 로딩

# `dbConnect()` 함수는 `MySQL` DB로 연결한한다. 

con <- dbConnect(
  MySQL(),
  user = 'uid',
  password = 'pwd',
  host = '127.0.0.1', # hostname
  dbname = 'test-db' # 연결할 db이름
)
dbSendQuery(con, 'set character set "utf8"') # utf8 지정 
```

<br>

### 2) `XLConnect, xlsx`

<br>

MS사의 엑셀을 R로 직접적으로 읽고 쓰게 가능하다. 

<br>

```R
# :: 불러오기
# XLConnect
install.packages("XLConnect") # 설치
library(XLConnect)  # 로딩
#  2003이하 버전, 2007이상 버전 모두 read 가능하다. 
wb <- XLConnect::loadWorkbook("파일명.xlsx") # 미리 정의 된 Excel 셀 스타일을 자동으로 가지고옴
sheet1 <- XLConnect::readWorksheet(wb, "Sheet1")
```

<br>

### 3) `foreign`

<br>

- SAS, SPSS 데이터셋을 읽어올때 사용한다
    - SAS의 경우 `sas 7bdat` 확장자로 되어있는 파일인데 읽어올 때 `foreign` 패키지를 사용해서 읽어올 수 있다. 

<br>

### 4) 일반적인 텍스트 파일을 로드할 때, R 에서는 별다른 패키지가 필요하지 않다. 

<br>

- `read.csv`, `read.table,` `read.fwf`를 이용하면 된다.
<!-- 이외의 독특한 자신만의 데이터셋을 불러오고 싶다면 CRAN guide에 데이터 `import`, `export`에 관해 문의가능하다.   -->

<br><br>

## 2. 데이터 핸들링 

<br>

### 1) `dplyr`

<br>

데이터 `subsetting`, `summarizing`, `rearranging`, `joining`에 대한 더 쉬운 길을 제공한다. `dplyr` 는 빠른 핸들링을 위하여 반드시 사용하는 패키지이다. 

<br>

### 2) `tidyr`

<br>

- `tidyr`는 데이터셋의 레이아웃을 바꿀 때 유용한 툴이다. 
    - 데이터를 `tidt format`으로 바꾸기 위해 `gather` 이나 `spread` 함수를 사용가능하다. 

<br>

### 3) `stringr`

<br>

- `stringr` 문자열 다루는 것과 정규표현식 관련된 패키지이다. 

<br>

### 4) `lubridate`

<br>

- date와 time을 다루기 쉽게 만드는 툴이다. 

<br><br>


## 3. 데이터 시각화 

<br>

### 1) `ggplot2`

<br>

- R에서 매우 유명한 시각화 패키지로 grammar of graphics를 활용하여 layered, customizable plot을 만들 수 있다는 장점이 있다. 

<br>

### 2) `ggvis`

<br>

- grammar of graphics 기반으로 동작하는, 대화형 웹베이스 그래픽 라이브러리이다.

<br>

### 3) `rgl`

<br>

- 3D 시각화를 위한 라이브러리이다. 

<br>

### 4) `htmlwidgets`

<br>

- 자바스크립트 기반의 시각화를 위한 툴이다. 

<br>

### 5) `googleVis`

<br>

- `R` 에서 데이터 시각화를 위해 구글 차트를 이용 할 수 있게 한다.
- 구글 차트 툴은 `Gapminder` 라고 불린다.

<br><br>


### 4) 데이터 모델링 

<br>

### 1) `car`

<br>

- car 패키지의 Anova 함수는 type2, type3 아노바 테이블을 만드는데 유명하다. 

<br>

### 2) `mgcv`

<br>

<br>

### 3) `lme4 / nlme`

<br>

- 라이너 , 논 라이너 혼합효과모형

<br>

### 4) `randomForest`

<br>

- 머신러닝의 렌덤포레스트 

<br>

### 5) `multcomp`

<br>

- 다중비교를 위한 툴 

<br>

### 6) `vcd`

<br>

- 범주형 변수의 시각화 분석을 위한 툴 

<br>

### 7) `glmnet`

<br>

- Lasso, elastic-net 회귀분석을 cross validation과 함깨 해준다. 

<br>

### 8) `survival`

<br>

- 생존분석

<br>

### 9) `caret`

<br>

- 회귀분석 및 분류 모델의 트레이닝을 위한 툴이다. 

<br>

<br>

---

<br>

## Reference <br>

- R VScode install  &nbsp; : &nbsp;<https://ark1st.tistory.com/7> <br>
- R 패키지 참조  &nbsp; : &nbsp;<https://statkclee.github.io/data-science/data-science-library.html><br>
- 공공데이터  &nbsp; : &nbsp;<https://statkclee.github.io/data-science/data-science-library.html><br>
<br>
<br>

## Practice makes perfect! <br>

<!-- - [내용](주소) -->