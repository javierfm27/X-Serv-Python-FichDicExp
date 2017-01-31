#!/usr/bin/python3
fd=open("/etc/passwd")
lineas=fd.readlines()
fd.close()
for linea in lineas:
    dic = {}
    #print("login:" + (linea.split(":")[0]) + "  shell:" + linea.split(":")[-1][:-1])
