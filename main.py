def estadoActualVias(diccionario):
	"""
 Funcion que muestra la clave y el valor de cada via del diccionario estados
 
    Parametros:
    ------------
    diccionario: contiene todos los estados de las vias Quito, Chone, Lorena, Pilaton 
 
    Retorno:
    ------------
    No retorna ningun valor
    ---
     """
	#Mostramos mensaje
	print("\nEstados actuales de las vías:")
	# Itera sobre las claves (nombres de las vías) y valores (estados) en el diccionario
	for key, value in diccionario.items():
		# Imprime el nombre de la vía y su estado actual
		print(f"{key}: {value}")
	# Hacemos un salto de línea
	print("\n")


def transito(diccionario, costo):
	"""
 Funcion que emula el comportamiento de un agente inteligente de un sistema automatizado de transito
 
    Parametros:
    ------------
    diccionario: contiene todos los estados de las vias Quito, Chone, Lorena, Pilaton 
	costo: costo 
 
    Retorno:
    ------------
    No retorna ningun valor
    ---
     """
	# Itera sobre las claves (nombres de las vías) en el diccionario
	for via in diccionario:
		# Solicita el estado de la vía actual
		estado = input(f"Ingrese el estado de la vía {via}: ")
		# Verifica que el estado sea válido (0 o 1)
		if estado != "0" and estado != "1":
			#Imprime que el estado no es válido
			print("Estado inválido.")
			#retornamos el
			return
		# Asigna el estado ingresado a la vía actual en el diccionario
		diccionario[via] = estado
	#llamamos a la funcion estadoActualVias
	estadoActualVias(diccionario)
	# Itera sobre las claves (nombres de las vías) en el diccionario
	for via in diccionario:
		# Verifica si la vía está liberada
		if diccionario[via] == "0":
			#Imprimimos que la via actual ya está liberada
			print(f"La vía {via} ya está liberada.")
		#caso contrario
		else:
			# Si no está liberada, cambia su estado a liberada
			diccionario[via] = "0"
			#Aumentamos el costo en 1
			costo += 1
			#Imprimimos que la via actual ha sido liberada
			print(f"La vía {via} ha sido liberada.")
	#llamamos a la funcion estadoActualVias
	estadoActualVias(diccionario)
	#Imprimimos el costo total por haber liberado las vías
	print("Costo actual:", costo)


if __name__ == "__main__":
	#creamos un diccionario con los estados de cada via
	estados = {"Quito": "0", "Chone": "0", "Lorena": "0", "Pilaton": "0"}
	#Inicializa una variable en este caso costo a 0
	costo = 0
	#llamamos a la funcion transito enviando como parametros el diccionario con los estados de las vias y el costo
	transito(estados, costo)
