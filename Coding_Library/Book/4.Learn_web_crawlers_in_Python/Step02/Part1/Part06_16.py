# Part06_16.py

# import 
import requests as rq


# 실습 Part06_01 - 16
# HTML 코드 가지고 오기 
url = "http://pjt3591oo.github.io"

res = rq.get(url)

print(res.content)

# content속성을 text 처럼 html코드를 가지고 오는데 한글을 바이너리 형태(인코딩)로 가지고 옴 
# 한글이 깨지는 현상이 있기 때문에 바이너리로 변경하는 것 => 한글을 코드화 시켜서 가지고 옴 
# 크롤링시 인코딩 문제가 생길 경우에 주로 이용 