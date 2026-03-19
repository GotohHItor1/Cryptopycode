import gmpy2
from Crypto.Util.number import*
p=18443
q=49891
phi=(p-1)*(q-1)
e=19
d=gmpy2.invert(e,phi)
ans=""
with open("C:\\Users\\Bing\\Desktop\\RsaRoll\\data.txt") as f:
    c=f.read().split('\n')[2:-1]
    for i in c:
        s=pow(int(i),d,p*q)
        ans+=long_to_bytes(s).decode("utf-8")
print(ans)

