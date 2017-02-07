#!/usr/bin/python3
fd=open("/etc/passwd")
lineas=fd.readlines()
fd.close()
dicUser = {}
for linea in lineas:
    dicUser[linea.split(":")[0]] = linea.split(":")[-1][:-1]
#Now, we going to look the shell of user 'root' and 'imaginario'
print("The shell of root is " + dicUser['root'])
try:
    print("The shell of imaginario is " + dicUser['imaginario'])
except KeyError:
    print("The user doesn't exist")
