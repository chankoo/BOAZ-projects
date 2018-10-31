## Get Started with airbnb-data-collection

[도커설치(우분투 18.04 도커(Docker) 설치 방법)](https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/) 후에 진행한다

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
