from this import d
from flask import Flask, jsonify, request
from main import *
import json
import shortuuid
from flask import Flask, render_template, request, flash, redirect, url_for
#
import flask_profiler
import sqlite3
import threading


app = Flask(__name__)

app.config["DEBUG"] = True 

# Load the Treblle SDK to your Python app
INSTALLEDD_APPS = [
    'treblle',
]
 
# Enable the Treblle SDK middleware
MIDDLEWARE_CLASSES = [
    'treblle.middleware.TreblleMiddleware',
]

TREBLLE_INFO = {
    'api_key': os.environ.get('ReyFLHEdcrU7iDNmgN0Zr4wllQMGgkqC'),
    'project_id': os.environ.get('jGpVSR2BBcvYMrbA')
}

# app.config["flask_profiler"] = {
#     "enabled": app.config["DEBUG"],
#     "storage": {
#         "engine": "sqlite"
#     },
#     "ignore": [
# 	"^/static/.*"
# 	]
# }
# app.config["flask_profiler"] = {
#     "enabled": app.config["DEBUG"],
#     "storage": {
#         "engine": "sqlite"
#     },
#     "basicAuth":{
#         "enabled": True,
#         "username": "admin",
#         "password": "admin"
#     },
#     "ignore": [
# 	    "^/static/.*"
# 	]
# }

#  "basicAuth":{
    #     "enabled": True,
    #     "username": "admin",
    #     "password": "admin"
    # },

def ordenesJson():
    '''Convierte el array multidimensional de ordenes a un diccionario o nested struct que nos permite enviarlo como JSON'''
    #printOrdenes()
    ordenesDict = {"ID":[],"NOMBRE":[],"CANTIDAD":[], "ESTADO":[], "TOTAL":[]};
    #print('len(ordenes) ',len(ordenes))
    for key in ordenes.keys:
        item = list(ordenes.get_val(key))
        ordenesDict[list(ordenesDict)[0]].append(key)
        for i in range(0,4):
            ordenesDict[list(ordenesDict)[i+1]].append(item[i])    
    return(ordenesDict)

def inventarioJson():
    '''Convierte el linked list de inventario a un diccionario o nested struct que nos permite enviarlo como JSON'''
    invDict = {"PRODUCTO":[],"PRECIO":[],"INVENTARIO":[]};
    nodo = inventario.headval
    while nodo is not None:
        data = nodo.dataval
        for i in range(0, len(data)):
            invDict[list(invDict)[i]].append(data[i])
        nodo = nodo.nextval
    return(invDict)
    
@app.route('/ordenes', methods=['GET'])
def imprimirOrdenes():
    '''
    GET http://127.0.0.1:5000/ordenes
    Regresa el JSON conteniendo todas las ordenes'''
    # return jsonify(ordenesJson())
    # json_object = json.loads(ordenes, indent = 4) 
    # print(json_object)
    return jsonify(ordenesJson())

# despachar ordenes
@app.route('/ordenes/despachar', methods=['GET'])
def despacharOrden():
    if ordenesQueue.size() > 0:
        mensaje = "La orden",ordenesQueue.get(), "ha sido despachada."
        return jsonify({'message' : " ".join(mensaje)})
    else:
        return jsonify({'message' : "No hay órdenes en la lista de espera de despacho."})

# ordenes queue
@app.route('/ordenes/queue', methods=['GET'])
def queueOrden():
    if ordenesQueue.empty():
        return jsonify({'message' : 'No hay ordenes en la lista de espera'})
    else:
        return jsonify({'message' : ordenesQueue.queue})


# generar orden
@app.route('/ordenes/generar', methods=['PUT'])
def agregarOrden():
    '''
    API para generar ordenes
    Metodo PUT que solicita un nombre (de producto) y cantidad
    Ejemplo:
    PUT http://127.0.0.1:5000/ordenes/generar
    {
    "nombre":"cafe",
    "cantidad": 15
    }
    '''
    idA = str(uuid.uuid4())
    req = request.get_json(force=True)
    orden = {'NOMBRE' : req['nombre'],'CANTIDAD' : req['cantidad'],}
    prodA = mayus(str(list(orden.values())[0]))
    totalA = int(list(orden.values())[1])
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        if(int(productoInventario[2])>=totalA):
            if not ordenesQueue.full():
                total = totalA * float(productoInventario[1])
                ordenes.set_val(idA, {'PRODUCTO':prodA, 'CANTIDAD': totalA, 'ESTADO':'PENDIENTE', 'TOTAL':total})
                print(ordenes)
                inventario.listmodify(prodA,(int(productoInventario[2]) - totalA), 'Inventario')
                ordenesQueue.add(idA)
                return jsonify({'message' : "Orden agregada exitosamente"})
            else:
                return jsonify({'message' : "Límite de órdenes diario alcanzado"})

        else:
            return jsonify({'message' : "El producto que desea comprar no cuenta con suficiente existencias, lo sentimos."})
    else:
        return jsonify({'message' : "El producto que desea comprar no existe"})
    # ordenes.append([j for j in [orden,"PENDIENTE",0]])
    #    
