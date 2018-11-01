## Get Started with airbnb-data-collection
-------------------------

- [깃 서브모듈 문제시 참고](http://blog.naver.com/PostView.nhn?blogId=tommybee&logNo=220840604103&parentCategoryNo=&categoryNo=90&viewDate=&isShowPopularPosts=true&from=search)


### 도커 설치 및 실행
-------------------------------
[도커설치(우분투 18.04 도커 설치 방법)](https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/) 후에 진행한다

도커에 관한 내용은 

- [초보를 위한 도커 안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html) 
- [우분투 18.04 도커 설치](https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/)


등을 참고하며 같이 공부해보자

우선 [/docker/README.md](https://github.com/tomslee/airbnb-data-collection/blob/462bac4719c6cddae586d3b23f6f9a5fd2fd3693/docker/README.md) 의 2. 3.을 차례로 진행한 결과이다

> ./BOAZ-projects/airbnb-data-collection 이라는 로컬 디렉토리에서 진행한다
>
> 그 하위 docker 디렉토리에 진입해 ps 명령으로 실행 중인 컨테이너 목록을 본다
>
> 아래와 같이 airbnbcollector 라는 이름으로 2개의 컨테이너가 실행되고 있다
>
> ![](https://user-images.githubusercontent.com/38183218/47371747-4d915f00-d723-11e8-8e7a-a6ba44386c61.png)

>  docker-compose up 명령의 결과이다
>
>  docker-compose는 컨테이너 여럿을 사용하는 도커 애플리케이션을 정의하고 실행하는 도구이다 [참고: 도커 컴포스 활용법](http://raccoonyy.github.io/docker-usages-for-dev-environment-setup/)
>
> up으로 서비스(멀티 컨테이너)가 실행된다
>![](https://user-images.githubusercontent.com/38183218/47370961-d27b7900-d721-11e8-81a2-18aa5c077d4b.png)

> 도커가 다운로드한 이미지의 목록을 확인하는 images 명령이다
>
> data collector의 사용을 위해 도커, 컨테이너, 이미지 등의 기본 개념 학습이 더 필요할 것이다
>
>![](https://user-images.githubusercontent.com/38183218/47371748-4e29f580-d723-11e8-9230-1aef26720657.png)


### PostgreSQL, PostGIS 설치 및 실행 -> PostGIS 설치가 까다로움
---------------------
 - [PostgreSQL]
  - [psql 설치](http://moomini.tistory.com/88)
  - [psql 설치 및 연동](https://wikidocs.net/7385)
  - [psql10_doc](http://postgresql.kr/docs/10/)
  - [psql 기본강좌](http://www.gurubee.net/postgresql/basic)
  - [docker와 psql](http://postgresql.kr/blog/docker_postgresql.html)
  
- [postgis 설치](http://paintitcode.tistory.com/35)
  - ``` sudo apt-get install postgresql-10-postgis-2.4 ``` 이용
  - [dependency 확인](https://postgis.net/docs/manual-2.4/postgis-ko_KR.html#install_short_version)
    - [GDAL 설치 참고](http://ngee.tistory.com/350)
  - [shared object 파일 관련 환경변수 설정](http://adnoctum.tistory.com/541)

> PostGIS 설치환경
> ![2018-10-31 23-36-46](https://user-images.githubusercontent.com/38183218/47796467-be5dfa00-dd67-11e8-9d17-ca6c989b32c0.png)

#### Installing and upgrading the database schema
> db와 role을 모두 airbnb로 둔다
> ![2018-10-31 23-59-08](https://user-images.githubusercontent.com/38183218/47797615-067e1c00-dd6a-11e8-9a44-58f00a40a3a0.png)

> ```psql --user airbnb airbnb < postgresql/schema_current.sql``` 명령으로 스키마 생성한다. 기존에 저장된 schema_current.sql을 리다이렉션한다

>> [Peer authentication 에러 발생시](http://zipeya.tistory.com/entry/postgresql-DB%EC%83%9D%EC%84%B1-%EB%B0%8F-%EC%A0%91%EC%86%8D-%EC%8B%9C-Peer-authentication%EC%97%90%EB%9F%AC-%EB%B0%9C%EC%83%9D-%EC%8B%9C-%ED%95%B4%EC%95%BC%ED%95%A0-%EA%B2%83)

> ![2018-11-01 00-23-57](https://user-images.githubusercontent.com/38183218/47798998-b8b6e300-dd6c-11e8-8348-b6425f83665d.png)
> 현재 위와같은 에러들이 발생한다. config 설정 필요



