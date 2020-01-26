# Part06_08.py
# 여기서는 실행이 안된다 당황;;

# import 
import requests as rq


# 실습 Part06_01 - 8
# 헤더 가지고 오기 
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)
print(res.status_code)