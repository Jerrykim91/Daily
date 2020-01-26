# Part06_08.py

# import 
import requests as rq


# 실습 Part06_01 - 8
# 특정한 값 가지고 오기 
url = "https://blog.naver.com/pjt3591oo"

res = rq.get(url)

# 스테이트_코드 출력 
print(res)

headers = res.headers
# Set-Cookie 이용 => 설정된 쿠키값을 확인 
print(headersp['Set-Cookie'])

# 쿠키는 매우 유동적으로 바뀜
# 쿠키값 내부의 expires => 쿠키 만료 기간 
