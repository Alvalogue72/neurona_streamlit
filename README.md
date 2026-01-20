# Neurona Streamlit

Una aplicación interactiva desarrollada con Streamlit que simula el comportamiento de una neurona artificial.

## Descripción

Esta aplicación web permite experimentar con los conceptos fundamentales de las redes neuronales artificiales de manera visual e interactiva. Esta herramienta permite ajustar parámetros como entradas, pesos y sesgos para observar cómo estos afectan la salida de la neurona.

## Características

La aplicación cuenta con tres modos de operación organizados en pestañas:

### 1. Una entrada
- Simula una neurona con una única entrada y un peso.
- Permite ajustar el peso mediante un control deslizante.
- Calcula la salida como: `y = x * w`

### 2. Dos entradas
- Simula una neurona con dos entradas y dos pesos correspondientes.
- Permite ajustar ambos pesos y entradas de forma independiente.
- Calcula la salida como: `y = w₀ * x₀ + w₁ * x₁`

### 3. Tres entradas y sesgo
- Simula una neurona con tres entradas, tres pesos y un término de sesgo (bias).
- Proporciona control completo sobre todos los parámetros.
- Calcula la salida como: `y = w₀ * x₀ + w₁ * x₁ + w₂ * x₂ + b`

## Capturas de pantalla

A continuación se muestran ejemplos de la aplicación en funcionamiento:

### Modo una entrada
![Modo con una entrada](img/tab1.png)

### Modo dos entradas
![Modo con dos entradas](img/tab2.png)

### Modo tres entradas y sesgo
![Modo con tres entradas y sesgo](img/tab3.png)

## Instalación y Ejecución

### Ejecución con Docker Compose

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Alvalogue72/neurona_streamlit.git
   cd neurona_streamlit
   ```

2. **Construir y ejecutar el contenedor:**
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la aplicación:**
   
   Abre tu navegador y navega a:
   ```
   http://localhost:8501
   ```

4. **Detener la aplicación:**
   
   Presiona `Ctrl+C` en la terminal o ejecuta:
   ```bash
   docker-compose down
   ```

## Estructura del Proyecto

```
neurona_streamlit/
├── streamlit_app.py      # Aplicación principal de Streamlit
├── requirements.txt      # Dependencias de Python
├── Dockerfile           # Configuración de Docker
├── docker-compose.yml   # Configuración de Docker Compose
├── img/                 # Directorio de imágenes
│   └── neurona.webp    # Imagen de la neurona
│   └── tab1.webp       # Imagen de ejemplo
│   └── tab2.webp       # Imagen de ejemplo
│   └── tab3.webp       # Imagen de ejemplo
└── README.md           # Este archivo
```

## Tecnologías Utilizadas

- **Streamlit**: Framework para crear aplicaciones web interactivas en Python
- **Python 3.12**: Lenguaje de programación
- **Docker**: Plataforma de contenedores para facilitar el despliegue

## Uso de la Aplicación

1. Selecciona una de las tres pestañas según el número de entradas que desees explorar.
2. Ajusta los valores de los pesos utilizando los controles deslizantes.
3. Introduce los valores de las entradas en los campos numéricos.
4. Si estás en el modo de tres entradas, también puedes ajustar el sesgo.
5. Haz clic en el botón "Calcular la salida" para ver el resultado.
6. Experimenta con diferentes valores para comprender cómo afectan a la salida de la neurona.

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## Autor

Desarrollado por Alvalogue72
