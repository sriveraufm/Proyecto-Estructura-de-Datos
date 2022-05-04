# Proyecto-Estructura-de-Datos
## Integrantes: Javier Caniz y Sebastian Rivera
### Puede importar el archivo /Estructura de Datos- Proyecto.postman_collection.json para importar y testear los APIs con POSTMAN
### Acceda a http://127.0.0.1:5000/docs para ver la documentacion del programa

# PROFILING
## APIs
Para la medición del renidmiento de nuestros APIs utilizamos una librería bastante interactiva llamada flask-profiler
Puede acceder a la visualización del profiling en http://127.0.0.1:5000/flask-profiler/ 

<img width="1510" alt="Screen Shot 2022-05-04 at 7 42 00 AM" src="https://user-images.githubusercontent.com/97861517/166693995-71821c2e-edcf-4898-b07f-f4f1acdf6513.png">
<img width="1512" alt="Screen Shot 2022-05-04 at 7 42 14 AM" src="https://user-images.githubusercontent.com/97861517/166694014-446cbdfe-ecd1-48b1-ae26-331e95ac62cd.png">
<img width="1512" alt="Screen Shot 2022-05-04 at 7 42 41 AM" src="https://user-images.githubusercontent.com/97861517/166694025-9c3a3bf8-63dc-4a73-89ee-f4608ce6fea2.png">

## Funciones del main.py
Para realizar el profiling de las funciones se utilizó una librería que genera una imagen que nos permite visualizar las llamadas entre funciones
Para generar este archivo es necesario instalar GraphViz y pycallgraph y correr $ pycallgraph graphviz -- ./main.py

![pycallgraph](https://user-images.githubusercontent.com/97861517/166624004-e96fecc5-d1b3-436b-9ebf-1049bb7a382d.png)

Alternativamente se puede utilizar un simple profiler comocido como cProfile dentro del archivo cprofile.py, el cual nos regresa las llamadas de las funciones...

<img width="1062" alt="Screen Shot 2022-05-03 at 10 19 08 PM" src="https://user-images.githubusercontent.com/97861517/166624020-c3bde873-2777-48f7-90c5-b218f9f80dde.png">
