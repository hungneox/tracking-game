#!/usr/local/bin/python3
import base64

word = ''

with open("noise.txt") as f:
    word = f.read()

for i in range(len(word)):
    try:
        data = base64.b64decode(word[i:i+16])
        print(data.decode('utf-8'))
    except Exception as err:
        pass
