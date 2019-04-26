import json
from match import MusicSearch

with open('../Album.json', 'r') as f:
	ALBUM_DATA = json.load(f)

collect_data = {
	'origin_url': 'https://columbia.jp/idolmaster/cinderella/COCC-16575.html',
	'cd_title': '高垣楓',
	'series': 'THE IDOLM@STER CINDERELLA MASTER 004',
	'full_title': 'THE IDOLM@STER CINDERELLA MASTER 004\n高垣楓',
	'artist': {'character': ['高垣楓'], 'voice': ['早見沙織']},
	'url': 'https://columbia.jp/idolmaster/cinderella/img/COCC-16578.jpg'
}


def test_search_data_3_input():
	input_data = {
		'artist': '高垣楓',
		'title': 'こいかぜ',
		'character_voice': '早見沙織'
	}
	assert MusicSearch(ALBUM_DATA).search_data(input_data) == collect_data


def test_search_data_2_input():
	input_data = {
		'artist': '高垣楓',
		'title': 'こいかぜ',
		# 'character_voice': '早見沙織'
	}
	assert MusicSearch(ALBUM_DATA).search_data(input_data) == collect_data


def test_search_data_1_input():
	input_data = {
		# 'artist': '高垣楓',
		'title': 'こいかぜ',
		# 'character_voice': '早見沙織'
	}
	assert MusicSearch(ALBUM_DATA).search_data(input_data) == collect_data
