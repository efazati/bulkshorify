# -*- coding: utf-8 -*-
import re
import sys

url_regex = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")

matches = []

def process_match(m):
    matches.append(m.group(0))
    return '{{URL}}'

if len(sys.argv) == 1:
    print "Please introduce file"
else:
    with open(sys.argv[1], 'r') as need_shortify_file:
        result = url_regex.sub(process_match, need_shortify_file.read())
        print result
