# Al seleccionar la opcion 1 debe llamar el modulo crear tarea
# Al seleccionar la opcion 2 debe llamar el modulo ver tarea
# Al seleccionar la opcion 3 debe llamar el modulo eliminar tarea
import creartarea, vertarea, eliminartarea


def menu():
    print("Este es el menu Principal de tu Gestor de Tareas")
    print("_______________________________________________")
    print(" 1. Crear tarea")
    print(" 2. Ver tareas")
    print(" 3. Eliminar tarea")
    print("_______________________________________________")

    tarea_texto = input("Ingresa la opcion deseada    ")
    tarea = int(tarea_texto)  # convertimos el texto del input a entero

    if tarea == 1:
        creartarea.creartarea()
    elif tarea == 2:
        vertarea.vertarea()
    elif tarea == 3:
        eliminartarea.eliminartarea()
    else:
        print("Opcion no valida, selecciones una opcion valida")
    
        menu()
            
        

    
    
    