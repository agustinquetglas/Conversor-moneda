#to-do-list-ejercicio
#Agustin Quetglas y Lautaro Romero Stach
def cargar_tareas(tareas):
    descripcion=input("Ingrese la descripción de la tarea: ")
    tareas.append({"descripcion": descripcion, "completada": False})
        
def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        for i, tarea in enumerate(tareas):
            if tarea["completada"]:
                estado = "Completada"
            else:
                estado = "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")

def marcar_tarea_completada(tareas):
    listar_tareas(tareas)
    if tareas:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: "))
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")

def eliminar_tarea(tareas):
    listar_tareas(tareas)
    if tareas:
        indice = int(input("Ingrese el número de la tarea a eliminar: "))
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            print("Tarea eliminada.")
        else:
            print("Número de tarea inválido.")

def menu_interactivo():
    tareas = []  # Lista para almacenar las tareas
    while True:
        print("\n--- Menú ---")
        print("1. Cargar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_tareas(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            marcar_tarea_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_interactivo()

