
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import json
from tqdm import tnrange, tqdm_notebook
from selenium.webdriver.chrome.options import Options

# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성

with open('review_daegu_33689.json', 'r', encoding='UTF8') as fp:  # 파일 열기
    review = json.load(fp)

driver = webdriver.Chrome('C:\\Users\\Kim\\Desktop/chromedriver')
# driver = webdriver.PhantomJS('C:\\Users\\Kim\\Desktop\phantomjs') # 있는 거 선택하기
driver.implicitly_wait(1.5)

new_review = {}
k = 1
max_attempt = 3
listing_id = review.keys()
attempt = 0

for j in tnrange(len(listing_id), desc='숙소 수'):
    l_id = list(listing_id)[j]
    rev_lst = review[l_id]
    print(str(k) + '번째 집 시작')
    for i in tnrange(len(rev_lst), desc='변역루프'):
        rev = rev_lst[i]
        comment = rev['comments']
        lang = rev['language']
        language.append(lang)
        if lang == 'en':
            print(str(i + 1) + '번째는 영어입니다. 번역을 하지 않습니다.')
            rev['language'] = rev['language'] + '_en'

        elif len(comment) >= 5000:
            print(str(listing_id) + '의' + str(i + 1) + '번째 리뷰는 5000자가 넘습니다.')
            rev['language'] = rev['language'] + '_5000'
            print(comment)
        else:
            url = 'https://papago.naver.com/?sk=auto&tk=en&st='
            driver.get(url)
            driver.set_window_size(1024, 600)  # 창크기 미리 설정
            try:
                input = driver.find_element_by_css_selector("#txtSource")
                input.send_keys(comment)
                driver.implicitly_wait(2)
                trans_button = driver.find_element_by_css_selector('#btnTranslate')
                driver.implicitly_wait(2)
                trans_button.click()  # 한문장인 경우는 번역 버튼 눌러줘야한다.
                if '\n' in comment:  # 띄여져있는 문장입력시 늦어져서 로드가 안되서 error 나와서 충분히 쉬는 시간준다.
                    time.sleep(2)
                    for x in range(max_attempt):  # 자동으로 번역 되는 경우있어서 세번의 확인 작업
                        driver.implicitly_wait(3)  # 다 써질때까지 기다리자
                        target = driver.find_elements_by_xpath(
                            '//*[@id="txtTarget"]/span')  # 여러 문장인 경우가 있어서 elements라 함
                        t_comment = ''
                        for t in range(len(target)):
                            t_comment = t_comment + target[t].text
                else:
                    driver.implicitly_wait(2)  # 로드 될 때까지 2초 의무로 기다려주기
                    target = driver.find_element_by_xpath('//*[@id="txtTarget"]/span')
                    t_comment = target.text

                rev['t_comments'] = t_comment  # json에 저장
                rev['language'] = rev['language'] + '_en'


            except NoSuchElementException:
                print(str(l_id) + '의' + str(i + 1) + '번째에서 오류가 났습니다.')
                trans.append('error')
                rev['error'] = 'True'
                print(comment)

            except StaleElementReferenceException:  # 한번 더 시도해보기
                time.sleep(2)
                target = driver.find_elements_by_xpath('//*[@id="txtTarget"]/span')  # 여러 문장인 경우가 있어서 elements라 함
                t_comment = ''  # 초기화
                trans_button.click()
                for t in range(len(target)):
                    t_comment = t_comment + target[t].text
                rev['t_comments'] = t_comment  # json에 저장
                rev['language'] = rev['language'] + '_en'

    print(str(k) + '번째 집 완료')
    new_review[listing_id] = review[listing_id]  # 집 하나 할때마다 새로운 딕셔너리에 넣기

    if k % 100 == 0:  # 집 100개마다 저장
        with open(str(k) + '_translated_review_daegu.json', 'w', encoding='UTF8') as fp:
            json.dump(new_review, fp, ensure_ascii=False)
        new_review = {}  # 딕셔너리 초기화
        print(str(k) + '개 까지 저장완료')

    k = k + 1

with open('all_translated_review_daegu.json', 'w', encoding='UTF8') as fp:
    json.dump(review, fp, ensure_ascii=False)

print('번역완료')