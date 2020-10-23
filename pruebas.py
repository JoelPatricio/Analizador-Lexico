import re

str1="a"
str2='\d'
aux=bool(re.search(r'\d', str1))
if(aux==True):
    print(aux)
else:
    print("False")
    

linea = "6=>=:10"
linea = linea.split("=>")
print(linea)
