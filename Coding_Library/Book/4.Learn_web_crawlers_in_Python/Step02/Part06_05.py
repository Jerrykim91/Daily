# Part06_05.py
# 여기서는 실행이 안된다 당황;;

# import 
import requests as rq


# 실습 Part06_01 - 5
# 없는 페이지 응답 코드 확인 
url = "http://pjt3591oo.github.io/a"

res = rq.get(url)

print(res)
print(res.status_code)
# >>> 404 출력 

# 응답 코드 404는 찾을 수 없다는 의미 
# 존재하지 않는 URL에 접속하여 해당 페이지에 접속이 불가능할 때 반환하는 코드
   
