# Part06_18.py
# import 
import requests as rq


# 실습 Part06_01 - 18
# 쿼리스트링 생성 - 1
url = "http://pjt3591oo.github.io"

res = rq.get(url, params = {"key1":"value1", "key2":"value2"})

print(res.url)

# 첫번째 인자 url = "http://pjt3591oo.github.io"
# 두번째 인자부터는 params 담아 쿼리스트링으로 만들어서 요청보냄

# 딕셔너리를 이용하면 특수문자를 직접 다루지 않기 때문에 코드 유지보수에 있어 버그나 에러가 발생할 확률이 줄어듬