# 영화 상세정보 
import requests, csv, pprint
from decouple import config
from pprint import pprint

KEY = config('API_KEY')
url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={KEY}'

with open('movie.csv', 'w', encoding='utf-8', newline='') as newf:
    #movie.csv 파일 생성 및 헤더 작성
    fieldnames = ('영화 대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독명')
    writer = csv.DictWriter(newf, fieldnames=fieldnames)
    writer.writeheader()

    with open('boxoffice.csv', 'r', encoding='utf-8') as f :
        # boxoffice.csv 읽기 및 영화 대표코드 추출 
        reader = csv.DictReader(f)  
        for row in reader :
            movie_code = row['영화 대표코드']
            result = requests.get(f'{url}&movieCd={movie_code}').json()
            movie_info = result.get('movieInfoResult').get('movieInfo')
            
            #장르
            genres = movie_info.get('genres')
            moive_genre_list = []
            for genre in genres:
                moive_genre_list.append(genre.get('genreNm'))
            movie_genre = (', ').join(moive_genre_list)
            
            #감독명
            directs = movie_info.get('directors')
            if directs == [] :
                movie_direct = ''
            else:
                if directs[0].get('peopleNmEn') == '':
                    movie_direct = directs[0].get('peopleNm')
                else:
                    movie_direct = directs[0].get('peopleNm') + '(' + directs[0].get('peopleNmEn') + ')'
            
            #관람등급
            grade = movie_info.get('audits')
            movie_grade = '' if grade == [] else grade[0].get('watchGradeNm')
           
            #info dict 작성
            movie_info_row = {
                '영화 대표코드': movie_code,
                '영화명(국문)': movie_info.get('movieNm'),
                '영화명(영문)': movie_info.get('movieNmEn'),
                '영화명(원문)': movie_info.get('movieNmOg'),
                '관람등급': movie_grade,
                '개봉연도': movie_info.get('openDt'),
                '상영시간': movie_info.get('showTm'),
                '장르': movie_genre,
                '감독명': movie_direct,
            }
            writer.writerow(movie_info_row)
            