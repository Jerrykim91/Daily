# Part06_14.py

# import 
import requests as rq


# 실습 Part06_01 - 14
# header와 cookies 속성 비교
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = list(res.cookies)
print(cookies)
headers_cookies = res.headers['Set-Cookie']

print('cookies 속성')
print(dict(cookies))

print('')

print('header 속성')
print(headers_cookies)

# cookies 속성이 header 속성보다 쿠키 값의 정보를 더 자세히 볼 수 있음 
# name단위로 구분 지어져 있어 header 보다 자세함 