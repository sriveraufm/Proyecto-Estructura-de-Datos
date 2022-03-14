# Proyecto-Estructura-de-Datos
## Integrantes: Javier Caniz y Sebastian Rivera
### Puede importar el archivo /Estructura de Datos- Proyecto.postman_collection.json para importar y testear los APIs con POSTMAN
### Acceda a http://127.0.0.1:5000/docs para ver la documentacion del programa

# PROFILING
## APIs
Para la medición del renidmiento de nuestros APIs utilizamos una librería bastante interactiva llamada flask-profiler
Puede acceder a la visualización del profiling en http://127.0.0.1:5000/flask-profiler/ 

<img width="1512" alt="Screen Shot 2022-03-14 at 2 44 49 PM" src="https://user-images.githubusercontent.com/97861517/158258785-f52218bd-dbc2-41d3-8bc0-f891249268c1.png">
<img width="1512" alt="Screen Shot 2022-03-14 at 2 45 16 PM" src="https://user-images.githubusercontent.com/97861517/158258812-4f60028c-7ee1-41f0-b48c-6d35336646e4.png">

## Funciones del main.py
Para realizar el profiling de las funciones se utilizó una librería que genera una imagen que nos permite visualizar las llamadas entre funciones
Para generar este archivo es necesario instalar GraphViz y pycallgraph y correr $ pycallgraph graphviz -- ./main.py
![pycallgraph](https://user-images.githubusercontent.com/97861517/158261924-9a088995-6b5e-479c-a7e8-1a4f3c65ea5d.png)
