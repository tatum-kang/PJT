# Project 1 - 파이썬을 활용한 데이터 수집 1

### |Project Goal

- 기초 Python에 대한 이해
- Python을 통한 데이터 수집 및 파일 저장
- Python 조건/반복문 및 다양한 자료구조 조작
- API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
- 영화평점사이트(예- watcha)에 필요한 데이터를 프로그래밍을 통해 수집한다.



### |Contents

- **주간/주말 박스오피스 데이터 수집**

  - [Code](https://github.com/epstlight/PJT/blob/master/pjt01/01.py)

  - [Result](https://github.com/epstlight/PJT/blob/master/pjt01/boxoffice.csv)

    - Open API를 통해서 `영화 대표코드`, `영화명`, `(해당일)누적관객수`의 Data를 얻어 최신의 누적 관객수를 보장하여 Write 

  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

    - 기본 요청

    `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json`

    

- **영화 상세정보 수집**

  - [Code](https://github.com/epstlight/PJT/blob/master/pjt01/02.py)

  - [Result](https://github.com/epstlight/PJT/blob/master/pjt01/movie.csv)

    - 위에서 얻은 Data 중 `영화 대표코드`를 통하여 상세한 영화정보 Write

  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

    - 기본 요청
    
      `http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json`
    
      
    
  
- **영화인 정보 수집**

  - [Code](https://github.com/epstlight/PJT/blob/master/pjt01/03.py)

  - [Result](https://github.com/epstlight/PJT/blob/master/pjt01/director.csv)

    - 위에서 얻은 Data 중 `영화인명`을 통하여 해당 영화인의 정보 Write
    
    - 동일 인물 배제를 하기 위하여 `영화명`을 통하여 Filtering
  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)
  
    - 기본 요청
    
      `http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json`
    
      
    
