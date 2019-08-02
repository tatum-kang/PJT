## Project 3 - Web(HTML/CSS를 활용한 웹 사이트 구성)

### |Project Goal

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성



### |Contents

- HTML 기초

  - 필수 사항
    - DOCTYPE 은 html입니다.
    - html 의 언어는 한국어(ko)입니다.
    - meta 태그에 인코딩 설정을 UTF-8로 설정 해주세요.
    - meta 태그에 기본 viewport 설정을 해주세요. (width: device-width, initial-scale: 1.0)
    - title 태그는 영화추천사이트 라고 설정 해주세요.
    
    ```
    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>영화 추천 서비스</title>
      <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="reboot.css">
      <link rel="stylesheet" href="style.css">
      <link rel="stylesheet" href="layout.css">
    </head>
    ```
    
    

- header
  웹 사이트의 헤더 부분에는 로고 이미지와 네비게이션 바를 구성합니다.

  - 필수 사항
    
    - 속성
    
      - 헤더는 항상 상단에 유지 됩니다. (sticky)
      - 높이는 80px이며, 좌우 안쪽 여백(padding)은 40px입니다
    
      ```html
      header {
        height: 80px;
        padding-left: 40px;
        padding-right: 40px;
      position: fixed;
        top: 0;
        z-index: 1000;
      }
      ```
    
    - 이미지 배치
    
      - 로고 이미지는 좌측에 배치합니다.
      - 로고 이미지의 높이는 60px입니다.
      - 로고 이미지는 images/logo.png 입니다.
    
    - 네비게이션 바 ( nav )
    
      - 네비게이션 바의 항목은 우측에 배치합니다.
      - 총 4개의 항목이 배치되며, 각각 임의의 링크( # ) 으로 설정합니다.
      - 수직 정렬을 통해 중앙으로 일치시킵니다.
      - bullet Point 제거시킵니다.
    
      ```
      nav {float:right;}
      .nav-items > li {
        display:inline-block;
        margin: 0 10px;
        list-style: none;  
      }
      ```
    
      - 글자 색상을 변경합니다.
      -  마우스 오버시에도 글자 색상을 변경하고 밑줄을 제거합니다.
    
      ```
      .nav-items > li > a {
        color: black;
      }
      .nav-items > li > a:hover {
        color: gray;
        text-decoration: none;
      }
      ```
  
- title section
  서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다.

  - 필수사항

    - 속성

      - 높이는 320px이며, header 의 높이만큼 상단 여백을 설정합니다.
      - 수직 정렬을 통해 중앙으로 일치시킵니다.
      - 배경 이미지는 적절하게 삽입하고, 이미지에 맞게 사이즈와 위치를 조절 합니다.

      ```
      #section-title {
        background-image: url('/images/background.jpg');
        background-size: cover;
        background-position: center;
        text-align: center;
        line-height: 300px
      }
      ```

      

- aside

  좌측 레이아웃에 장르 목록을 구성합니다.

  - 필수 사항
    - 속성

      - 좌측에 위치하며, 상위 div 요소( #content )의 상단에 고정 시킵니다.
      - 너비는 160px이며, 상하좌우 안쪽 여백(padding)은 24px입니다.
      - h2 태그를 활용하여 장르 목록 이라고 작성합니다.
      - 개별 장르는 ul 태그를 활용 하되 기본 안쪽 여백을 제거합니다.

      ```
      aside {
        position: absolute;
        top: 0;
      }
      .aside-items {
        padding: 0;
      }
      .aside-items > li {
        list-style: none
      }
      ```

      

- footer
  연도와 이름이 작성된 푸터를 구성합니다.

  - 필수 사항

    - 속성

      - 푸터는 항상 하단에 유지 됩니다. (sticky)
      - 높이는 40px이며, 모든 내용은 수직/수평 가운데 정렬을 합니다.
      - 적절한 배경 색상을 적용 시킵니다.

      ```
      footer {
        bottom: 0;
        position: fixed;
        z-index: 100;
        text-align: center;
        line-height: 50px;
      }
      ```

      

### |Result

![result](C:\Users\student\development\PJT\pjt03\결과물.jpg)

