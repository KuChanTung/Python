#!/usr/bin/env python3

# coding=utf-8
# -*- coding: utf8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen("https://news.google.com")
soup = BeautifulSoup(res, "html.parser")
#print soup.select(".esc-body")

count = 1

for item in soup.select(".esc-body"):
    print('======[',count,']=========')
    news_title = item.select(".esc-lead-article-title")[0].text
    news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
    print(news_title)
    print(news_url)
    count += 1