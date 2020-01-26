# Part06_03.py
# 여기서는 실행이 안된다 당황;;

# requests 모듈 설치 
# !pip install requests

# import 
import requests as rq


# 실습 Part06_01 - 3
# 응답 결과 
url = "http://pjt3591oo.github.io"

res = rq.get(url)
print(res)
