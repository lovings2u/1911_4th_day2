from flask import Flask, escape, request
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    daily_toon_data = {}
    day = 'mon'
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    
    return daily_toon_data
    




def request_json_data_from_url(url):
    # 3. 해당 url에 요청을 보낸다.
    response = requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    toons = []
    for toon in data["data"]:
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