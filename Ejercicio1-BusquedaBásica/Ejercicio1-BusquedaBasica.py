# Módulo para importar rutas 
import os
import time
import matplotlib.pyplot as plt

# Global
buscar_palabra = "Montañita"
dataset = "data"

# ========================
# PARTE 1: BÚSQUEDA LINEAL
# ========================

resultados = []
files = [i for i in os.listdir(dataset)]

inicio_lineal = time.time()

for corpus in files:
    corpus_path = os.path.join(dataset, corpus)

    with open(corpus_path, 'r', encoding='utf-8') as corpus_file:
        for doc in corpus:
            if buscar_palabra in doc.split():
                resultados.append(doc.strip())
                
fin_lineal = time.time()
tiempo_total_lineal = fin_lineal - inicio_lineal

# Mostrar Resultados
if not resultados:
    print("No hay Resultados")
else:
    print("\nParte 1: Búsqueda Lineal\n")
    print('\n'.join(resultados))

# ===================================
# PARTE 2: BÚSQUEDA ÍNDICE INVERTIDO
# ===================================
indice_invertido = {}

#files = [i for i in os.listdir(dataset)]

for corpus in files:
    corpus_path = os.path.join(dataset, corpus)
    
    with open(corpus_path, 'r', encoding='utf-8') as doc:
        for i, line in enumerate(doc, start=1):
            palabras = line.split()
            for palabra in palabras:
                if palabra not in indice_invertido:
                    indice_invertido[palabra] = [(corpus,i)]
                else:
                    indice_invertido[palabra].append((corpus,i))
                    
inicio_invertido = time.time()

if buscar_palabra in indice_invertido:
    print("\nParte 2: Búsqueda con Índice Invertido\n")
    print(f"La palabra '{buscar_palabra}' se encuentra en:")
    for archivo, linea in indice_invertido[buscar_palabra]:
        print(f" - Línea {linea}, archivo {archivo}")
else:
    print("No hay Resultados")

fin_invertido = time.time()
tiempo_total_invertido = fin_invertido - inicio_invertido

# ========================
# PARTE 3: RESULTADOS
# ========================

print("\n*** Resultados de los Tiempos de Ejecución***\n")
print(f"⏱️ Tiempo total de búsqueda Lineal: {tiempo_total_lineal:.6f} segundos") 
print(f"⏱️ Tiempo total de búsqueda con Índice Invertido: {tiempo_total_invertido:.6f} segundos")

# ========================
# PARTE 4: 
# ========================


palabras_a_buscar = ["Quito", "montañita", "Feriado", "playas", "aventura", "Galápagos", "Francia"]
