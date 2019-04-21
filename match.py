#!/usr/bin/env python
# -*- encoding:utf-8 -*-


from levenshtein import Levenshtein


class MusicSearch(Levenshtein):
	def __init__(self, _music_data):
		super(Levenshtein, self).__init__(self)
		self.music_data = _music_data
		self.keys = ['artist', 'title', 'character_voice']

	def _calc_similarity(self, query_word, search_word):
		# leven = Levenshtein(query_word, search_word)

		long_word_length = len(query_word)  if len(query_word) > len(search_word) else len(search_word)

		self.str1 = query_word
		self.str2 = search_word
		distance = self.initArray(self.str1, self.str2)
		dist = self.editDist(self.str1, self.str2, distance)
		return dist / long_word_length

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

		for data in self.music_data:
			flag = True
			perplexities = []

			for key in self.keys:
				perplexity = self._calc_similarity(query_dict[key], search_word)

				if perplexity > 0:
					perplexities.append(perplexity)
				else:
					flag = False
					break

			if flag:
				total_perplexity = self._calc_perplexity(perplexities)
				music_list.append([data, total_perplexity])

		music_data = max(music_list, key=lambda x:x[1])[0]

		return music_data