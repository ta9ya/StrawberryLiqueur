import json
import io
import urllib.request

import os
from flask import Flask, redirect, url_for, render_template, request
from PIL import Image

from match import MusicSearch
 
app = Flask(__name__)
app.config.from_object(__name__)
 
json_str = '''
{"artist":"高垣楓",
"title":"こいかぜ",
"character_voice":"早見沙織"}
'''

def hoge():
    # アルバムDBのJSONを読み込み
    f = open ("Album.json", 'r', encoding="utf-8")
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

    answer = a.search_data(json_dict)
    
    print(answer)
    # answerは sample.json の1要素が返るイメージ
    url = answer["url"]
    #url = album_db[1][0]["url"]
    f = io.BytesIO(urllib.request.urlopen(url).read())
    img = Image.open(f)
    img.show()

    print(url)

def get_url(q):
    # アルバムDBのJSONを読み込み
    f = open ("Album.json", 'r', encoding="utf-8")
    album_db = json.load(f)

    # アルバムDBのJSONを使ってmatchクラスのインスタンスを生成
    a = MusicSearch(album_db)

    answer = a.search_data(q)

    return answer["url"]

'''
@app.route('/')
def index():
    """ 一覧画面 """
    return render_template('index.html', results={})
 '''
 
@app.route('/')
def search():
    """ 新規検索画面 """
    return render_template('form.html')
 
 
 # 検索後の処理
@app.route('/result', methods=['POST'])
def result():
    """ 分析実行処理 """
    if request.method == 'POST':
        a = request.form['title']
        b = request.form['artist']
        c = request.form['character_voice']
        url=get_url(request.form)
        return render_template('view.html', a=a, b=b, c=c, url=url)
 
if __name__ == '__main__':
    app.run(debug=True)



