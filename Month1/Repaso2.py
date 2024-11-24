import datetime

listaDeEquipos =[
    ["seleccion Colombia", "01/01/1924", "Futbol", [0,2,1,2,3]],
    ["seleccion Chile", "01/01/1923", "Basquet", [1,2,1,2,3]]
]

def agregar_equipo():
    try:
        nombre = input("Ingrese el nombre del equipo: ")
        fecha = input("Ingrese la fecha de creacion del equipo: ")
        tipo = input ("Ingrese el tipo de deporte:")
        resultados = list(map(int,input("Ingrese los puntos obtenidos por partidos separados por comas:").split(",")))
        listaDeEquipos.append([nombre,fecha,tipo,resultados])
        print("Equipo agregado exitosamente")
    except:
        print("Error al agregar el equipo")
        
def eliminar_equipo():
    pass

def visualizar_equipos():
    print("Listado de equipos")
    for i, equipo in enumerate(listaDeEquipos):
        print(f"{i}. {equipo[0]} - {equipo[1]} - {equipo[2]} - {equipo[3]}")
        

def calcular_estadisticas():
    visualizar_equipos()
    index = int(input("Ingrese el numero del equipo:")) 
    
    if( 0 <= index < len(listaDeEquipos)):
        resultados = listaDeEquipos[index][3]
        promedio = sum(resultados) / len(resultados)
        maximo = max(resultados)
        minimo = min(resultados)
        print(f"Estadisticas del equipo {listaDeEquipos[index][0]}")
        print(f"Promedio: {promedio}")
        print(f"Maximo: {maximo}")
        print(f"Minimo: {minimo}")

def comprar_equipo():
    visualizar_equipos()
    indices = list(map(int, input("Ingrese los indices de los equipos que desea comprar separados por comas:").split(","))) 
    resultados_comprados = []
    for index in indices:
        if( 0 <= index < len(listaDeEquipos)):
            promedio = sum(listaDeEquipos[index][3]) / len(listaDeEquipos[index][3])
            resultados_comprados.append((index, promedio))
        else:
            print(f"indice {index} no valido")
    resultados_comprados.sort(key=lambda x: x[1])
    print("Resultados Comprados")
    for index, promedio in resultados_comprados:
        print(f"{index+1}. {listaDeEquipos[index][0]} - {promedio}")  

def generar_informe():
    pass

def mostar_menu():
    pass

def main():
    pass   