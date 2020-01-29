# Part06_10.py

# import 
import requests as rq


# 실습 Part06_01 - 10
# 쿠키 가지고 오기 - 1 
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = res.cookies
print(cookies)

# 쿠키는 해드 속성에 접급하지 않고 cookies 속성에서 가지고 올수 있음 
