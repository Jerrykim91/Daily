# Part06_06.py
# 여기서는 실행이 안된다 당황;;

# import 
import requests as rq


# 실습 Part06_01 - 6
# 응답 코드를 활용한 조건분기 
def url_check(url):
    res = rq.get(url)

    print(res)

    sc = res.status_code

    if sc == 200: 
        print("%s 요청 성공" %(url))
    elif sc == 404:
        print("%s 찾을 수 없음" %(url))
    else:
        print("%s 알 수 없는 에러 :%s " %(url, sc))


url_check("http://pjt3591oo.github.io/")
url_check("http://pjt3591oo.github.io//a")


# 실행결과 
# http://pjt3591oo.github.io/   => 요청 성공 => 출력
# http://pjt3591oo.github.io//a => 찾을 수 없음 => 출력 
# 응답 코드에 따라 조건을 나누어 처리 가능 