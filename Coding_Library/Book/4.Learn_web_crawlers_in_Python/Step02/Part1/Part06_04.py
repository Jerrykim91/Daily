# Part06_04.py
# 여기서는 실행이 안된다 당황;;

# requests 모듈 설치 
# !pip install requests

# import 
import requests as rq


# 실습 Part06_01 - 4
# 응답 코드 가지고 오기 
url = "http://pjt3591oo.github.io"

res = rq.get(url)

print(res)
print(res.status_code)
# status_code 속성을 통해 응답코드를 확인가능 
