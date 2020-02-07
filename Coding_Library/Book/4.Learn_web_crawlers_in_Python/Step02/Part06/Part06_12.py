# Part06_12.py

# import 
import requests as rq


# 실습 Part06_01 - 12
# 쿠키 가지고 오기 - 3
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = res.cookies
print(tuple(cookies))

# 튜플로 출력 