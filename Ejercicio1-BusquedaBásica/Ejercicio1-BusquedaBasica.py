# Módulo para importar rutas 
import os
import time

# ========================
# PARTE 1: BÚSQUEDA LINEAL
# ========================

def busqueda_lineal(buscar_palabra, dataset):
    resultados = []
    files = os.listdir(dataset)

    inicio = time.time()

    for archivo in files:
        archivo_path = os.path.join(dataset, archivo)

        with open(archivo_path, 'r', encoding='utf-8') as f:
            for linea in f:
                if buscar_palabra in linea.split():
                    resultados.append(linea.strip())

    fin = time.time()
    tiempo_total = fin - inicio

    return resultados, tiempo_total

# ===================================
# PARTE 2: BÚSQUEDA ÍNDICE INVERTIDO
# ===================================

def construir_indice_invertido(dataset):
    """Construye un índice invertido a partir de todos los archivos del dataset."""
    indice_invertido = {}
    files = os.listdir(dataset)

    for archivo in files:
        archivo_path = os.path.join(dataset, archivo)

        with open(archivo_path, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f, start=1):
                palabras = linea.split()
                for palabra in palabras:
                    if palabra not in indice_invertido:
                        indice_invertido[palabra] = [(archivo, i)]
                    else:
                        indice_invertido[palabra].append((archivo, i))
    
    return indice_invertido

def busqueda_indice_invertido(buscar_palabra, indice_invertido):
    """Busca una palabra en el índice invertido."""
    inicio = time.time()

    resultados = indice_invertido.get(buscar_palabra, [])

    fin = time.time()
    tiempo_total = fin - inicio

    return resultados, tiempo_total


# ========================
# PARTE 3: RESULTADOS
# ========================

def mostrar_resultados_lineal(resultados):
    if not resultados:
        print("No hay Resultados")
    else:
        print("\nParte 1: Búsqueda Lineal\n")
        print('\n'.join(resultados))

def mostrar_resultados_invertido(buscar_palabra, resultados):
    if resultados:
        print("\nParte 2: Búsqueda con Índice Invertido\n")
        print(f"La palabra '{buscar_palabra}' se encuentra en:")
        for archivo, linea in resultados:
            print(f" - Línea {linea}, archivo {archivo}")
    else:
        print("No hay Resultados")


# ========================
# MAIN
# ========================

if __name__ == "__main__":
    dataset = "data"
    buscar_palabra = "Quito"

    # --- Búsqueda Lineal ---
    resultados_lineal, tiempo_lineal = busqueda_lineal(buscar_palabra, dataset)
    mostrar_resultados_lineal(resultados_lineal)

    # --- Índice Invertido ---
    indice_invertido = construir_indice_invertido(dataset)
    resultados_invertido, tiempo_invertido = busqueda_indice_invertido(buscar_palabra, indice_invertido)
    mostrar_resultados_invertido(buscar_palabra, resultados_invertido)

    # --- Resultados de tiempos ---
    print("\n*** Resultados de los Tiempos de Ejecución***\n")
    print(f"⏱️ Tiempo total de búsqueda Lineal: {tiempo_lineal:.6f} segundos") 
    print(f"⏱️ Tiempo total de búsqueda con Índice Invertido: {tiempo_invertido:.6f} segundos")

    # --- Búsqueda de múltiples palabras ---
    palabras_a_buscar = ["Quito", "montañita", "Feriado", "playas", "aventura", "Galápagos", "Francia"]
    for palabra in palabras_a_buscar:
        res_inv, _ = busqueda_indice_invertido(palabra, indice_invertido)
        mostrar_resultados_invertido(palabra, res_inv)

