import re
patron=r"\b(C\/|Calle) ([A-ZÑÁÉÍÓÚ][a-záéíóúñ]+),? +(N|Nº|n|nº)? ?(\d+), +([\d]{5})\b"
linea=input()
resultado=re.findall(patron,linea)
for i in range(0,len(resultado)):
   print(resultado[i][4]+"-"+resultado[i][1]+"-"+resultado[i][3])