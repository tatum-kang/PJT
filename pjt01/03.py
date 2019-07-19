# 영화인 정보 
import requests, csv, pprint
from decouple import config
from pprint import pprint

KEY = config('API_KEY')
url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={KEY}'

with open('director.csv', 'w', encoding='utf-8', newline='') as newf:
    #director.csv 파일 생성 및 헤더 작성
    fieldnames = ('영화인 코드', '영화인명', '분야', '필모리스트')
    writer = csv.DictWriter(newf, fieldnames=fieldnames)
    writer.writeheader()

    with open('movie.csv', 'r', encoding='utf-8') as f :
        #movie.csv 읽기 및 영화감독명 추출
        reader = csv.DictReader(f)  
        for row in reader :
            director = row['감독명']
            directors_id = []
            if director != '':  # 감독명이 없는게 있기 때문에 걸러줌
                movie_director = director.split('(')[0]
                movie_name = row['영화명(국문)']  ## 동명이인이 있어서 걸러주기 위해서 영화명 포함하여 검색 
                result = requests.get(f'{url}&peopleNm={movie_director}&filmoNames={movie_name}').json()
                movie_people = result.get('peopleListResult').get('peopleList')

                for person in movie_people:
                    role = person.get('repRoleNm')
                    director_id = person.get('peopleCd')
                    if role == '감독' and director_id not in directors_id:
                        directors_id.append(director_id)
                        filmo_list = person.get('filmoNames').split('|')
                        movie_info_row = {
                            '영화인 코드': director_id,
                            '영화인명': director,
                            '분야': role,
                            '필모리스트': (', ').join(filmo_list),
                        }
                        writer.writerow(movie_info_row)
