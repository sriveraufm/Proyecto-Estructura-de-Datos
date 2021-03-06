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


from flask_cors import CORS, cross_origin
app = Flask(__name__)


app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

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

@app.route('/ordenes', methods=['GET'])
def imprimirOrdenes():
    '''
    GET http://127.0.0.1:5000/ordenes
    Regresa el JSON conteniendo todas las ordenes'''
    return jsonify(ordenes.get_table())

# despachar ordenes
@app.route('/ordenes/despachar', methods=['PUT'])
def despacharOrden():
    '''Despachar la orden con mayor prioridad'''
    global cadena
    if ordenesQueue.size > 0:
        solicitud = request.get_json(force=True)
        if solicitud['zonadestino'] not in set(ciudad.keys()):
            return jsonify({'message' : "No contamos con ruta disponible para la zona de destino y zona de origen solicidada."})
        else:
            ordenDespacho = ordenesQueue.extractMax()
            ordenPrev = ordenes.get_val(ordenDespacho['ID'])
            ordenes.set_val(ordenDespacho['ID'], {
                    'PRODUCTO':ordenPrev['PRODUCTO'], 
                    'CANTIDAD': ordenPrev['CANTIDAD'], 
                    'ESTADO':'DESPACHADA', # cambia el estado a pagada
                    'TOTAL': ordenPrev['TOTAL'],
                    'CLIENTE': ordenPrev['CLIENTE']
                })
            registroDespacho.append(ordenDespacho['ID'])
            registroClientes.insert(ordenPrev['CLIENTE'], ordenDespacho['ID'])
            cadenaMensaje = cadena.find_shortest_path(start = solicitud['zonaorigen'], end = solicitud['zonadestino'])
            cadenaMensaje = " ->> Zona: ".join(str(item) for item in cadenaMensaje)
            return jsonify({
            'ordenDespachada' : ordenDespacho['ID'],
            'TotalOrden' : ordenDespacho['TOTAL'],
            'rutaOptima': 'Zona: '+ cadenaMensaje
            })
    else:
        return jsonify({
            'message' : "No hay ??rdenes en la lista de espera de despacho."
            })


@app.route('/ordenes/despachadas/cliente', methods=['GET'])
def despachadasOrden():
    '''Ver las ordenes despachadas del cliente'''
    solicitud = request.get_json(force=True)
    ordenesDesp = registroClientes.retrieve(str(solicitud['cliente']).upper())
    if ordenesDesp is None:
        return jsonify({
            'alerta' : "No hay ??rdenes despachadas para este cliente."
            })
    else:
        return jsonify({ str(solicitud['cliente']).upper() : {
        'ordenesDespachadas' : ordenesDesp
        }})


@app.route('/rutas', methods=['GET'])
def rutasAB():
    global cadena
    solicitud = request.get_json(force=True)
    if solicitud['zonadestino'] not in set(ciudad.keys()):
        return jsonify({'message' : "No contamos con ruta disponible para la zona de destino y zona de origen solicidada."})
    else:
        return jsonify({
        'rutasPosibles': cadena.find_all_paths(start = solicitud['zonaorigen'], end = solicitud['zonadestino']),
        'rutaOptima':  cadena.find_shortest_path(start = solicitud['zonaorigen'], end = solicitud['zonadestino'])
        })


@app.route('/ordenes/despachar/rutas', methods=['GET'])
def rutas():
    global ciudad
    return jsonify(ciudad)

