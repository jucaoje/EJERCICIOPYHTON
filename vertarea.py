def leer_tareas(taskes):
    """
    Función encargada de mostrar todas las tareas almacenadas en el diccionario.
    """
    print("\n===============================")
    print("      LISTA DE TAREAS")
    print("===============================")
    
    # Validamos si el diccionario está vacío
    if not taskes:
        print("No hay tareas registradas todavía.")
    else:
        # Recorremos el diccionario mostrando cada tarea y su descripción
        contador = 1
        for tarea, descripcion in taskes.items():
            print(f"{contador}. Tarea: {tarea}")
            print(f"   Descripción: {descripcion}")
            print("-" * 30)
            contador += 1
            
    print("===============================\n")