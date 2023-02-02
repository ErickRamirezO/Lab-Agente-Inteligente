#INSTRUCTIONS
#Enter LOCATION A/B in captial letters
#Enter Status O/1 accordingly where 0 means CLEAN and 1 means DIRTY

def aspiradora():
    # inicializamos el diccionario de estados
    # 0 indica limpio y 1 indica sucio
    """funcion que emula el comportamiento de un agente inteligente de una aspiradora
    Parametros:
    ------------
    NO tiene parametros 

    Retorna:
    ------------
    No retorna ningun valor

    ---
     """
     #Declara variable de estado
    estados = {'A': '0', 'B': '0'}
    #Inicializa una variable en este caso costo a 0
    costo = 0
    #solicitamos que ingrese la locacion inicial
    primera_locacion = input("Ingrese la locacion de la aspiradora: ") 
    #user_input El usuario señala SI la localizacion esta sucia o limpia
    estado_habitacion = input("Ingresa el estado de esa habitacion: " ) 
    #El usuario indicia el estado de la siguiente localizacion
    estado_habitacion_complemento = input("Ingresa el estado de la otra habitacion: ")
	#Imprimimos las habitaciones deseadas
    print("Habitaciones:" + str(estados))

#Agregar las condiciones
    if primera_locacion == 'A':
        # Localizacion A esta sucia.
        print("Aspiradora yendo a A: ")
        if estado_habitacion == '1':
            print("Locacion A esta sucio.")
            # Absorver la suciedad y marca el lugar como limpio
            estados['A'] = '0'
            costo += 1
            ## Incrementa el costo de A
            print("Limpiando locacion A")
            print("Costo actual: " + str(costo))
#Condiciones para A limpio 
            if estado_habitacion_complemento == '1':
                # SI B esta sucio
                print("Locacion B esta sucio.")
                print("Moviendo a la derecha a la Locacion B. ")
                costo += 1 #incrementar cost para moverse a la otra ubicacion
                print("Costo actual: " + str(costo))
                # Limpiar y marcarlo como limpio
                estados['B'] = '0'
                costo += 1 #incrementar cost por limpieza 
                print("Limpiando locacion B")
                print("Costo actual: " + str(costo))
            else:
                # limpiar y marcar como limpio
                print("Location B ya esta limpio.")
                print("Ninguna accion. Costo actual" + str(costo))
               
        if estado_habitacion == '0':
            print("Locacion A ya esta limpio.")
            if estado_habitacion_complemento == '1':
                # Si B esta Sucio
                print("Locacion B esta sucio.")
                print("Moviendo a la derecha a la Locacion B.")
                costo += 1 #incrementar cost para moverse la locacion 
                print("costo actual: " + str(costo))
                # limpiar la suciedad y marcar como limpio
                estados['B'] = '0'
                costo += 1   
                print("Limpiando Locacion B. ")                    #cost para limpiar
                print("Actualizando costo: "+str(costo))
                
            else:
                print("No acciones" + str(costo))
                print(costo)
                # aspirar y marcar como limpio
                print("Locacion B ya esta limpio.")
    else:
        print("Aspiradora dezplazandose a la locacion B")
        # Localizacion B esta sucia.
        if estado_habitacion == '1':
            print("Locacion B esta sucia.")
            # Aspirar la suciedad y marcarla como limpia
            estados['B'] = '0'
            costo += 1  # cost para aspirar
            print("Costo por Limpieza" + str(costo))
            print("Locacion B ya esta limpio.")

            if estado_habitacion_complemento == '1':
                # Si A esta Sucio
                print("Locacion A esta sucio.")
                print("Moviendo a la izquierda para la localizacion A ")
                costo += 1  # cost Para moverse a la localizacion
                print("Costo por mover a la izquierda" + str(costo))
                # Aspirar la suciedad y marcarla como limpia
                estados['A'] = '0'
                costo += 1  # cost para aspirar 
                print("Costo por suciedad " + str(costo))
                print("Locacion A esta ya limpio.")

        else:
			#imprimimos el costo
            print(costo)
			# Imprimimos que ya esta limpio
            print("Location B esta ya limpio.")

            if estado_habitacion_complemento == '1': 
                # Imprimimos que esta sucio
                print("Locacion A is Dirty.")
                print("Moviendo a la izquierda to the Location A. ")
                costo += 1  
                # cost para moverse a la izquierda
                print("COST for moving LEFT " + str(costo))
                # Limpiar la suciedad y marcar como limpio
                estados['A'] = '0'
                costo += 1 
                 # cost para limpiar
                print("Cost for SUCK " + str(costo))
				# Imprimimos que ya esta limpio
                print("Location A has been Cleaned. ")
            else:
				#Imprimimos que no hay acccion por hacer
                print("No hay costo: " + str(costo))
                # Imprimimos que ya esta limpio
                print("Locacion A esta ya limpio.")

    # Terminar Limpieza 
    print("Estados actuales: ")
    print(estados)
    print("Performance Measurement: " + str(costo))

if __name__ == "__main__":
	aspiradora()