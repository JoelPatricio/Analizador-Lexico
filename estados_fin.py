#Leyendo mi archivo en la linea 3
with open("automata.txt") as f:
    lec_estadosf = f.readlines()[2]
print(lec_estadosf)

#Aplicando mi separador
separador = ","
separado = lec_estadosf.split(separador)
print(separado)

#LLenando mi diccionario con los estados y por default agregando el valor de Final
estadosf = dict.fromkeys(separado, "Final")
print (f"Este es mi diccionario de estados finales:\n{estadosf}")

#Eliminando el salto de linea de mis claves
estadosf_dic = { x.replace('\n', ''): estadosf[x] for x in estadosf.keys() }
print (f"Este es mi diccionario ya sin saltos de linea:\n{estadosf_dic}")