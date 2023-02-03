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
	print("\nEstados actuales de las vías:")
	for key, value in diccionario.items():
		print(f"{key}: {value}")
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
	for via in diccionario:
		estado = input(f"Ingrese el estado de la vía {via}: ")
		if estado != "0" and estado != "1":
			print("Estado inválido.")
			return
		diccionario[via] = estado
	estadoActualVias(diccionario)
	for via in diccionario:
		if diccionario[via] == "0":
			print(f"La vía {via} ya está liberada.")
		else:
			diccionario[via] = "0"
			costo += 1
			print(f"La vía {via} ha sido liberada.")
	estadoActualVias(diccionario)
	print("Costo actual:", costo)


if __name__ == "__main__":
	estados = {"Quito": "0", "Chone": "0", "Lorena": "0", "Pilaton": "0"}
	#Inicializa una variable en este caso costo a 0
	costo = 0
	transito(estados, costo)
