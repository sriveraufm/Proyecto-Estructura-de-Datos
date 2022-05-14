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
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
	    "^/static/.*"
	]
}

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
    for j in range(1, len(ordenes)):
        for i in range(0,5):
            #print(ordenes[j][i])
            ordenesDict[list(ordenesDict)[i]].append(ordenes[j][i])
    return(ordenesDict)

def inventarioJson():
    '''Convierte el linked list de inventario a un diccionario o nested struct que nos permite enviarlo como JSON'''
    invDict = {"PRODUCTO":[],"PRECIO":[],"INVENTARIO":[]};
    nodo = inventario.headval.nextval
    while nodo is not None:
        for i in range(0, len(nodo.dataval)):
            invDict[list(invDict)[i]].append(nodo.dataval[i])
        nodo = nodo.nextval
    return(invDict)
    
@app.route('/ordenes', methods=['GET'])
def imprimirOrdenes():
    '''
    GET http://127.0.0.1:5000/ordenes
    Regresa el JSON conteniendo todas las ordenes'''
    registro.add('GET ORDENES, EXITOSO')
    return jsonify(ordenesJson())

# despachar ordenes
@app.route('/ordenes/despachar', methods=['GET'])
def despacharOrden():
    if ordenesQueue.size() > 0:
        mensaje = "La orden",ordenesQueue.get(), "ha sido despachada."
        registro.add('DESPACHO DE ORDEN, EXITOSO')
        return jsonify({'message' : " ".join(mensaje)})
    else:
        registro.add('DESPACHO DE ORDEN, FALLIDO')
        return jsonify({'message' : "No hay órdenes en la lista de espera de despacho."})

# ordenes queue
@app.route('/ordenes/queue', methods=['GET'])
def queueOrden():
    if ordenesQueue.empty():
        registro.add('GET ORDENES QUEUE, FALLIDO')
        return jsonify({'message' : 'No hay ordenes en la lista de espera'})
    else:
        registro.add('GET ORDENES QUEUE, EXITOSO')
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
    idA = shortuuid.ShortUUID().random(length=10)
    req = request.get_json(force=True)
    orden = {'NOMBRE' : req['nombre'],'CANTIDAD' : req['cantidad'],}
    prodA = mayus(str(list(orden.values())[0]))
    totalA = int(list(orden.values())[1])
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        if(int(productoInventario[2])>=totalA):
            if not ordenesQueue.full():
                total = totalA * float(productoInventario[1])
                ordenes.append([j for j in [idA,prodA,totalA,"PENDIENTE",total]])
                # valorPrueba=int(productoInventario[2]) - totalA
                # #print(valorPrueba)
                inventario.listmodify(prodA,(int(productoInventario[2]) - totalA), 'Inventario')
                guardar()
                ordenesQueue.add(idA)
                registro.add('AGREGAR ORDEN, EXITOSO')
                return jsonify({'message' : "Orden agregada exitosamente"})
            else:
                registro.add('AGREGAR ORDEN, FALLIDO')
                return jsonify({'message' : "Límite de órdenes diario alcanzado"})

        else:
            registro.add('AGREGAR ORDEN, FALLIDO')
            return jsonify({'message' : "El producto que desea comprar no cuenta con suficiente existencias, lo sentimos."})
    else:
        registro.add('AGREGAR ORDEN, FALLIDO')
        return jsonify({'message' : "El producto que desea comprar no existe"})
    # ordenes.append([j for j in [orden,"PENDIENTE",0]])
    
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
        registro.add('PAGAR ORDEN, FALLIDO')
        return(jsonify({'message' : "El metodo de pago no ha sido aceptado."}))
    g = 0
    for k in range(0,len(ordenes)):
        if ordenes[k][0]== idR:
            ordenes[k][3]="PAGADA"
            g = 1
            guardar()
            registro.add('PAGAR ORDEN, EXITOSO')
            return(jsonify({"message" :"Orden pagada con exito"}))
    if g==0:
        registro.add('PAGAR ORDEN, FALLIDO')
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
    g = 0
    for k in range(0,len(ordenes)):
        if ordenes[k][0]== idR:
            ordenes[k][3]="ANULADA"
            g = 1
            guardar()
            registro.add('ANULAR ORDEN, EXITOSO')
            return(jsonify({"message" :"Orden anulada con exito"}))
    if g==0:
        registro.add('ANULAR ORDEN, FALLIDO')
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

@app.route('/inventario', methods=['GET'])
def inventarioimprimirAPI():
    '''
    GET http://127.0.0.1:5000/inventario
    Metodo GET que regresa el JSON conteniendo todos los nodos del inventario'''
    registro.add('VER INVENTARIO, EXITOSO')
    return jsonify(inventarioJson())


@app.route('/inventario/buscar', methods=['GET'])
def inventarioBuscarAPI():
        '''permite buscar en el arbol si existe el producto dado'''
        req = request.get_json(force=True)
        orden = {'PRODUCTO' : req['producto']}
        producto = mayus(str(list(orden.values())[0]))
        if(bplustree.retrieve(producto) is not None):
            registro.add('BUSCAR PRODUCTO, EXITOSO')
            return(jsonify({"message" : "Este producto si existe en el inventario"}))
        else:
            registro.add('BUSCAR PRODUCTO, FALLIDO')
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
    if(bplustree.retrieve(producto) is not None):
        registro.add('AGREGAR INVENTARIO, FALLIDO')
        return(jsonify({"message" : "Este producto ya existe en el inventario, por favor verifique"}))
    else:
        if(inventario.headval.nextval is None):
            inventario.agregar([producto, precio, inv])
        else:
            inventario.agregar([producto, precio, inv])
        bplustree.insert(str(producto), str(producto))
        # bplustree.show()
        registro.add('AGREGAR INVENTARIO, EXITOSO')
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
        registro.add('MODIFICAR INVENTARIO, FALLIDO')
        return jsonify({'message' : "No puede haber un inventario negativo"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,inv, 'Inventario')
        guardar()
        registro.add('MODIFICAR INVENTARIO, EXITOSO')
        return jsonify({'message' : "Nuevo inventario modificado exitosamente"})
    else:
        registro.add('MODIFICAR INVENTARIO, FALLIDO')
        return jsonify({'message' : "El producto que desea modificar no existe"})

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
        registro.add('APLICAR DESCUENTO, FALLIDO')
        return jsonify({'message' : "El descuento debe ser un porcentaje"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,float(productoInventario[1]) - (float(productoInventario[1]) * float(descuento)/100), 'Precio')
        guardar()
        registro.add('APLICAR DESCUENTO, EXITOSO')
        return jsonify({'message' : "Descuento aplicado exitosamente"})
    else:
        registro.add('APLICAR DESCUENTO, FALLIDO')
        return jsonify({'message' : "El producto que desea aplicar el descuento no existe"})


@app.route('/registro', methods=['GET'])
def registroGet():
    '''Permite ver el registro del uso de apis'''
    return jsonify({'message' : " <- ".join(registro.get())})

flask_profiler.init_app(app)

@app.route("/docs")
def docs():
    return render_template('api.html')

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000)
