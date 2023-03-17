import re
patron=r"(([a-z]\.([a-z]+))\.([\d]{4})(@alumnos.urjc.es))|(([a-z]+)\.([a-z]+)(@urjc.es))"
pattern=r"\3"
linea=input()
resultado=re.findall(patron,linea)
for i in range(0,len(resultado)):
    if resultado[i][4]=="@alumnos.urjc.es":
        print("alumno "+ resultado[i][2]+" matriculado en "+ resultado[i][3])
    if resultado[i][8]=="@urjc.es":
        print("profesor " + resultado[i][6] + " apellido " + resultado[i][7])
