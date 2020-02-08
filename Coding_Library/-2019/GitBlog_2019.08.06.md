# GitBlog_2019.08.06.md
---
## git 필수 용어 

저장소 (repository): 소스코드 저장소      
clone : 원격지 저장소를 로컬에 복제하여, 로컬저장소, 생성     
index: 커밋 할 파일들의 스냅샷     
commit : 추가, 수정, 변경내역 저장단위      
push: 원격지 저장소에 반영되지않은 로컬 저장소 내역을 push   
pull:로컬 저장소에 반영되지않은 원격지 저장소 내역을 pull   
branch: 저장소 내에서 독립된 커밋 공간 . 기본 브랜치는 master       

---
- jekyll가동 
>$ bundle exec jekyll serve     
- UTF-8 인코딩으로 바꿔 줘야 한다.    


-해결 방안   
>$ chcp 65001  
>$ bundle exec jekyll serve   
    
* 해결 방안으로 도 해결 안될 경우가 많다 그래서 최대한 한글을 주석으로 안 다는것이 좋은것같다.   
  
-서버 동기화 시킬때    
> 깃허브 주소를만들고    
: jerrykim91.github.io  

>$ git clone username.github.io(주소를 끌어와야한다.)  
>$ cd username.github.io  
>$ git remote remove origin   
>$ git remote add origin   
      https://github.com/username/username.github.io.git  
>$ git push -u origin master   
  
 touch : 크리에이티브와 같은 생성 명령어 이지만 작동이 안할경우    
      echo.>name_file.txt 형식으로 입력하면 오류 없이 생성이 된다.   
 ---