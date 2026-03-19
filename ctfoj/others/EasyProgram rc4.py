flag = open('C:\\Users\\Bing\\Desktop\\60ca11bb-ea8b-408f-bd68-973ed20740d3\\闄勪欢\\file.txt','rb').readline()
S=[]
T=[]
for i in range(256):
    S.append(i)

key = "whoami"

for i in range(256):
    T.append(ord(key[i%len(key)]))

j = 0
for i in range(256):
    j = (j+S[i]+T[i])%256
    S[i],S[j] = S[j],S[i]

i = 0
j = 0
x = 0
result = ''
for m in range(38):
    i = (i+1)%256
    j = (j+S[i])%256
    S[i],S[j] = S[j],S[i]
    x = (S[i]+S[j]%256)%256
    result += chr(ord(flag[m])^S[x])

print(result)