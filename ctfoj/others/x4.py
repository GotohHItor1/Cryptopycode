from Crypto.Util.number import*
str1="ἇ̀Ј唒ဃ塔屋䩘卖剄䐃堂ن䝔嘅均ቄ䩝ᬔ"
str2="asadsasdasdasdasdasdasdasdasdasdqwesqf"
str1=bytes_to_long(str1.encode("utf-16-le"))
str2=bytes_to_long(str2.encode("utf-8"))
c=str1^str2
print(long_to_bytes(c))