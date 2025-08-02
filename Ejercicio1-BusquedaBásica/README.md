
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
