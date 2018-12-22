## GCP와 Docker를 이용한 손쉬운 GPU 기반 딥러닝 개발환경 구축

#### 참고
이상수님의 [이제는, 딥러닝 개발환경도 Docker로 올려보자!!](https://github.com/2sang/Moducon-Docker-tf-setup/blob/master/Docker-tensorflow-setup.pdf)

변성윤님의 [Google Cloud Platform에서 Tensorflow, Jupyter Notebook 설치 및 startup script 설정](https://zzsza.github.io/gcp/2018/06/14/install-tensorflow-jupyter-in-gcp/)

### 

변성윤님 포스팅을 참조하여 

1) GCP 가입 
2) Quota 요청
3) 인스턴스 생성
  - 지역 : asia-east1, 영역 : asia-east1-a
  - 머신 유형 : cpu 8, ram 52, Tesla K80 Gpu
  - 부팅 디스크 : Ubuntu 16.04 LTS
  - 방화벽에 HTTP/HTTPS 트래픽 허용 체크

까지 완료한 후 

4) 인스턴스에 접속한다(gcloud compute --project "nlp-tensorflow" ssh --zone "asia-east1-a" "gpu-k80")
5) 인스턴스에 [Nvidia Graphic Driver] - [Docker] - [Nvidia-docker2] 를 각각 설치한다
  - [Nvidia Graphic Driver] 설치
    - `sudo apt install ubuntu-drivers-common`
    - `sudo ubuntu-drivers autoinstall`
    - `sudo reboot` (재부팅) 후 `nvidia-smi` 로 gpu 확인 
    > ![2018-12-19 23-21-29](https://user-images.githubusercontent.com/38183218/50225819-e7545000-03e4-11e9-80de-d460367c1534.png)
  - [Docker] 설치
    - [초보를 위한 도커 안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html) 참고
    - `curl -fsSL https://get.docker.com/ | sudo sh` 리눅스 환경에선 한줄로 끝
  - [Nvidia-docker2] 설치
    - `--runtime=nvidia` 옵션으로 호스트의 nvidia 드라이버를 컨테이너에 적용한다
    > ![2018-12-19 23-25-25](https://user-images.githubusercontent.com/38183218/50226003-6c3f6980-03e5-11e9-8c0c-6207cc1b081f.png)
6) Dockerhub의 tensorflow-gpu 컨테이너를 실행한다
  - `docker run --runtime=nvidia -it -p 8888:8888 tensorflow/tensorflow:latest-gpu`
  
7) Jupyter Notebook 실행
  - 인스턴스의 외부 ip에 port 8888로 접속한다
  > ![2018-12-19 23-30-37](https://user-images.githubusercontent.com/38183218/50226557-dc9aba80-03e6-11e9-90c2-94db7fe25d7c.png)
  - 처음 접속시 token을 요구한다. 터미널에 뿌려지는 토큰을 복붙해주자
  - 모든 과정을 잘 마치면 다음과 같이 jupyter notebook을 띄운다
  > ![2018-12-19 23-37-37](https://user-images.githubusercontent.com/38183218/50226743-5632a880-03e7-11e9-98b3-4074557bcf59.png)
  
### 도커 사용으로 이득보는 부분
- CUDA, Tensorflow 등 설치과정에서 발생하는 수많은 알수없는 충돌을 해결 -> official image는 거의 대부분 깨끗하게 잘 돌아간다
- 혹시나 충돌이 나더라도 충돌 원인의 분석이 훨씬 쉬워진다(깨끗한 인스턴스 환경)



#### GCP 인스턴스와 도커 컨테이너 간 공유폴더 설정하기

1) docker run 시에 v 옵션을 주어 gcp 인스턴스의 '/data'와 도커 컨테이너의 '/data'를 공유 폴더로 설정한다 ':' 로 구분해 앞쪽이 gcp인스턴스, 뒤쪽이 도커 컨테이너의 디렉토리이다 
> ![0](https://user-images.githubusercontent.com/38183218/50374489-7bffbd80-0632-11e9-8bad-3d5a1ba9b0e9.PNG)
2) jupyter notebook의 upload 기능으로 쉽게 파일 업로드한다
![1](https://user-images.githubusercontent.com/38183218/50374490-7bffbd80-0632-11e9-9cdb-c0345fb3c5bb.PNG)
3) 노트북 내에서 파일목록을 확인하고 (!ls)
![2](https://user-images.githubusercontent.com/38183218/50374491-7c985400-0632-11e9-83fd-2cdc7c7c8fa0.PNG)
4) 공유폴더로 설정된 '/data'에 파일을 copy한다 (!cp)
![3](https://user-images.githubusercontent.com/38183218/50374492-7e621780-0632-11e9-8d38-5b2adc7f2096.PNG)
5) '/data'에 파일이 옮겨졌고
![4](https://user-images.githubusercontent.com/38183218/50374493-7e621780-0632-11e9-9959-1e61e8fb6973.PNG)
6) 도커를 stop 시킨 후에도 파일은 인스턴스에 남아있다 굳
![-1](https://user-images.githubusercontent.com/38183218/50374485-786c3680-0632-11e9-8a07-807c6fc058b7.PNG)
