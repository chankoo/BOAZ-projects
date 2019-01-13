# BOAZ 10th Adv project

_에어비앤비 리뷰 분석_

강민 소현 찬규

## Did List

- [18.09.26] gitHub repo 생성, 일부 자료 정리
- [18.09.27] 프로젝트 회의 
- [18.10.04] 프로젝트 회의: 각자 주제 선정
- [18.10.15] 프로젝트 회의: 주제 아이디어 추가
- [18.10.20] 주제 아이디어 확정
- [18.10.21] 회의 : 데이터 수집 시작
- [18.10.25] 회의 : 일부 데이터 수집 및 전반적인 시스템 구상 & 리뷰 based RS 관련 논문
- [18.11.01] 정리 : 리뷰 데이터 crawler & LDA 개념
- [18.11.06] 회의 : 크롤러 완성, 데이터수집
- [18.11.08] 정리 : RNN기반 감성분석, LDA 공부
- [18.11.15] 회의 : LARA,LDA 이용 세부 rating 도출 방법 정리, BOAZ 수료자 피드백
- [18.11.19] 정리 : 데이터수집(서울,부산,제주) 완료, 영어 외 언어 번역작업(파파고) 수행 중
- [18.11.22] 회의 : [What Airbnb Reviews can Tell us?] 논문 리뷰
- [18.11.24] 회의 : 한국어 번역 전 전처리 시도
- [18.11.29] 회의 : 파파고 이용 번역 완료
- [18.12.03] 회의 : 텍스트 전처리 완료. LDA 모델링 중. LARA 논문 리뷰
- [18.12.06] 회의 : LARA segmentation 알고리즘 구현 완료
- [18.12.08] 정리 : LDA 최적화 중, LRR 구현 중
- [18.12.14] 회의 : elastic net 기반 감성사전 구축 논의, 스케쥴조정
- [19.01.13] 정리 : doc2vec, 평점 0-3인 방에 대해 LDA 후 aspect별 elastic net , LDA 전처리 완료, 전체 LDA

## To Do List

[18.01.13]

- doc2vec 내일까지 parameter 조정
- 내륙 / 바다 지역 LDA
- 방에 대한 워드클라우드 만들어보기
- aspect별로 긍부정 워드클라우드 만들어보기 (ppt용)
- DTM으로 행렬곱, 부정적인 aspect에 대해서 score 구해보기 -> 다른방과 비교해서 표정으로 시각화
- LARA는 motivatation
- 포토샵으로 사이트 구성 다시해보기


