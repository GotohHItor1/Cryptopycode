from Crypto.Util.number import*
import gmpy2
from sympy import*
c=169169912654178
c1=128509160179202
c2=518818742414340
c3=358553002064450
n=gcd(pow(c1,2)-c2,c1*c2-c3)
print(n)
p = 28977097
q = 18195301
n = p*q
e = discrete_log(n,c1,2)
phi = (p-1)*(q-1)
d=  gmpy2.invert(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))