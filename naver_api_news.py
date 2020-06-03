# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
# url 변수에 원하는 링크 및 요청 쿼리를 전달 하면 됨

import os
import sys
import urllib.request

# 네이버 어플리케이션(검색) 생성 후, "client_id", "client_secret" 확인 가능
client_id = ""
client_secret = ""
encText = urllib.parse.quote("코로나")
displyNum = "10"

# https://openapi.naver.com/v1/search/news            # GET JSON, XML네이버 검색의 뉴스 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/encyc           # GET JSON, XML네이버 검색의 백과사전 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/blog            # GET JSON, XML네이버 검색의 블로그 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/shop            # GET JSON, XML네이버 검색의 쇼핑 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/webkr           # GET JSON, XML네이버 검색의 웹 문서 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/movie           # GET JSON, XML네이버 검색의 영화 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/image           # GET JSON, XML네이버 검색의 이미지 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/doc             # GET JSON, XML네이버 검색의 전문정보 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/kin             # GET JSON, XML네이버 검색의 지식iN 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/book            # GET JSON, XML네이버 검색의 책 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/cafearticle     # GET JSON, XML네이버 검색의 카페글 검색 결과를 반환합니다.
# https://openapi.naver.com/v1/search/adult           # GET JSON, XML입력한 검색어가 성인 검색어인지 판별한 결과를 반환합니다.
# https://openapi.naver.com/v1/search/errata          # GET JSON, XML입력한 검색어의 한영 오류를 변환한 결과를 반환합니다.
# https://openapi.naver.com/v1/search/local           # GET JSON, XML네이버 지역 서비스에 등록된 지역별 업체 및 상호 검색 결과를 반환합니다.

url = "https://openapi.naver.com/v1/search/news" + "?display=" + displyNum +"&query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)