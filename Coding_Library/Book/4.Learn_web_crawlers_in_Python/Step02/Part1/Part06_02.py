# Part06_02.py
# 여기서는 실행이 안된다 당황;;

# requests 모듈 설치 
# !pip install requests

# import 
import requests as rq


# 실습 Part06_01 - 2
# get 요청- 2 
url = "http://pjt3591oo.github.io"

rq.post(url)

# requests GET과 POST로 요청을 보낼수 있음 
# GET을 보낼 때 => requests.get()
# POST로 보낼 때 => requests.post()
