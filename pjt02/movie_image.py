import requests, csv, time

        # movie_naver.csv 읽기 
with open('movie_naver.csv', 'r', encoding='utf-8') as f :
    reader = csv.DictReader(f)  
    # 썸네일 및 영화코드 추출하여 jpg 파일로 저장하기 
    for row in reader :
        thumb_url = row.get('영화 썸네일 이미지의 URL')
        movie_code = row.get('영진위 영화 대표코드')
        with open(f'images/{movie_code}.jpg', 'wb') as f:
            image = requests.get(thumb_url).content
            f.write(image)
            time.sleep(0.1)
        


