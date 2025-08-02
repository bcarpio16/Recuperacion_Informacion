# Módulo para importar rutas 
import os

#Función para buscar una palabra en archivos de texto dentro de una carpeta
def buscar_archivos(palabra, carpeta):
    palabra = palabra.lower()
    resultados = []

    archivos = [i for i in os.listdir(carpeta)]

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as i:
            for linea in i:
                palabras_linea = linea.lower().split()
                if palabra in palabras_linea:
                    resultados.append((archivo, linea.strip()))

    if not resultados:
        print(f"No se encontró la palabra '{palabra}' en los archivos de la carpeta '{carpeta}'.")
    else:
        print(f"Resultados para la palabra '{palabra}':\n")
        for archivo, linea in resultados:
            print(f"[{archivo}] {linea}")

# Ejemplo de uso
buscar_palabra = "Quito"
carpeta = "data"
buscar_archivos(buscar_palabra, carpeta)

