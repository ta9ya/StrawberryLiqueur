#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import json
import io
import urllib.request
from match import MusicSearch
from PIL import Image

json_str = '''
{"artist":"高垣楓",
"title":"こいかぜ"}
'''

def main():

    # アルバムDBのJSONを読み込み
    f = open ("sample.json", 'r',encoding="utf-8")
    album_db = json.load(f)

    #print(album_db[1][0]["artist"]["character"])
    #print(album_db[1][0]["artist"]["voice"])
    #print(album_db[1][0]["in_music_title"])

    # アルバムDBのJSONを使ってmatchクラスのインスタンスを生成
    a = MusicSearch(album_db)

    # 問い合わせ

    # json_str = input()
    json_dict = json.loads(json_str)

    artist = json_dict["artist"]
    title = json_dict["title"]

    #answer = a.search_data(json_str)
    
    # answerは sample.json の1要素が返るイメージ
    #url = answer[0]["url"]
    url = album_db[1][0]["url"]
    f = io.BytesIO(urllib.request.urlopen(url).read())
    img = Image.open(f)
    img.show()

    print(url)

if __name__ == "__main__":
    main()