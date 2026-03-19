import re
import base64
s=open('C:\\Users\\Bing\\Desktop\\attachment\\flag_encode.txt','rb').read()   #双斜杠转义
base16_dic = r'^[A-F0-9=]*$'
base32_dic = r'^[A-Z2-7=]*$'
base64_dic = r'^[A-Za-z0-9/+=]*$'
n= 0
while True:
    n += 1
    t = s.decode()
    if '{' in t:
        print(t)
        break
    elif re.match(base16_dic, t):
        s = base64.b16decode(s)
        print(str(n) + ' base16')
    elif re.match(base32_dic, t):
        s = base64.b32decode(s)
        print(str(n) + ' base32')
    elif re.match(base64_dic, t):
        s = base64.b64decode(s)
        print(str(n) + ' base64')