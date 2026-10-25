
# Diccionario global para almacenar las tareas de forma persistente
taskes = {}

def creartarea():
    print("\n--- Ingresar nueva tarea ---")
    task = input("Ingresa una tarea: ").strip()
    
    if not task:
        print("La tarea no puede estar vacía.")
        return None, None
        
    description = input("Ingresa una descripción: ").strip()
    
    # Guardamos en el diccionario
    taskes[task] = description
    
    print(f"\n¡Tarea guardada con éxito!")
    print(f"La tarea ingresada es '{task}' y su descripción es: '{description}'")
    
    # Retornamos el diccionario completo actualizado
    return taskes