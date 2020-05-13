import os
import json
while True:
	#Menu principal que cuenta con un bucle while
	print("       Menu   ")
	print("1. Iniciar lavado ")
	print("2. Base de datos ")
	print("3. Salir ")
	opcion = input(' Digite una opcion  ' )

	os.system('cls') 
	if opcion == "1":
		print('  Tipo de vehiculo  ')
		print(' 1. Automovil    (Q30.00) ')
		print(' 2. Motocicleta  (Q15.00)')
		print(' 3. Camioneta    (Q50.00)')
		#valores asignados a las variables dependiendo la condicion if 
		opcion1 = input(' Seleccione el tipo de vehiculo ')
		if opcion1 == "1":
			precio = 30
			tipoauto = "Automovil"
		elif opcion1 == "2":
			precio = 15
			tipoauto = "Motocicleta"
		elif opcion1 == "3":
			precio = 50
			tipoauto = "Camioneta"
		
		os.system('cls')
		print(' Tipo de cliente ')
		print(' 1. Standar ')
		print(' 2. Miembro')
		opcion2 = input(' Seleccione tipo de cliente ')
		if opcion2 == "2":
			cliente = "Miembro"
			print('  Tiene un descuento de 10%  ')
		elif opcion2 == "1":
			cliente = "Standar"
		os.system('cls')
		print(' Dia de la semana')
		print('1. Lunes a Viernes ')
		print('2. Fin de Semana ')
		opcion3 = input(' Seleccione una opcion ')
		if opcion3 == "1":
			dia = "No"
		elif opcion3 == "2":
			dia = "Si"
		os.system('cls')
		#operaciones logicas de los descuentos de precios totales de los lavados 
		if opcion1 == "1" and opcion2 == "2" and opcion3 == "1":
			total = precio - (precio * 0.20)
			descuento = (precio * 0.20)
			print(" Tiene descuento del 20%")
		elif opcion1 =="2" and opcion2 == "2" and opcion3 == "1":
			total = precio - (precio * 0.20)
			descuento = (precio * 0.20)
			print(" Tiene descuento del 20%")
		elif opcion1 == "3" and opcion2 == "2" and opcion3 == "1":
			total = precio - (precio * 0.20)
			descuento = (precio * 0.20)
			print(" Tiene descuento del 20%")
		
		elif opcion1 == "1" and opcion2 == "1" and opcion3 == "1":
			total = precio - (precio * 0.10)
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")
		elif opcion1 =="2" and opcion2 == "1" and opcion3 == "1":
			total = precio - (precio * 0.10)
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")
		elif opcion1 == "3" and opcion2 == "1" and opcion3 == "1":
			total = precio - (precio * 0.10)  
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")
		

		elif opcion1 == "1" and opcion2 == "2" and opcion3 == "2":
			total = precio - (precio * 0.10)
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")
		elif opcion1 =="2" and opcion2 == "2" and opcion3 == "2":
			total = precio - (precio * 0.10)
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")
		elif opcion1 == "3" and opcion2 == "2" and opcion3 == "2":
			total = precio - (precio * 0.10)
			descuento = (precio * 0.10)
			print(" Tiene descuento del 10%")

		elif opcion1 == "1" and opcion2 == "1" and opcion3 == "2":
			print(" No hay descuento ")
			total = precio
			descuento = 0
		elif opcion1 =="2" and opcion2 == "1" and opcion3 == "2":
			print(" No hay descuento ")
			total = precio
			descuento = 0
		elif opcion1 == "3" and opcion2 == "1" and opcion3 == "2":
			print(" No hay descuento")
			total = precio
			descuento = 0
		print(" El total a pagar es: Q", total)
		basedatos = []
		for i in range(1):
			ventas = {}
			ventas[" tipo de vehiculo: "] = tipoauto
			ventas[" Precio: "] = precio
			ventas[" Tipo de cliente: "] = cliente
			ventas[" Fin de semana: "] = dia
			ventas[" Descuento: "] = descuento
			ventas[" Total: "] = total
			basedatos.append(ventas)
		with open ("basedatos.json", "w") as archivo:
			json.dump(basedatos, archivo)

	elif opcion == "2":
		print (basedatos)
	elif opcion == "3":
		break
	else:
		print( " Seleccione una opcion valida ")

