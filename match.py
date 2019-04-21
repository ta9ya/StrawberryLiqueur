#!/usr/bin/env python
# -*- encoding:utf-8 -*-


from levenshtein import Levenshtein


class MusicSearch(Levenshtein):
	def __init__(self, _music_data):
		super(Levenshtein, self).__init__()
		self.music_data = _music_data
		self.keys = {
			'artist': 'character',
			'title': 'in_music_title',
			'character_voice': 'voice'
		}

	def _calc_similarity(self, query_word, data_list):

		dist_list = list()

		for d in data_list:
			long_word_length = len(query_word) if len(query_word) > len(d) else len(d)

			distance = self.initArray(query_word, d)
			dist = self.editDist(query_word, d, distance)

			dist_list.append(dist / long_word_length)

		min_data = min(dist_list)

		return min_data

	def _calc_perplexity(self, perplexities):
		total_perplexity = sum(perplexities) / len(perplexities)
		return total_perplexity

	def search_data(self, query_dict):
		"""
		果物の値段を取得する。

		Parameters
		----------
		query_dict : dict
			{
				artist: str
					曲を歌ってるアイドル名
				title : str
					曲のタイトル
				character_voice : str
					声優名
			}

		Returns
		----------
		music_data : dict
		"""

		music_list = list()
		music_data = {}

		for data in self.music_data:
			flag = True
			perplexities = []

			for key, value in self.keys.items():
				if key == 'title':
					data_list = data[value]
				else:
					data_list = data['artist'][value]

				perplexity = self._calc_similarity(query_dict[key], data_list)

				if perplexity < 1:
					perplexities.append(perplexity)
				else:
					flag = False
					break

			if flag:
				total_perplexity = self._calc_perplexity(perplexities)
				music_list.append([data, total_perplexity])

		if len(music_data) > 0:
			music_data = min(music_list, key=lambda x: x[1])[0]

		return music_data