### [진행사항.md](https://github.com/chankoo/BOAZ-projects/blob/master/%EC%A7%84%ED%96%89%EC%82%AC%ED%95%AD.md)

 
-----------------------------------------------
***Review Based Airbnb Recommender System***
- [airbnb-data-collection](https://github.com/tomslee/airbnb-data-collection)
  - [Get Started](https://github.com/chankoo/BOAZ-projects/blob/master/airbnb-data-collection.md)
- [What Airbnb Reviews can tell us?](https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=7410&context=etd)
- [GCP와 docker 이용한 딥러닝 개발환경(gpu) 구축](https://github.com/chankoo/BOAZ-projects/blob/master/gcp-gpu-with-docker.md)
  
  



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
   - [NLP를 위한 딥러닝 가이드](http://docs.likejazz.com/deep-learning-for-nlp/)
   
 
 - 관련 논문
 
    ***Embeddings***
   - [word2vec Parameter Learning Explained](https://github.com/chankoo/BOAZ-projects/files/2420174/word2vec.Parameter.Learning.Explained.pdf): W2V 이해하기 가장 좋은 문서
   - [한국어에 적합한 단어 임베딩 모델 및 파라미터 튜닝에 관한 연구_2015](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnwyMDE2aGNsdHxneDozMjkyYjRkYWViM2Q0MzU2): 한국어에 최적화된 단어 임베딩 학습 방법 소개
   - [Skip-Thought Vectors(문장수준 임베딩)](https://arxiv.org/pdf/1506.06726.pdf)
   -

    ***Sentence Classification***  
   - [Convolutional Neural Networks for Sentence Classification_2014](http://www.aclweb.org/anthology/D14-1181): w2v과 CNN 이용 문장분류
   - [PR-015 논문읽기](https://www.youtube.com/watch?v=IRB2vXSet2E&index=16&list=PLlMkM4tgfjnJhhd4wn5aj8fVTYJwIpWkS)
      - [컨볼루션 신경망 기반 대용량 텍스트 데이터 분류 기술_2015](https://bi.snu.ac.kr/Publications/Conferences/Domestic/KIISE2015W_JoHY.pdf): 한국어에 적용
   
   ***Aspects Detection***
   - [LARA: A Rating Regression Approach](https://www.cs.virginia.edu/~hw5x/paper/rp166f-wang.pdf)
   - [LARA: without Aspect Keyword Supervision](https://www.cs.virginia.edu/~hw5x/paper/p618.pdf)
   - [Aspect extraction for opinion mining with a deep convolutional neural
network(aspect detection을 위한 multi-level CNN)](http://sentic.net/aspect-extraction-for-opinion-mining.pdf)
   
   
## __LDA__
 
  - 블로그 등 자료
     - [Topic modelint, LDA](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/06/01/LDA/)
     - [Latent Dirichlet Allocation (LDA)](http://khanrc.tistory.com/entry/Latent-Dirichlet-Allocation-LDA)
     - [LDA 파라미터 추정: 깁스 샘플링을 써서](http://4four.us/article/2014/10/lda-parameter-estimation)   
     - [Topic Modeling with Gensim(Python)](http://www.engear.net/wp/tag/gensim/)
     - [트위터로 바라본 지카바이러스 사태](http://miniddong.me/2016/11/12/zika-tweet-lda/#f5) : 트위터를 크롤링해서 LDA후 감정분석
     - [LDA에 용어 가중치 적용하기](https://bab2min.tistory.com/605)
  - 관련 논문
     - [커뮤니티 기반 Q&A서비스에서의 질의 할당을 위한 이용자의 관심 토픽 분석에 관한 연구](http://www.dbpia.co.kr/Journal/PDFViewNew?id=NODE06519825&prevPathCode=)
     - [LDA 토픽 모델링을 활용한 판례 검색 및 분류 방법](http://www.dbpia.co.kr/Journal/PDFViewNew?id=NODE07252870&prevPathCode=)
     - [LDA를 이용한 온라인 리뷰의 다중 토픽별 감성분석 : TripAdvisor 사례](http://kiss.kstudy.com/thesis/thesis-view.asp?key=3585302)
     - [한국어 자연어 처리와 LDA, 감성분석을 이용한 항공사 서비스 만족요인 연구](http://www.earticle.net/Article.aspx?sn=317360)
     - [여행 사이트 리뷰를 활용한 관광지 만족도 요인 추출 및 평가](http://jkiie.snu.ac.kr/index.php/journal/article/viewFile/323/pdf)
     - [엘라스틱 넷을 적용한 블로그 리뷰 감성사전 구축 및 극성 분류](http://www.dbpia.co.kr/Journal/PDFViewNewid=NODE06602478&prevPathCode=)
     - [SNS에서 단어 간 유사도 기반 단어의 쾌-불쾌 지수 추정](http://kiise.or.kr/e_journal/2014/3/cpl/pdf/05.pdf)
     - [퍼지 추론과 감성사전 구축을 통한 화장품 추천 시스템](http://www.ndsl.kr/ndsl/search/detail/article/articleSearchResultDetail.do?cn=JAKO201722163436188)
  - usin R
     - [R을 이용한 토픽분석](https://brunch.co.kr/@mapthecity/2)
     - [환자 불편 상담에 관한 LDA 분석](https://junhewk.github.io/text/2017/08/15/complaint-LDA/)
  - usin Python
     - [Topic Modeling and LDA in Python](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)
     - [LDA in Python](https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html)
     - [LDA in Python-How to grid search best topic models](https://www.machinelearningplus.com/nlp/topic-modeling-python-sklearn-examples/)
     - [gensim ftn](https://svn.spraakdata.gu.se/repos/richard/pub/statnlp2016_web/vgassignment1.html)
     
     
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

0) Review Based Cosmetics Recommender System
- [Topic Modeling & Word Embedding on Cosmetics](https://www.slideshare.net/hongjoo/topic-modeling-word-embedding-on-cosmetics)
   - [발표_YouTube](https://www.youtube.com/watch?v=F4sIkIlGG78&feature=share)
   
- [사용자 리뷰 마이닝을 결합한 협업 필터링 시스템:앱추천](http://jiisonline.evehost.co.kr/files/DLA/20150627210745_01-%EC%95%88%ED%98%84%EC%B2%A0.pdf)
- [감정분석을 이용한 협업적 영화 추천 방법](https://www.researchgate.net/profile/Kyunglag_Kwon/publication/261842815_gamjeong_bunseog-eul_iyonghan_hyeob-eobjeog_yeonghwa_chucheon_bangbeob/links/02e7e535a1b5735374000000/gamjeong-bunseog-eul-iyonghan-hyeob-eobjeog-yeonghwa-chucheon-bangbeob.pdf)
- [고객 온라인 구매후기를 활용한 추천시스템 개발 및 적용](http://web.yonsei.ac.kr/dslab/Journal/isr20151.pdf)

1) 스포일러성 리뷰 분류 

- [CNN으로 문장 분류하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)

2) 개발자 커뮤니티 QA
- okky_crawler.ipynb 구현 [게시글 데이터](https://drive.google.com/open?id=1C9TE2sfZamVG61MNbe54UpKn6P1Hb9b3)
- QnA분석.ipynb 진행중, 우선 Question classification 시도(전처리)
- [기사 : ‘뉴욕타임스’, 머신러닝 기반 자동 태그 시스템 개발](http://www.bloter.net/archives/234850)
- [논문 : CNN을 이용한 소셜 이미지 자동 태깅](http://kiise.or.kr/e_journal/2016/1/JOK/pdf/06.pdf)
  - [ImageNet](http://image-net.org/index)
3) 소설 내 인물 관계망 학습 
4) 댓글기반 뉴스추천과 악성유저
- 카카오 루빅스
  - [기계학습 기반의 뉴스 추천 서비스 구조와 그 효과에 대한 고찰_2015](https://github.com/chankoo/BOAZ-projects/files/2497787/_._._._._._._._._.pdf)
  - [카카오 정책산업 연구:루빅스 소개](https://brunch.co.kr/@kakao-it/57)
  
5) 일베 스크리닝 
6) 인스타 이미지 태깅
  - [Domaiin adaption](https://www.youtube.com/watch?v=SYki6jXs5eI)
7) 항공권 OCR 
8) 상품 카테고리 태깅
  - [NAVER Hack Day](https://github.com/NAVER-CAMPUS-HACKDAY/common/issues)
  

