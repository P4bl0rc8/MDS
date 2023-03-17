import re
patron=r"\b([\d]{4})[-]([\d]{2})[-]([\d]{2})\b"
pattern=r"\3.\2.\1"
linea=input()
res=re.sub(patron,pattern,linea)
print(res)
