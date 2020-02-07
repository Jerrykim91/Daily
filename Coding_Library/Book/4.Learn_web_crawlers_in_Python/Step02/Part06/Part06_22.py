# Part06_22.py
# import 
import requests as rq
import json


# 실습 Part06_01 - 22
# json모듈과 str의 차이

url = "http://www.example.com"

dict1 = {'key1':'value1', 'key2':'value2'}
dict2 = {"key1":"value1", "key2":"value2"}


print(json.dumps(dict1))
print(str(dict1))

print(json.dumps(dict2))
print(str(dict2))

# json모듈과 str의 차이를 확인 해봄
# 큰차이는 없음 => 문자열 작성시 " ",' ' 을 사용 
# 딕셔너리 형태를 유지하려면 작은 짜옴표가아닌 큰 따옴표로 키와 벨류값을 표현해야함 
# 그렇기 때문에 json.dumps()확인하여 딕셔너리를 문자열로 바꾸어 사용 