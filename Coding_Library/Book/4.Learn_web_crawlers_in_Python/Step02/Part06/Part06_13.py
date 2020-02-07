# Part06_13.py

# import 
import requests as rq


# 실습 Part06_01 - 13
# 쿠키 가지고 오기 - 4
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = res.cookies
print(dict(cookies))

# 딕셔너리 형태로 출력 
# 딕셔너리 형으로 변환할 경우 쿠키에 있는 name과 value를 
# name : value 형태로 만듬 
