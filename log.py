import re
patron=r"\d{4}-\d{2}-\d{2} * \d{2}:\d{2}:\d{2}\.\d{3} * (\w*) * \d* * --- * \[(.*)\] *(\w*\.)*(\w*) *: *(.*)"
linea=input()
resultado=re.findall(patron,linea)
for i in range(0,len(resultado)):
   print("\""+resultado[i][0]+"\",\""+resultado[i][1]+"\",\""+resultado[i][3]+"\",\""+resultado[i][4]+"\"")
