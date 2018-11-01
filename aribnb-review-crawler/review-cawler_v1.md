
### 1.리뷰데이터 크롤링


```python
import requests
```


```python
url = "https://www.airbnb.co.kr/api/v2/reviews"
params = {
    'key':'d306zoyjsyarp7ifhu67rjxn52tv0t20',
    'currency':'KRW',
    'locale':'ko',
    'listing_id':'6261834',
    'role':'guest',
    '_format':'for_p3',
    '_limit':'',
    '_offset':'',
    '_order':'language_country'}
```

##### https://www.airbnb.co.kr/api/v2/reviews?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=KRW&locale=ko&listing_id=6261834&role=guest&_format=for_p3&_limit=7&_offset=7&_order=language_country


```python
params['_offset']=0  # 시작하는 게시물
params['_limit']=100 # 보여지는 게시물(100개가 최대)
```


```python
response = requests.get(url,params=params).text
```


```python
import json
result = json.loads(response)
```


```python
result.__class__
```




    dict




```python
review_count= result['metadata']['reviews_count'] # 총 review 갯수
```


```python
review_count_100 = review_count//100 # 100개단위로 하기위해서
```


```python
review_count_rest = review_count%100 # 나머지
```


```python
reviews = []

while True:
    for i in range(review_count_100):
        params['_offset'] = 100*i
        params['limit'] = 100
        response = requests.get(url,params=params).text
        time.sleep(2)
        result = json.loads(response)
        time.sleep(2)
        result_dic = result['reviews']
        for j in range(100):
            reviews.append(result_dic[j]['comments'])
            
    params['limit'] = review_count_rest
    response = requests.get(url,params=params).text
    time.sleep(2)
    result = json.loads(response)
    time.sleep(2)
    result_dic = result['reviews']
    for k in range(review_count_rest):
        reviews.append(result_dic[j]['comments'])
        
    break
    
```


```python
len(reviews)
```




    392



## listing id

### listing id만 알면 숙소 하나하나 주소 다 찾을 필요가 없다
### 피쳐 어떤 걸로 뽑아야하는지 알면 뽑을 수 있을듯
### https://api.airbnb.com/v2/explore_tabs?_format=for_explore_search_web&currency=KRW&items_per_grid=300&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&location=%EC%84%9C%EC%9A%B8&section_offset=1&&supports_for_you_v3=true&tab_id=home_tab&timezone_offset=300&version=1.3.9

Question
1. 지역 어떤 지역 할지
2. 다른 나라도 할지
3. dataframe 형태 어떤 피쳐, 파일명
4.  DB와 연결 어떻게할지
