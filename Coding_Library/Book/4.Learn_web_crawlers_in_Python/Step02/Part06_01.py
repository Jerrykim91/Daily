# Part06_01
# 여기서는 실행이 안된다 당황;;

# requests 모듈 설치 
# !pip install requests

# import 
# import requests 
import requests as rq

# 실습 Part06_01 -1

url = "http://pjt3591oo.github.io"

res = rq.post(url)
print(res)

# requests 요청 후 응답 객체를 반환 => print(응답코드) => 확인가능


