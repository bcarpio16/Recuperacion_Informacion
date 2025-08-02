# Ejercicio 1: Introducción a la Recuperación de Información

## Objetivo de la práctica
* Entender el problema de buscar información en colecciones de texto.
* Comprender por qué se necesita un índice invertido en recuperación de información.
* Programar una primera solución manual y luego optimizarla con un índice.
* Evaluar la mejora en tiempos de búsqueda cuando usamos estructuras adecuadas.


## Parte 1: Búsqueda lineal en documentos
### Actividad
1. Se te proporcionará un conjunto de documentos de texto.
2. Escribe una función que:
    * Lea todos los documentos.
    * Busque una palabra ingresada por el usuario.
    * Muestre en qué documentos aparece la palabra.
  
## Parte 2: Construcción de un índice invertido
### Actividad
1. Escribe un programa que:

    * Recorra todos los documentos.
    * Construya un índice invertido, es decir, un diccionario donde:
        * Cada palabra clave apunta a una lista de documentos donde aparece.
2. Escribe una nueva función de búsqueda que:

    * Consulte directamente el índice para encontrar los documentos relevantes.
    * Sea mucho más rápida que la búsqueda lineal.
  
## Parte 3: Evaluación de tiempos de búsqueda
### Actividad
1. Realiza la búsqueda de varias palabras usando:
    * Corpus pequeño: 16 documentos (turismo en Ecuador).
    * Corpus grande: 500 documentos (versión ampliada).
2. Mide el tiempo de ejecución:
    * Para búsqueda lineal.
    * Para búsqueda usando índice invertido.
    * Gráfica o presenta los resultados en una tabla comparativa.
#### Ejemplo de palabras para buscar
* quito
* montañita
* feriado
* playas
* aventura
* galápagos

## Parte 4:
### Actividad
1. Modifica el índice para que ignore mayúsculas/minúsculas (por ejemplo, "Playa" y "playa" deben considerarse iguales).
2. Permite consultas de múltiples términos (ejemplo: buscar documentos que contengan "playa" y "turismo").
3. Calcula el _speedup_


# 📄 Búsqueda de Palabras en Corpus de Texto

## 🔎 Proyecto: Recuperación de la Información  
Este proyecto implementa una herramienta básica para buscar una palabra específica dentro de varios archivos `.txt` que conforman un corpus textual.  
Es ideal para prácticas en asignaturas como **Recuperación de la Información** o **Procesamiento de Lenguaje Natural (NLP)**.

---

## 📂 Estructura del Proyecto

```
.
├── data/
│   ├── 01_corpus_turismo.txt
│   └── 01_corpus_turismo_500.txt
├── buscar_palabra.py
└── README.md
```

> ✅ Todos los archivos `.txt` deben colocarse en la carpeta `data/`.

---

## 🚀 ¿Qué hace este script?

- Recorre todos los archivos `.txt` en una carpeta (`data/`).
- Busca una palabra determinada (sin distinguir entre mayúsculas y minúsculas).
- Devuelve las líneas que contienen la palabra, junto con el nombre del archivo donde fue encontrada.

---

## 🧠 Lógica del Código

```python
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
```

---

## ▶️ Ejecución

Puedes ejecutar el código desde un archivo `.py` o celda de Jupyter Notebook:

```python
buscar_palabra = "Quito"
carpeta = "data"
buscar_en_varios_archivos(buscar_palabra, carpeta)
```

---

## 📌 Requisitos

- Python 3.x
- Archivos `.txt` codificados en `UTF-8`

No requiere librerías externas. Solo se usa la biblioteca estándar de Python (`os`).

---

## 💡 Ejemplo de Salida

```
Resultados para la palabra 'quito':

[01_corpus_turismo.txt] Quito es la capital del Ecuador y una joya del turismo andino.
[01_corpus_turismo_500.txt] El centro histórico de Quito es patrimonio de la humanidad.
```

---

## ✅ Posibles mejoras

- Contar el número de apariciones por archivo.
- Buscar múltiples palabras clave.
- Implementar expresiones regulares o coincidencias parciales.
- Exportar los resultados a un archivo `.csv` o `.json`.

---

## 🧑‍💻 Autor

Byron Carpio  
Proyecto académico — Recuperación de la Información
