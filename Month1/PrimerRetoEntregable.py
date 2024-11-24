import datetime

#!Paso numero 1 , crear una lista de caracter global para almacenar los experimentos 
experimentos = []

#!Creamos las funciones que nos van a poder permiter agregar los nuevos experimentos a la lista.

#!Funciones
def añadir_experimento():
    try:
        nombre = input("Nombre del experimento: ").strip()# usamos el strip()para eliminar los espacios en blancos al momento en el que el usuario inserte los datos requeridos 
        fecha = input("Fecha de realizacion (DD/MM/AAAA): ").strip()
        datetime.datetime.strptime(fecha,"%d/%m/%Y")#nos permite validar el formato de la fecha
        tipo = input("Tipo del experimento (Quimica,Biologia,Fisica): ").strip()
        if tipo not in ["Quimica","Biologia","Fisica"]:
            raise ValueError("El tipo del experimento no es valido. Opciones: Quimica, Biologia, Fisica.")
        
        resultados = input("Por favor ingrese los resultados numericos obtenidos y separelos en comas: ").strip()
        resultados = [float(valor) for valor in resultados.split(",") if valor.strip()]#convierte la lista en floats

        if not resultados: 
            raise ValueError("La lista de los resultados no debe de estar vacia.")
        
        #* agregamos los experimentos a la lista
        experimentos.append({
            "nombre": nombre,
            "fecha": fecha,
            "tipo": tipo,
            "resultados": resultados
        })
        print("🟢El experimento ha sido añadido correctamente.\n🟢")
    except ValueError as e:
        print(f"❎ Error: {e}\n")

def visualizacion_experimento():
    #!esta funcion nos permitira visualizar los experimentos añadidos

    if not experimentos:
        print("🤖No tiene experimentos registrados en el sistema.\n")
        return
    print("\nLa Lista de los experimentos registrados: ")
    for i, exp in enumerate(experimentos, start=1):
     print(f"{i}. Nombre: {exp["nombre"]}, Fecha: {exp["fecha"]}, Tipo: {exp["tipo"]}, Resultados: {exp["resultados"]}")
    print()

#* funcion para calcular los resultados usando estadisticas basicas,(promedio, maximo y minimo), para un experimento seleccionado 

def analisisDeResultados():
    if not experimentos:
        print("📣No hay experimentos rehistrados para el respectivo analisis.\n")
        return
    
    try: 
        visualizacion_experimento() #nos permite mostrar la lista antes de elegir 
        indice = int(input("Seleccione el numero del experimento: ")) - 1
        if indice < 0 or indice >= len(experimentos):
            raise IndexError ("Numero del experimento invalido.")
        
        resultados = experimentos[indice]["resultados"]
        promedio = sum(resultados) / len(resultados)     
        maximo = max(resultados)
        minimo = min(resultados)
        print(f"\n💡Estadisticas del experimento seleccionado:")
        print(f"Promedio: {promedio:.2f},Maximo: {maximo},Minimo: {minimo}\n")
    except (ValueError, IndexError) as e:
        print(f"❌Tenemos un error: {e}\n")


#!Creamos la funcion que nos permitira generar el informe del aplicativo

def generacionDelInforme():
    if not experimentos:
        print("📋 No hay experimentos registrados para generar un informe.\n")
        return
    
    try:
        with open("informe_experimentos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("📋 Informe de los experimentos\n\n")
            for exp in experimentos:
                resultados = exp["resultados"]
                promedio = sum(resultados) / len(resultados)
                maximo = max(resultados)
                minimo = min(resultados)
                archivo.write(f"Nombre: {exp['nombre']}\n")
                archivo.write(f"Fecha: {exp['fecha']}, Tipo: {exp['tipo']}\n")
                archivo.write(f"Resultados: {resultados}\n")
                archivo.write(f"Promedio: {promedio:.2f}, Máximo: {maximo}, Mínimo: {minimo}\n\n")
        print("✅ Informe generado exitosamente: 'informe_experimentos.txt'\n")
    except IOError as e:
        print(f"❌ Error al escribir el archivo: {e}\n")
    except Exception as e:
        print(f"❌ Error inesperado al generar el informe: {e}\n")

#!Creamos una funcion principal para definir el menu del aplicativo 


def menu():
  while True: 
    print("\nMenu de las opciones: ")
    print("1. Agregar el experimento")
    print("2. Visualizar experimentos")
    print("3. Analizar resultados")
    print("4. Generar informe")
    print("5. Salir")
        
    try: 
        opcion = int(input("Por Favor seleccione una opcion: "))
        if opcion == 1: 
            añadir_experimento()
        elif opcion ==2:
            visualizacion_experimento()
        elif opcion ==3:
            analisisDeResultados()
        elif opcion ==4:
            generacionDelInforme()
        elif opcion ==5:
            print("🤝Saliendo del programa. ¡ADIOS!")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.\n")
    except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese un número.\n")

#!Inicializacion del programa 

if __name__ =="__main__":
    menu()
