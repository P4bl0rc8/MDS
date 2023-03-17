import re
patron=r"\b[E]*[\ | \- ]*[\d]{4}[\ | \- ]?[A-Z]{3}\b"
linea=input()
res=re.findall(patron,linea)
for fecha in res:
    print(fecha)