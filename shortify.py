# -*- coding: utf-8 -*-
import re
import sys
import requests
import json

url_regex = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")

def goo_shorten_url(url):
    post_url = 'http://da.gd'
    payload = {'url': url, 'shorturl':''}
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
        'Referer':'http://da.gd/',
        'Origin':'http://da.gd/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    r = requests.post(post_url, data=payload, headers=headers)
    return re.findall(url_regex,r.text)[0][0]

def process_match(m):
    url = m.group(0)
    shorten_url = goo_shorten_url(url)    
    return url

if len(sys.argv) == 1:
    print "Please introduce file"
else:
    with open(sys.argv[1], 'r') as need_shortify_file:
        result = url_regex.sub(process_match, need_shortify_file.read())
        print result
