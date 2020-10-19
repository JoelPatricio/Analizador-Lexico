txt = "welcome,to,the,jungle"
txt2 = "1:4,0:2;1:5,0:-;1:-,0:3"
print(txt2)
x = txt2.split(";")

print(x)
x1 = x[0].split(",")
arre0 = []
arre0.append(x1[0])
arre0.append(x1[1])
print(arre0)
print(arre0[1][2])
