#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import json
import match

json_str = '''
{"artist":"高垣楓",
"title":"こいかぜ"}
'''
#json_str = input()

json_dict = json.loads(json_str)
print(json_dict["artist"])

artist = json_dict["artist"]
title = json_dict["title"]

url = hogehoge(artist, title)

print(url)
