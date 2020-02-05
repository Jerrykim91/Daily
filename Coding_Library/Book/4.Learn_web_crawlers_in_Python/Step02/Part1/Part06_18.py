# Part06_18.py
# import 
import requests as rq


# 실습 Part06_01 - 17
# 인코딩 확인 
url = "http://pjt3591oo.github.io"

res = rq.get(url, params = {"key1":"value1", "key2":"value2"})

print(res.url)

# 첫번째 인자 url = "http://pjt3591oo.github.io"
# 두번째 인자부터는 params 담아 쿼리스트링으로 만들어서 요청보냄
