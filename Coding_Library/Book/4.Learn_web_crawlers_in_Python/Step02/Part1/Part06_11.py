# Part06_11.py

# import 
import requests as rq


# 실습 Part06_01 - 11
# 쿠키 가지고 오기 - 2
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = res.cookies
print(list(cookies))

# 리스트 타입으로 변환 후 출력 => 타입 변환 가능 