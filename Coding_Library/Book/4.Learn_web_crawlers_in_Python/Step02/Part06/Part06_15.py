# Part06_15.py

# import 
import requests as rq


# 실습 Part06_01 - 15
# HTML 코드 가지고 오기 
url = "http://pjt3591oo.github.io"

res = rq.get(url)

print(res.text)

# text속성을 이용하면 html을 가지고 올 수 있음 
# 보다 나은 방법을 다음 실습으로 구현 