# ordenes queue
@app.route('/ordenes/queue', methods=['GET'])
def queueOrden():
    if ordenesQueue.empty():
        return jsonify({'message' : 'No hay ordenes en la lista de espera'})
    else:
        return jsonify({'queue' : ordenesQueue.queue()})


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
    idOrden = str(uuid.uuid4())
    solicitud = request.get_json(force=True)
    if str(solicitud['cliente']) == '':
        return jsonify({'alerta' : "Falta cliente"})
    if str(solicitud['producto']) == '':
        return jsonify({'alerta' : "Falta producto"})
    if str(solicitud['cantidad']) == '' or int(solicitud['cantidad']) <= 0:
        return jsonify({'alerta' : "Falta cantidad"})
    if inventario.exists(str(solicitud['producto']).upper()):
        if(int(inventario.get_val(str(solicitud['producto']).upper())['INVENTARIO'])>=int(solicitud['cantidad'])):
            if not ordenesQueue.full():
                totalOrden = int(solicitud['cantidad']) * float(inventario.get_val(str(solicitud['producto']).upper())['PRECIO'])
                ordenes.set_val(idOrden, {
                    'PRODUCTO':str(solicitud['producto']).upper(), 
                    'CANTIDAD': solicitud['cantidad'], 
                    'ESTADO':'PENDIENTE', 
                    'TOTAL': totalOrden,
                    'CLIENTE': str(solicitud['cliente']).upper()
                })
                #modificar la cantidad de inventario
                inventario.set_val(str(solicitud['producto']).upper(),
                {
                    'PRECIO' :  inventario.get_val(str(solicitud['producto']).upper())['PRECIO'],
                    'INVENTARIO' :  int(inventario.get_val(str(solicitud['producto']).upper())['INVENTARIO']) - int(solicitud['cantidad'])
                })
                return jsonify({'message' : "Orden agregada exitosamente"})
            else:
                return jsonify({'message' : "L??mite de ??rdenes diario alcanzado"})

        else:
            return jsonify({'message' : "El producto que desea comprar no cuenta con suficiente existencias, lo sentimos."})
    else:
        return jsonify({'message' : "El producto que desea comprar no existe"})
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
    solicitud = request.get_json(force=True)
    query = ordenes.get_val(solicitud['id'])
    if query is None:
        return(jsonify({"alerta" : "La orden no ha sido encontrada"}))
    else:
        if query['ESTADO'] == 'PAGADA':
            return(jsonify({"alerta" : "La orden ya ha sido pagada"}))
        elif query['ESTADO'] == 'DESPACHADA':
            return(jsonify({"alerta" : "La orden ya ha sido despachada"}))
        else:
            if(solicitud['tarjeta'] != '1414'):# SIMULACION DE RESPUESTA DE VISANET
                return(jsonify({'message' : "El metodo de pago no ha sido aceptado."}))
            g = 0
            if query is not None:
                query['ESTADO'] = 'PAGADA'
                ordenes.set_val(solicitud['id'], query)
                ordenesQueue.insert({
                            'ID': solicitud['id'],
                            'TOTAL': ordenes.get_val(solicitud['id'])['TOTAL']
                        })
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
    solicitud = request.get_json(force=True)
    if ordenes.delete(solicitud['id']):
        # ordenesQueue.anular(solicitud['id']) esto falta...
        return(jsonify({"message" :"Orden eliminada con exito"}))
    else:
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

@app.route('/inventario', methods=['GET'])
def inventarioimprimirAPI():
    '''
    GET http://127.0.0.1:5000/inventario
    Metodo GET que regresa el JSON conteniendo todos los nodos del inventario'''
    return jsonify(inventario.get_table())


@app.route('/inventario/buscar', methods=['GET'])
def inventarioBuscarAPI():
        '''permite buscar si existe el producto dado'''
        solicitud = request.get_json(force=True)
        if(inventario.exists(str(solicitud['producto']).upper())):
            return(jsonify({"message" : "Este producto si existe en el inventario"}))
        else:
            return(jsonify({"message" : "Este producto no existe en el inventario"}))

@app.route('/inventario/agregar', methods=['PUT'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
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
    solicitud = request.get_json(force=True)
    if(inventario.exists(str(solicitud['producto']).upper())):
        return(jsonify({"message" : "Este producto ya existe en el inventario, por favor verifique"}))
    else:
        inventario.set_val(
        key = str(solicitud['producto']).upper(), 
        val = {
            'PRECIO' : solicitud['precio'],
            'INVENTARIO' : solicitud['inventario']
        })
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
    solicitud = request.get_json(force=True)
    if inventario.exists(str(solicitud['producto']).upper()):
        if(int(solicitud['inventario']) < 0):
            return jsonify({'message' : "No puede haber un inventario negativo"})
        else:
            inventario.set_val(key = str(solicitud['producto']).upper(), val ={
                'PRECIO' : inventario.get_val(str(solicitud['producto']).upper())['PRECIO'],
                'INVENTARIO' : solicitud['inventario']
            })
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
    solicitud = request.get_json(force=True)
    if inventario.exists(str(solicitud['producto']).upper()) :
        inventario.delete(str(solicitud['producto']).upper())
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
    solicitud = request.get_json(force=True)
    if str(solicitud['descuento']) == '':
        return jsonify({'message' : "El producto que desea aplicar el descuento no existe"})
    if(float(solicitud['descuento']) > 100):
        return jsonify({'message' : "El descuento debe ser un porcentaje"})
    if inventario.exists(str(solicitud['producto']).upper()):
        inventario.set_val(str(solicitud['producto']).upper(), {
                'PRECIO' : float(inventario.get_val(str(solicitud['producto']).upper())['PRECIO']) - (float(inventario.get_val(str(solicitud['producto']).upper())['PRECIO'] ) * float(solicitud['descuento'])/100),
                'INVENTARIO' : inventario.get_val(str(solicitud['producto']).upper())['INVENTARIO']
            })
        return jsonify({'message' : "Descuento aplicado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea aplicar el descuento no existe"})

@app.route('/ordenes/despachar/registro', methods=['GET'])
def registroGet():
    '''Permite ver el registro de ordenes despachadas'''
    return jsonify({'message' : registroDespacho})


@app.route("/docs")
def docs(): 
    return render_template('api.html')

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000)
