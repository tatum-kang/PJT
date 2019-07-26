# Project 1 - 파이썬을 활용한 데이터 수집 1

### |Project Goal

- 기초 Python에 대한 이해
- Python을 통한 데이터 수집 및 파일 저장
- Python 조건/반복문 및 다양한 자료구조 조작
- API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
- 영화평점사이트(예- watcha)에 필요한 데이터를 프로그래밍을 통해 수집한다.



### |Contents

- **주간/주말 박스오피스 데이터 수집**

  - [Code](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/01.py)

  - [Result: `boxoffice.csv`](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/boxoffice.csv)

    - 영화진흥원 Open API를 통해 `영화 대표코드`, `영화명`, `(해당일)누적관객수`의 Data를 얻어 가장 최신 누적 관객수를 보장하여 `boxoffice.csv`  파일을 생성하고 Write 

  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

    - 기본 요청

    `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json`

    

- **영화 상세정보 수집**

  - [Code](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/02.py)

  - [Result: `movie.csv`](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/movie.csv)

    - 위 결과인 `boxoffice.csv`파일에서 `영화 대표코드`를 통하여 상세한 영화정보 Data를 얻고, 이를 `movie.csv`파일을 생성하고  Write

  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

    - 기본 요청
    
      `http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json`
    
      
    
  
- **영화인 정보 수집**

  - [Code](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/03.py)

  - [Result: `director.csv`](https://lab.ssafy.com/stlight/pjt/blob/master/pjt01/director.csv)

    - 위 결과인 `movie.csv`파일에서 `영화인명`을 통하여 해당 영화인 Data를 얻고, 이를 `director.csv`파일을 생성하고 Write
    
    - 동일 인물 배제를 하기 위하여 `영화명`을 통하여 Filtering
  - [API Interface](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)
  
    - 기본 요청
    
      `http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json`
    
      
    
