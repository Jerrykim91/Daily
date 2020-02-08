# Part06_25.py
# import 
import requests as rq


# 실습 Part06_01 - 25
# requests 발생시 오류 발생
url = "blog.naver.com/pjt3591oo"

res = rq.get(url)

# http를 명시하지 않으면 missingSchema 에러 발생