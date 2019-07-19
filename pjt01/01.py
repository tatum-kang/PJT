# 주간/주말 박스오피스 데이터 
import requests, csv, pprint
from decouple import config
from pprint import pprint
from datetime import datetime, timedelta

KEY = config('API_KEY')
url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KEY}&weekGb=0'

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    
    #가장 위쪽에 헤더를 작성하는 작업
    fieldnames = ('영화 대표코드', '영화명', '(해당일) 누적관객수')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    movie_list = []

    for i in range(51):
        targetDt = (datetime(2019, 7, 13) - timedelta(weeks=i)).strftime('%Y%m%d')
        result = requests.get(f'{url}&targetDt={targetDt}').json()

        for movie_info in result.get('boxOfficeResult').get('weeklyBoxOfficeList'):
            movie_code = movie_info.get('movieCd')
            movie_name = movie_info.get('movieNm')
            movie_audinum = f'({targetDt}) ' + movie_info.get('audiAcc')  

            if movie_code not in movie_list:
                movie_list.append(movie_code)
                movie_info_row = {
                    '영화 대표코드': movie_code, 
                    '영화명': movie_name, 
                    '(해당일) 누적관객수': movie_audinum,
                }
                writer.writerow(movie_info_row)
            

    