# Day2

- 파이썬 딕셔너리

  - 딕셔너리?

  ```python
  student_phone_number = {
      "김민지": "010-1234-1234"
  }
  # key와 value로 이루어진 데이터 타입
  # 일반 변수와 리스트 변수와 비교해서 생각하기
  ```

  - 얘를 왜 씀?
  - 얘를 어떻게 활용할지?
  - JSON과 비교했을 때 어떤 차이가 있는지?

  ```json
  result: {
      status: "200",
      message: "",
  }, ...
  // JSON 파일 내용
  ```

  ```python
  "20층 식당": {
      "A코스": "돈까스",
      "B코스": "순대국"
  },
  # python 딕셔너리
  ```

  

  - 딕셔너리 활용 문제

- 어제 사용했던 다음 웹툰 코드를 활용해서 우리가 원하는 정보를 뽑아내는 것

  ```python
  url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
  response = requests.get(url)
  data = response.json()
  
  toons = []
  for toon in data:
      # 제목의 key는 'title'
      title = toon["title"]
  
      # 설명의 key는 'introduction'
      desc = toon["introduction"]
  
      # 장르의 위치는 'cartoon' 안에 'genre'라는 리스트 안에 'name'이라는 key
      genres = []
      for genre in toon["cartoon"]["genres"]:
          genres.append(genre["name"])
  
      # 작가 이름의 위치는 'cartoon'안에 'artists'라는 리스트 안에 'name'이라는 key
      artists = []
      for artist in toon["cartoon"]["artists"]:
          artists.append(artist["name"])
      # 썸네일 이미지의 위치는 'pcThumbnailImage'안에 'url'이라는 키의 값으로 있음
      img_url = toon["pcThumbnailImage"]["url"]
      tmp = {
          title: {
              "desc": desc,
              "writer": artists,
              "img_url": img_url
          }
      }
      toons.append(tmp)
  ```

- 함수 활용하기

  ```python
  def request_json_data_from_url(url):
      # 3. 해당 url에 요청을 보낸다.
      response = requests.get(url)
      data = response.json()
      return data
  
  def parse_daum_webtoon_data(data):
      toons = []
      for toon in data:
          # 제목의 key는 'title'
          title = toon["title"]
  
          # 설명의 key는 'introduction'
          desc = toon["introduction"]
  
          # 장르의 위치는 'cartoon' 안에 'genre'라는 리스트 안에 'name'이라는 key
          genres = []
          for genre in toon["cartoon"]["genres"]:
              genres.append(genre["name"])
          
          # 작가 이름의 위치는 'cartoon'안에 'artists'라는 리스트 안에 'name'이라는 key
          artists = []
          for artist in toon["cartoon"]["artists"]:
              artists.append(artist["name"])
          # 썸네일 이미지의 위치는 'pcThumbnailImage'안에 'url'이라는 키의 값으로 있음
          img_url = toon["pcThumbnailImage"]["url"]
          tmp = {
              title: {
                  "desc": desc,
                  "writer": artists,
                  "img_url": img_url
              }
          }
          toons.append(tmp)
      return toons
  
  days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
  daily_toon_data = {}
  
  ```



- 내가 자주 접속하는 사이트들 중에 우리가 좀전에 배운 형태로 되어 있는 사이트를 찾아서 필요한 정보들만 뽑아서 화면에 출력하세요.

  - 다음 영화
  - 카카오 페이지(웹툰, 기다무)
  - 서울시 공공데이터
  - 아프리카 tv
  - 네이버 지도(경로 데이터)

  

- 플라스크 설치하기

  ```command
  > pip install flask
  ```

  - 환경 설정

    ```command
    > $env:FLASK_ENV="development"
    > $env:FLASk_DEBUG="True"
    ```



- 플라스크 서버 돌리기

  ```python
  # 기본내용
  from flask import Flask, escape, request
  import requests
  
  app = Flask(__name__)
  if __name__ == '__main__':
      app.run(debug=True)
      
  @app.route('/')
  def index():
      return { 'hello': 'world'}
  ```

  