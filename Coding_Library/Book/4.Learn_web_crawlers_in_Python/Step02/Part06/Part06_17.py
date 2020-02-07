# Part06_17.py

# import 
import requests as rq


# 실습 Part06_01 - 17
# 인코딩 확인 
url = "http://pjt3591oo.github.io"

res = rq.get(url)

print(res.encoding)

# encoding 속성으로 인코딩을 확인가능 
# meta태그는 웹 페이지의 메타정보뿐 아니라 인코딩 정보도 포함 
