# Part06_21.py
# import 
import requests as rq
import json


# 실습 Part06_01 - 21
# json모듈을 이용한 post 요청 

url = "http://www.example.com"

res = rq.post(url, data = json.dumps({"key1":"value1", "key2":"value2"}))

print(res.url)

# 20.py와 결과는 같다
# 하지만 data를 딕션너리에서 문자열로 바꾸어 보냈다. 
# json.dumps을 이용하면 딕셔너리의 형태를 유지하면서 문자열로 바꾸어 준다. 