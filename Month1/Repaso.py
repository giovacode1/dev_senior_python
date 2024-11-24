#!
#* repaso para el reto 1 


"""Atributos de un experimento: nombre, fecha(DD/MM/AAAA), tipo y resultados numérico"""
listaDeExperimentos = [
    ["Experimento 1", "16/11/2024","Química", [5,3,4,5,6,4]],
]

def agregar_experimento():
    """Permite agregar un nuevo experimento con sus atributos. dificultad: 1"""
    pass

def eliminar_experimentos():
    """Perminte eliminar un experimento. dificultad: 1, requiere el uso de la funcion agregar_experimento"""
    pass

def visualizar_experimentos():
    """Permite visualizar todos los experimentos. dificultad: 1. requiere el uso de la funcion agregar_experimento"""
    pass

def calcular_estadisticas():
    """Calcular estadisticas basicas(promedios, máximos y mínimos) de un experimento. dificultad: 2. requiere el uso de funcion agregar_experimento"""
    pass

def comprar_experimentos():
    """Comparar dos o mas expremientos para determinar los mejores o peores resultados dificultad: 2. requiere el uso de funciones calcular_estudisticas"""
    pass

def generar_informe():
    """Generar un informe resumen de los expremintos y sus estadisticas. dificultad: 3. requiere el uso de funciones visualizar_experimentos y calcular_estadisticas"""
    pass

def mostar_menu():
    """Muesta el numero principal del programa. dificultad: 1"""
    print("=====Menu Principal=====")
    print("=====Gestión de Experimentos====")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    print("=====Análisis de Datos====")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("====Informes====")
    print("6. Generar informe")
    print("====Salir====")
    print("7. Salir")
    
def main():
    """Controla el flujo general del sistema. dificultad: 1"""
    mostar_menu()
    pass

main()