# Part06_20.py
# import 
import requests as rq


# 실습 Part06_01 - 20
# post 요청 

url = "http://www.example.com"

# res = rq.get(url, params = {"key1":"value1", "key2":"value2"}) # 비교용 
res = rq.post(url, data = {"key1":"value1", "key2":"value2"})

print(res.url)

# POST를 요청할때  url이 없고 헤더에 바디에 포함되기 때문에 반드시 추가적인 인자가 필요 
# 쿼리스트링은 params를 사용
# body 데이터에 추가 할때는 data를 이용 

# data 키워드를 이용해서 post 이용시 데이터를 포함에서 가능 
# 출력을 보면 data = dict()로 제대로 전달이 안됨 