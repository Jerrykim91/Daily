# Part06_19.py
# import 
import requests as rq


# 실습 Part06_01 - 19
# 쿼리스트링 생성 -2 
url = "http://pjt3591oo.github.io//?key2=value2&key1=value1"

res = rq.get(url)

print(res.url)

# 코드를 작성하지 않고 데이터만 보낼경우 
# 이렇게 작성하면 url  코드의 슬래시에 집중해야한다.  
# 코드가 길어지면 누락되거나 추가 되는 경우가 발생할 수 있다. 

