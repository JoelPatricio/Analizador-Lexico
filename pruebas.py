<<<<<<< HEAD
room_num = {'John': 425, 'Liz': 212}
room_num['Isaac'] = {"joel":19,"patrocop":25}
room_num['Hilario'] = "Sanchez"
if(room_num["Hilario"]!="-"):
    print("Si exite")
else:
    print("No existe")
print("********************")

aux1='a'
if(aux1.isdigit()):
    print("digito")
else:
    print("letra")
=======
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
>>>>>>> a88ddff4170db0cef6f2220b56a757742f843d51
