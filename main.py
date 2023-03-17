import re
patron=r"\b\d{4}\b"

linea=input()
res=re.findall(patron,linea)
for fecha in res:
    print(fecha)

