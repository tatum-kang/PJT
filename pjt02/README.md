# Project 2 - 파이썬을 활용한 데이터 수집 2

### |Project Goal

- API 요청을 통한 데이터 수집 및 파일 저장
- Python을 통한 JSON 및 이미지 파일 조작
- API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
- 영화평점서비스(예- watcha)에 필요한 추가 데이터를 프로그래밍을 통해 수집한다.



### |Contents

- **네이버 영화 검색 API - `movie_naver.py`**

  - [Code](https://lab.ssafy.com/stlight/pjt/blob/master/pjt02/movie_naver.py)

  - [Result : `movie_naver.csv`](https://lab.ssafy.com/stlight/pjt/blob/master/pjt02/movie_naver.csv)

    - NAVER 영화 검색 API를 통해 `영진위 영화 대표코드` ,`하이퍼텍스트 link `, `영화 썸네일 이미지의 URL` , `유저 평점`의 Data를 `movie_naver.csv` 파일 Write
    -  `영화 썸네일 이미지의 URL` 이 없는 경우 저장

  - [API Interface](https://developers.naver.com/docs/search/movie/)

    - 기본 요청

    `https://openapi.naver.com/v1/search/movie.json`

    

- **영화 포스터 이미지 저장 - `movie_image.py`**

  - [Code](https://lab.ssafy.com/stlight/pjt/blob/master/pjt02/movie_image.py)

  - [Result : `.jpg`](https://lab.ssafy.com/stlight/pjt/tree/master/pjt02/images)

    - 위 결과의 `movie_naver.csv` 파일에서 `영화 썸네일 이미지의 URL` Data를 얻고, 이를 통하여 영화 포스터를 `.jpg` 파일로 저장
  - 파일명은 마찬가지로 `movie_naver.csv`에서  `영진위 영화 대표코드`를 읽어와서 이를 적용
  
- 기본 요청
  
    - Image 요청 기본 python code
    
    ```python
    requests.get({썸네일 이미지의 URL}).content
    ```

