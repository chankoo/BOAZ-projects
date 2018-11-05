# BOAZ 10th Adv project

_리뷰 기반 숙소 or 화장품 추천검색 시스템_

강민 소현 찬규

## Did List

- [18.09.26] gitHub repo 생성, 일부 자료 정리
- [18.09.27] 프로젝트 회의 
- [18.10.04] 프로젝트 회의: 각자 주제 선정
- [18.10.15] 프로젝트 회의: 주제 아이디어 추가
- [18.10.20] 주제 아이디어 확정
- [18.10.21] 회의 : 데이터 수집 시작
- [18.10.25] 회의 : 일부 데이터 수집 및 전반적인 시스템 구상 & 리뷰 based RS 관련 논문
- [18.11.01] 정리 :  리뷰 데이터 crawler & LDA 개념

## ToDo List

- [18.11.06] 
   - (공통)  
   - (LDA) http://www.engear.net/wp/topic-modeling-gensimpython/ 
   - (소현) 교수님 자문 & 라이브러리(gensim) 통달
   - (강민) 리뷰 크롤링했던 내용 정리해서 올리기
   - (찬규) 리뷰 크롤링 완벽하게 통달!
   - data 형태  { room_id : [  ] , reviewr_id : [  ] , comments : [  ] }

  
                    
 
