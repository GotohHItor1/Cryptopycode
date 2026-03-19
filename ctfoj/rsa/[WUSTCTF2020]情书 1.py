from Crypto.Util.number import*
import gmpy2
n = 2537
e = 13
d = 937
c = '0156 0821 1616 0041 0140 2130 1616 0793'.split(' ')
p=43
q=59
phi=(p-1)*(q-1)
m=""
for x in c:
    m+=chr(int(pow(int(x),d,n))+ord('a'))
print(m)
