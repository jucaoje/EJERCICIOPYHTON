# Importamos las funciones y el diccionario desde sus respectivos archivos
from creartarea import creartarea, taskes
from vertarea import leer_tareas

def mostrar_menu():
    print("\n===============================")
    print("      MENÚ DE GESTIÓN DE TAREAS")
    print("===============================")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas guardadas")
    print("3. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-3): ").strip()
        
        if opcion == '1':
            # Llama a la función para ingresar una nueva tarea
            creartarea()
            
        elif opcion == '2':
            # Llama a la función externa para leer/mostrar las tareas
            leer_tareas(taskes)
            
        elif opcion == '3':
            print("\n¡Saliendo del programa. Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, elige 1, 2 o 3.")

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    ejecutar_menu()