# Proyecto-Estructura-de-Datos
## Integrantes: Javier Caniz y Sebastian Rivera
### Puede importar el archivo /Estructura de Datos- Proyecto.postman_collection.json para importar y testear los APIs con POSTMAN
### Acceda a http://127.0.0.1:5000/docs para ver la documentacion del programa
#### Presentacion: https://docs.google.com/presentation/d/15u5ZwAtxbyW5MZj4zBSsUxbP5ZU1cFVNlMksBQV2jDY/edit#slide=id.g12c76b1608f_0_5
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

![pycallgraph](https://user-images.githubusercontent.com/97861517/169164666-72aa94e8-dd32-4bf5-8ee9-075022704067.png)


Alternativamente se puede utilizar un simple profiler comocido como cProfile dentro del archivo cprofile.py, el cual nos regresa las llamadas de las funciones...

<img width="1025" alt="Screen Shot 2022-05-04 at 1 29 08 PM" src="https://user-images.githubusercontent.com/97861517/166811396-25dfd1d1-9e4f-4d94-b008-097a5efdf466.png"> </img>

<img width="205" alt="Screen Shot 2022-05-04 at 1 29 08 PM" src="https://user-images.githubusercontent.com/97846712/166832048-f7812465-201b-45ed-84c3-0c7358dc0753.png">
</img>

# DOCUMENTACION
PUEDE VER LA DOCUMENTACION DE LOS APIS EN:
https://documenter.getpostman.com/view/19550087/UyxnD51S

# TESTING


![Screenshot 2022-05-18 173032](https://user-images.githubusercontent.com/97861517/169171848-e3eff95f-2bb2-444b-8d0b-8f77834de865.png)

![Screenshot 2022-05-18 173041](https://user-images.githubusercontent.com/97861517/169171861-3c1c0438-9af4-426f-9cba-fb78cad0daff.png)
![Screenshot 2022-05-18 173053](https://user-images.githubusercontent.com/97861517/169171870-1512bb1c-a147-4023-b5c2-7350f3974347.png)
![Screenshot 2022-05-18 173059](https://user-images.githubusercontent.com/97861517/169171872-4e9a6942-979d-4630-b299-7572eb7f4521.png)
![Screenshot 2022-05-18 173108](https://user-images.githubusercontent.com/97861517/169171877-5105c4d7-6e17-4ac1-b96c-36b76850d408.png)

![Screenshot 2022-05-18 173113](https://user-images.githubusercontent.com/97861517/169171882-904c4fb8-985e-42e5-9ac8-437ff1e098bf.png)
![Screenshot 2022-05-18 173121](https://user-images.githubusercontent.com/97861517/169171888-d66ddd40-70a7-4709-9804-492a9f5a7bea.png)


