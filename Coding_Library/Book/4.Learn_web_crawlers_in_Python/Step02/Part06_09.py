# Part06_09.py

# import 
import requests as rq


# 실습 Part06_01 - 9
# 헤더의 모든 요소 접근 
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

headers = res.headers

for header in headers:
    print(headers[header])

# 헤더의 요소를 확인 가능함 
# 크롤링에서 가장 중요한 부분은 서버에서 쿠키값을 만들어 준 Set-Cookie 파트 