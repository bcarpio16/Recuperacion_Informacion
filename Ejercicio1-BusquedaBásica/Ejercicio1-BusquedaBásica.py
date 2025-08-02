import os

def buscar_en_varios_archivos(palabra, carpeta):
    palabra = palabra.lower()
    resultados = []

    archivos = [f for f in os.listdir(carpeta) if f.endswith(".txt")]

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
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
buscar_en_varios_archivos(buscar_palabra, carpeta)
#aasd

