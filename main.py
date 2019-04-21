#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import json
import match

json_str = '''
{"artist":"高垣楓",
"title":"こいかぜ"}
'''

def main():
    # json_str = input()

    # アルバムDBのJSONを読み込み
    f = open ("sample.json", 'r',encoding="utf-8")
    album_db = json.load(f)

    print(album_db[1][0]["artist"]["character"])
    print(album_db[1][0]["artist"]["voice"])
    print(album_db[1][0]["in_music_title"])

    # アルバムDBのJSONを使ってmatchクラスのインスタンスを生成
    # a = Match(album_db)

    # 問い合わせ
    json_dict = json.loads(json_str)

    artist = json_dict["artist"]
    title = json_dict["title"]

    #url = a.match(artist, title)

    #print(url)

if __name__ == "__main__":
    main()