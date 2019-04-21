#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class MusicSearch:
	def __init__(self, _music_data):
		self.music_data = _music_data
		self.keys = ['artist', 'title', 'character_voice']

	def _calc_similarity(self, query_word, key):
		perplexity = 0

		return perplexity

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

		perplexities = [self._calc_similarity(query_dict[key], key) for key in self.keys]

