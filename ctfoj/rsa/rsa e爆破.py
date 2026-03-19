from Crypto.Util.number import*
import gmpy2
import base64
p = 177077389675257695042507998165006460849
n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
q=n//p
phi=(p-1)*(q-1)
c="==gMzYDNzIjMxUTNyIzNzIjMyYTM4MDM0gTMwEjNzgTM2UTN4cjNwIjN2QzM5ADMwIDNyMTO4UzM2cTM5kDN2MTOyUTO5YDM0czM3MjM"
c=c[::-1]
c=base64.b64decode(c)
c=int(c)
for e in range ( 50000, 70000 ):
    if  gmpy2.gcd ( e, phi ) == 1:
        d = gmpy2.invert ( e, phi )
        m = pow ( c, d, n )
        flag=str(long_to_bytes(m))
        if 'flag' in flag or 'CTF' in flag or ("{" in flag and '}'in flag):
            print(flag)