-----------------------------------------------
***Review Based Airbnb Recommender System***
- [airbnb-data-collection](https://github.com/tomslee/airbnb-data-collection)
  - [Get Started](https://github.com/chankoo/BOAZ-projects/blob/master/airbnb-data-collection.md)
  
  
  
***Review Based Cosmetics Recommender System***
- [Topic Modeling & Word Embedding on Cosmetics](https://www.slideshare.net/hongjoo/topic-modeling-word-embedding-on-cosmetics)
  - [발표_YouTube](https://www.youtube.com/watch?v=F4sIkIlGG78&feature=share)
- [사용자 리뷰 마이닝을 결합한 협업 필터링 시스템:앱추천](http://jiisonline.evehost.co.kr/files/DLA/20150627210745_01-%EC%95%88%ED%98%84%EC%B2%A0.pdf)
- [감정분석을 이용한 협업적 영화 추천 방법](https://www.researchgate.net/profile/Kyunglag_Kwon/publication/261842815_gamjeong_bunseog-eul_iyonghan_hyeob-eobjeog_yeonghwa_chucheon_bangbeob/links/02e7e535a1b5735374000000/gamjeong-bunseog-eul-iyonghan-hyeob-eobjeog-yeonghwa-chucheon-bangbeob.pdf)
- [고객 온라인 구매후기를 활용한 추천시스템 개발 및 적용](http://web.yonsei.ac.kr/dslab/Journal/isr20151.pdf)


--------------------------------

## 강의

- __CS231n__
  - [Lecture Videos](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)
  - [Syllabus](http://cs231n.stanford.edu/2017/syllabus.html)
  - [Korea Univ DSBA 한글강의](https://github.com/dsba-koreauniv/cs231n)
  - [Kyoseok Song님 한글강의](https://www.youtube.com/playlist?list=PL1Kb3QTCLIVtyOuMgyVgT-OeW0PYXl3j5)
  
- __CS224n__
  - [Lecture Videos](https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)
  - [Syllabus](http://web.stanford.edu/class/cs224n/syllabus.html)

- [모두를 위한 머신러닝/딥러닝_김성훈](https://hunkim.github.io/ml/)
  - [동영상 강의노트](http://pythonkim.tistory.com/notice/25)
  
- [PR12 딥러닝 논문읽기 모임](https://www.youtube.com/playlist?list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS)

## __NLP__

- 블로그 등 자료
   - [ratsgo's blog](https://ratsgo.github.io/blog/categories/): 훌륭한 설명
   - [딥러닝 기반 자연어처리 기법의 최근 연구 동향](https://ratsgo.github.io/natural%20language%20processing/2017/08/16/deepNLP/)
   - [쉽게 씌어진word2vec](https://dreamgonfly.github.io/machine/learning,/natural/language/processing/2017/08/16/word2vec_explained.html): 직관적이고 이해하기 쉬움
   - [한국어와 NLTK, Gensim의 만남](https://www.slideshare.net/lucypark/nltk-gensim)
 - 관련 논문
 
    ***W2V***
   - [word2vec Parameter Learning Explained](https://github.com/chankoo/BOAZ-projects/files/2420174/word2vec.Parameter.Learning.Explained.pdf): W2V 이해하기 가장 좋은 문서
   - [한국어에 적합한 단어 임베딩 모델 및 파라미터 튜닝에 관한 연구_2015](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnwyMDE2aGNsdHxneDozMjkyYjRkYWViM2Q0MzU2): 한국어에 최적화된 단어 임베딩 학습 방법 소개

    ***Sentence Classification***  
   - [Convolutional Neural Networks for Sentence Classification_2014](http://www.aclweb.org/anthology/D14-1181): w2v과 CNN 이용 문장분류
   - [PR-015 논문읽기](https://www.youtube.com/watch?v=IRB2vXSet2E&index=16&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS)
   - [컨볼루션 신경망 기반 대용량 텍스트 데이터 분류 기술_2015](https://bi.snu.ac.kr/Publications/Conferences/Domestic/KIISE2015W_JoHY.pdf): 한국어에 적용
   
## __LDA__
 
  - 블로그 등 자료
     - [Topic modelint, LDA](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/06/01/LDA/)
     - [Latent Dirichlet Allocation (LDA)](http://khanrc.tistory.com/entry/Latent-Dirichlet-Allocation-LDA)
     - [LDA 파라미터 추정: 깁스 샘플링을 써서](http://4four.us/article/2014/10/lda-parameter-estimation)   
     - [Topic Modeling with Gensim(Python)](http://www.engear.net/wp/tag/gensim/)

## __RS__

- 블로그 등 자료
   - [Yamarae님 추천 시스템의 전반적인 내용(1)](http://yamalab.tistory.com/67?category=747907)
   - [‘검색의 시대’ 지고 ‘추천의 시대’ 뜬다](https://news.samsung.com/kr/%EA%B2%80%EC%83%89%EC%9D%98-%EC%8B%9C%EB%8C%80-%EC%A7%80%EA%B3%A0-%EC%B6%94%EC%B2%9C%EC%9D%98-%EC%8B%9C%EB%8C%80-%EB%9C%AC%EB%8B%A4)
   - [네이버_인공지능추천시스템 airs개발기](https://www.slideshare.net/deview/airs-80886207)
   - [카카오 추천 알고리즘 리포트](https://brunch.co.kr/@kakao-it/72)
   - [SanghyukChun님 Matrix Completion](http://sanghyukchun.github.io/73/)
 
 - 관련 논문
   - [Deep Neural Networks for YouTube Recommendations](https://github.com/chankoo/BOAZ-projects/files/2420203/Deep.Neural.Networks.for.YouTube.Recommendations_2016_google.pdf): 구글의 유튜브 추천 알고리즘, 딥러닝 기반 추천 시스템 
   - [PR-60 논문읽기](https://www.youtube.com/watch?v=V6zixdCIOqw&index=62&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS&t=0s)
   - [최근우님 논문요약](http://keunwoochoi.blogspot.com/2016/09/deep-neural-networks-for-youtube.html)
    
   - [Deep Learning based Recommender System: A Survey and New Perspectives](https://github.com/chankoo/BOAZ-projects/files/2423646/Deep.Learning.based.Recommender.System.A.Survey.and.New.Perspectives.pdf): 딥러닝 기반 추천시스템 관련 최근 리서치 포괄적으로
  
   - [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792): 구글 플레이에 적용된 추천엔진
   - [PR-64 논문읽기](https://www.youtube.com/watch?v=hKoJPqWLrI4&index=66&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS&t=0s)
   - [Yamarae님 Wide & Deep Learning for Recommender Systems 리뷰](http://yamalab.tistory.com/101?category=747907)
  

     
------------------------
## ETC
_후보 주제 리스트업_

1) 스포일러성 리뷰 분류 
2) 개발자 커뮤니티 QA 
3) 소설 내 인물 관계망 학습 
4) 댓글기반 뉴스추천과 악성유저  
5) 일베 스크리닝 
6) 인스타 이미지 태깅
  - [Domaiin adaption](https://www.youtube.com/watch?v=SYki6jXs5eI)
7) 항공권 OCR 
8) 상품 카테고리 태깅
  - [NAVER Hack Day](https://github.com/NAVER-CAMPUS-HACKDAY/common/issues)
  
__SPLR__
 - [CNN으로 문장 분류하기] (https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)
 
 
__q_cls_rec__
- okky_crawler.ipynb 구현 [게시글 데이터](https://drive.google.com/open?id=1C9TE2sfZamVG61MNbe54UpKn6P1Hb9b3)
- QnA분석.ipynb 진행중, 우선 Question classification 시도(전처리 )
- [기사 : ‘뉴욕타임스’, 머신러닝 기반 자동 태그 시스템 개발](http://www.bloter.net/archives/234850)
- [논문 : CNN을 이용한 소셜 이미지 자동 태깅](http://kiise.or.kr/e_journal/2016/1/JOK/pdf/06.pdf)
  - [ImageNet](http://image-net.org/index)
  
  
__news_rec__
- 카카오 루빅스
  - [기계학습 기반의 뉴스 추천 서비스 구조와 그 효과에 대한 고찰_2015](https://github.com/chankoo/BOAZ-projects/files/2497787/_._._._._._._._._.pdf)
  - [카카오 정책산업 연구:루빅스 소개](https://brunch.co.kr/@kakao-it/57)