# realizar pago
@app.route('/ordenes/pagar', methods=['PUT'])
def pagar():
    ''' API para pagar una orden
    Metodo PUT que solicita un "id" y una "tarjeta"
    Ejemplo:
    PUT http://127.0.0.1:5000/ordenes/pagar
    {
    "id": "DhjVjQwyJs",
    "tarjeta": "1414"
    }
    Notese que el numero de tarjeta debe ser "1414", esto es para simular una respuesta de VISANET y si se manda un numero de tarjeta invalido el API de VISANET no permitiria realizar un pago'''
    req = request.get_json(force=True)
    orden = {'ID' : req['id'],'TARJETA' : req['tarjeta'],}
    idR = str(list(orden.values())[0])
    tarjeta = str(list(orden.values())[1])
    if(tarjeta != '1414'):# SIMULACION DE RESPUESTA DE VISANET
        return(jsonify({'message' : "El metodo de pago no ha sido aceptado."}))
    g = 0
    values = list(ordenes.get_val(idR))
    if values is not None:
        values[2] = 'PAGADA'
        ordenes.set_val(idR, values)
        return(jsonify({"message" :"Orden pagada con exito"}))
    else:
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

# anular orden
@app.route('/ordenes/anular', methods=['PUT'])
def anular():
    '''API para anular una orden
    Metodo PUT que solicita un "id"
    ejemplo:
    PUT http://127.0.0.1:5000/ordenes/anular
    {
    "id":"DhjVjQwyJs"
    }'''
    req = request.get_json(force=True)
    orden = {'ID' : req['id']}
    idR = str(list(orden.values())[0])
    if ordenes.delete_val(idR):
        ordenesQueue.anular(idR)
        return(jsonify({"message" :"Orden eliminada con exito"}))
    else:
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

@app.route('/inventario', methods=['GET'])
def inventarioimprimirAPI():
    '''
    GET http://127.0.0.1:5000/inventario
    Metodo GET que regresa el JSON conteniendo todos los nodos del inventario'''
    print(inventarioJson())
    return jsonify(inventarioJson())


@app.route('/inventario/buscar', methods=['GET'])
def inventarioBuscarAPI():
        '''permite buscar si existe el producto dado'''
        req = request.get_json(force=True)
        orden = {'PRODUCTO' : req['producto']}
        producto = mayus(str(list(orden.values())[0]))
        if(producto in set(inventarioJson()['PRODUCTO'])):
            return(jsonify({"message" : "Este producto si existe en el inventario"}))
        else:
            return(jsonify({"message" : "Este producto no existe en el inventario"}))

@app.route('/inventario/agregar', methods=['PUT'])
def inventarioAgregrarAPI():
    '''API que permite agregar un NUEVO producto al inventario
    Metodo PUT que solicita un "producto", "precio" e "inventario",
    Ejemplo:
    PUT http://127.0.0.1:5000/inventario/agregar
    {
    "producto":"leche",
    "precio": 12,
    "inventario": 220
    },
    Tome en cuenta que el API no permite agregar un producto que ya exista'''
    req = request.get_json(force=True)
    orden = {'PRODUCTO' : req['producto'],'PRECIO' : req['precio'], 'INVENTARIO': req['inventario']}
    producto = mayus(str(list(orden.values())[0]))

    precio = float(list(orden.values())[1])
    inv = int(list(orden.values())[2])
    # if(inventario.listfind(producto) is not None):
    if(producto in set(inventarioJson()['PRODUCTO'])):
        return(jsonify({"message" : "Este producto ya existe en el inventario, por favor verifique"}))
    else:
        inventario.agregar([producto, precio, inv])
    return(jsonify({"message" : "Producto agregado con exito al inventario"}))

@app.route('/inventario/modificar', methods=['PUT'])
def inventarioModificar():
    '''API que permite modificar el inventario actual del producto dado,
    Metodo PUT que solicita un "producto" e "inventario"
    Ejemplo:
    PUT http://127.0.0.1:5000/inventario/modificar
    {
    "producto" : "leche",
    "inventario": 100
    }'''
    req = request.get_json(force=True)
    orden = {'PRODUCTO' : req['producto'],'INVENTARIO' : req['inventario']}
    prodA = mayus(str(list(orden.values())[0]))
    inv = int(list(orden.values())[1])
    if(inv < 0):
        return jsonify({'message' : "No puede haber un inventario negativo"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,inv, 'Inventario')
        return jsonify({'message' : "Nuevo inventario modificado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea modificar no existe"})

@app.route('/inventario/borrar', methods=['PUT'])
def inventarioBorrar():
    '''API que permite borrar el  producto dado,
    Metodo PUT que solicita un "producto" e "inventario"
    Ejemplo:
    PUT http://127.0.0.1:5000/inventario/borrar
    {
    "producto" : "leche"
    
    }'''
    req = request.get_json(force=True)
    orden = {'PRODUCTO' : req['producto']}
    prodA = mayus(str(list(orden.values())[0]))
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,None,'Borrar')
        return jsonify({'message' : "Inventario eliminado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea eliminar no existe"})

@app.route('/inventario/descuento', methods=['PUT'])
def inventarioDescuentos():
    '''API que permite realizar descuentos
    Metodo PUT que solicita un "producto" y "descuento" (dado como porcentaje)
    Ejemplo:
    PUT http://127.0.0.1:5000/inventario/descuento
    {
    "producto" : "leche",
    "descuento": 40
    }'''
    req = request.get_json(force=True)
    orden = {'PRODUCTO' : req['producto'],'DESCUENTO' : req['descuento']}
    prodA = mayus(str(list(orden.values())[0]))
    descuento = float(list(orden.values())[1])
    if(descuento > 100):
        return jsonify({'message' : "El descuento debe ser un porcentaje"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,float(productoInventario[1]) - (float(productoInventario[1]) * float(descuento)/100), 'Precio')
        return jsonify({'message' : "Descuento aplicado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea aplicar el descuento no existe"})

@app.route("/docs")
def docs():
    return render_template('api.html')

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000)
