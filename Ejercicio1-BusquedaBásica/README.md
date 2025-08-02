# 🧠 Ejercicio 1: Introducción a la Recuperación de Información

## 🎯 Objetivo de la práctica
- Entender el problema de buscar información en colecciones de texto.
- Comprender por qué se necesita un índice invertido en recuperación de información.
- Programar una primera solución manual y luego optimizarla con un índice.
- Evaluar la mejora en tiempos de búsqueda cuando usamos estructuras adecuadas.


## 📌 Parte 1: Búsqueda lineal en documentos
### 🔧 Actividad
1. Se te proporcionará un conjunto de documentos de texto.
2. Escribe una función que:
    - Lea todos los documentos.
    - Busque una palabra ingresada por el usuario.
    - Muestre en qué documentos aparece la palabra.
  
## 📌 Parte 2: Construcción de un índice invertido
### 🔧 Actividad
1. Escribe un programa que:
   - Recorra todos los documentos.
   - Construya un índice invertido, es decir, un diccionario donde:
      - Cada palabra clave apunta a una lista de documentos donde aparece.
3. Escribe una nueva función de búsqueda que:
   - Consulte directamente el índice para encontrar los documentos relevantes.
   - Sea mucho más rápida que la búsqueda lineal.
  
## 📌 Parte 3: Evaluación de tiempos de búsqueda
### 🔧 Actividad
1. Realiza la búsqueda de varias palabras usando:
   - Corpus pequeño: 16 documentos (turismo en Ecuador).
   - Corpus grande: 500 documentos (versión ampliada).
2. Mide el tiempo de ejecución:
   - Para búsqueda lineal.
   - Para búsqueda usando índice invertido.
   - Gráfica o presenta los resultados en una tabla comparativa.
### 📄 Ejemplo de palabras para buscar
      - quito
      - montañita
      - feriado
      - playas
      - aventura
      - galápagos

## 📌 Parte 4: Multiple Búsqueda
### 🔧 Actividad
1. Modifica el índice para que ignore mayúsculas/minúsculas (por ejemplo, "Playa" y "playa" deben considerarse iguales).
2. Permite consultas de múltiples términos (ejemplo: buscar documentos que contengan "playa" y "turismo").
3. Calcula el _speedup_

----

# 📄 Explicación Ejercicio

## 📂 Estructura del Proyecto

```
.
├── data/
│   ├── 01_corpus_turismo.txt
│   └── 01_corpus_turismo_500.txt
└── Ejercicio1-BusquedaBasica.py
```

> ✅ Todos los archivos `.txt` deben colocarse en la carpeta `data/`.

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
