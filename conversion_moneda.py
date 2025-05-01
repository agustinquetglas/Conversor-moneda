# Ejercicio Conversor de monedas
#Agustin Quetglas y Lautaro Romero Stach
def convertir_moneda(monto, origen, conv):
    if origen == "USD" and conv == "EUR":
        return monto * 0.88
    elif origen == "USD" and conv == "ARS":
        return monto * 1172.50
    elif origen == "USD" and conv == "BRL":
        return monto * 5.68
    elif origen == "EUR" and conv == "USD":
        return monto * 1.13
    elif origen == "EUR" and conv == "ARS":
        return monto * 1328.45
    elif origen == "EUR" and conv == "BRL":
        return monto * 6.43
    elif origen == "ARS" and conv == "USD":
        return monto * 0.00085
    elif origen == "ARS" and conv == "EUR":
        return monto * 0.00075
    elif origen == "ARS" and conv == "BRL":
        return monto * 0.00048
    elif origen == "BRL" and conv == "USD":
        return monto * 0.18
    elif origen == "BRL" and conv == "EUR":
        return monto * 0.16
    elif origen == "BRL" and conv == "ARS":
        return monto * 206.57
    elif origen == conv:
        return monto
    else:
        return None

def guardar_historial(origen, conv, monto, resultado):
    with open("historial.txt", "a") as archivo:
        archivo.write(f"{monto} {origen} → {round(resultado, 2)} {conv}\n")

def mostrar_historial():
    try:
        with open("historial.txt", "r") as archivo:
            print("\nHistorial de conversiones:")
            print(archivo.read())
    except FileNotFoundError:
        print("No hay historial aún.")

def main():
    while True:
        print("\n1. Convertir moneda")
        print("2. Ver historial")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                monto = float(input("Ingrese el monto: "))
            except ValueError:
                print("Monto inválido.")
                continue

            origen = input("Moneda origen (USD, EUR, ARS, BRL): ").upper()
            conv = input("Moneda destino (USD, EUR, ARS, BRL): ").upper()  # Usar conv para destino

            resultado = convertir_moneda(monto, origen, conv)  # Usar conv aquí
            if resultado is not None:
                print(f"Resultado: {round(resultado, 2)} {conv}")
                guardar_historial(origen, conv, monto, resultado)  # Usar conv aquí también
            else:
                print("Conversión no válida.")
        
        elif opcion == "2":
            mostrar_historial()
        
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

if _name_ == "_main_":
    main()