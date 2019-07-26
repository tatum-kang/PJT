# 주간/주말 박스오피스 데이터 
import requests, csv, time
from decouple import config
from pprint import pprint

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
BASE_URL = f'https://openapi.naver.com/v1/search/movie.json'
URL_HEADER = {
    'X-Naver-Client-Id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_SECRET
}

def check_director(movie_director, directors):
    if movie_director in directors:
        return True

    else:
        for director in directors:
            same_spelling = 0
            for i in range(len(movie_director)):
                if movie_director[i] in director :
                    same_spelling += 1

            if 0.7 < same_spelling / len(director):
                movie_info = temp_info
                check_director = True
                return True

    return False

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as newf:
    #movie_naver.csv 파일 생성 및 header 작성
    fieldnames = ('영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지의 URL', '유저 평점')
    writer = csv.DictWriter(newf, fieldnames=fieldnames)
    writer.writeheader()
    with open('movie.csv', 'r', encoding='utf-8') as f :
        # movie.csv 읽기 및 영화명(국문) 추출
        reader = csv.DictReader(f)  
        for row in reader :
            movie_title = row.get('영화명(국문)')
            movie_code = row.get('영화 대표코드')
            movie_director = row.get('감독명').split('(')[0]
            query = f'query={movie_title}'

            #NAVER API를 이용하여 영화정보 요청하여 받기
            movie_infos = requests.get(f'{BASE_URL}?{query}', headers=URL_HEADER).json().get('items')
            
            #검색한 영화가 1개이면 바로 넣고 아니라면 감독명으로 비교해서 확인
            if len(movie_infos) == 1:
                movie_info = movie_infos[0]
            else:
                for temp_info in movie_infos:
                    directors = temp_info.get('director').strip('|').split('|')  #감독이 여러명일 경우 예외처리
                    if check_director(movie_director, directors):   #감독명이 영문표기로 인하여 한글명이 조금 다를 경우를 판단하기 위한 함수 
                        movie_info = temp_info
                        break
                        
            
            image_url = movie_info.get('image')
            time.sleep(0.1)  #요청이 너무 빨라서 sleep으로 조절 

            #썸네일 이미지가 있는 것만 info_dict 작성
            if image_url:
                movie_info_row = {
                    '영진위 영화 대표코드': movie_code,
                    '하이퍼텍스트 link': movie_info.get('link'),
                    '영화 썸네일 이미지의 URL': image_url,
                    '유저 평점': movie_info.get('userRating'),
                    # '요청': movie_title,
                    # '결과': movie_info.get('title').lstrip('<b>').rstrip('</b>'),
                }
                writer.writerow(movie_info_row)

