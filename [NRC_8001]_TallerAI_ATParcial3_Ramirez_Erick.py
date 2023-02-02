#1 no puede transitar aumenta el costo
#via liberada no aumenta un costo
#camine o que se quede
def funcion():
	#diccionario con estados de las vias
	estados = {"Quito": "0", "Chone": "0", "Lorena": "0", "Pilatón": "0"}
	#Inicializa una variable en este caso costo a 0
	costo = 0
	#solicitamos que ingrese la locacion inicial
	primera_via = input("Ingrese la primera via: ")
	#user_input El usuario señala SI la localizacion esta sucia o limpia
	estado_via = input("Ingresa el estado de esa via: ")
	#El usuario indicia el estado de la siguiente localizacion
	estado_via2 = input("Ingresa el estado de la via 2: ")
	#El usuario indicia el estado de la siguiente localizacion
	estado_via3 = input("Ingresa el estado de la via 3: ")
	#El usuario indicia el estado de la siguiente localizacion
	estado_via4 = input("Ingresa el estado de la via 4: ")

	if primera_via == "quito":
		print("Trasladandose a la via Quito")
		# estado de via no liberada
		if estado_via == '0':
			print("Via ya esta liberada.")
		else:
			estados["Quito"] = "1"
			print("Via liberada.")
	elif primera_via == "chone":
		print("Trasladandose a la via Chone")
		# estado de via no liberada
		if estado_via == '0':
			print("Via ya esta liberada.")
		else:
			estados["Chone"] = "1"
			print("Via liberada.")
	elif primera_via == "lorena":
		print("Trasladandose a la via Lorena")
		# estado de via no liberada
		if estado_via == '0':
			print("Via ya esta liberada.")
		else:
			estados["Lorena"] = "1"
			print("Via liberada.")
	else:
		# estado de via no liberada
		print("Trasladandose a la via Pilatón")
		if estado_via == '0':
			print("Via ya esta liberada.")
		else:
			estados["Pilatón"] = "1"
			print("Via liberada.")

if __name__ == "__main__":
	funcion()
