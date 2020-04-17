import os
nombres = []

for item in os.listdir("escriba direccion"):
    if item[-4:] == ".jpg":
        nombres.append(item)

print("listado de todos los nombres",nombres)
print("Nombre Original",nombres[0:4])

for fn in os.listdir("sireccion"):
  if fn[-4:] == ".jpg":
   nombre=fn[0:-4:]
   nn=''
   nn='ejempplo_1.jpg'
   os.rename(fn,nn)
print("Cambio realizado",nn)