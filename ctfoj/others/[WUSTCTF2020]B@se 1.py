str="JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs****kxyz012789+/"
ciper="MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbVD"
from Crypto.Util.number import*
import gmpy2
import itertools
import binascii

s=['j','u','3','4']

for i in itertools.permutations(s,4):  # 对s进行排列组合的函数工具
    ss="JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs"+"".join(i)+"kxyz012789+/"
    bins = ""
    for j in ciper:
      bins+=bin(ss.index(j))[2:].zfill(6)
    print(binascii.unhexlify(hex(eval("0b"+bins))[2:-1]))