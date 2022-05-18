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

![pycallgraph](https://user-images.githubusercontent.com/97861517/166811211-55b90407-a95c-4c91-babf-a9bdb6275b8d.png)

Alternativamente se puede utilizar un simple profiler comocido como cProfile dentro del archivo cprofile.py, el cual nos regresa las llamadas de las funciones...

<img width="1025" alt="Screen Shot 2022-05-04 at 1 29 08 PM" src="https://user-images.githubusercontent.com/97861517/166811396-25dfd1d1-9e4f-4d94-b008-097a5efdf466.png">

<img width="205" alt="Screen Shot 2022-05-04 at 1 29 08 PM" src="https://user-images.githubusercontent.com/97846712/166832048-f7812465-201b-45ed-84c3-0c7358dc0753.png">

LA DOCUMENTACION DE LOS APIS SE ENCUENTRA EN:
https://documenter.getpostman.com/view/19550087/UyxnD51S
