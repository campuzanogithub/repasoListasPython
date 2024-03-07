# se declaran diccionarios = objetos
clienteUno = {
    "id": 5,
    "nombre":"edificio1",
    "consumo":200
}

clienteDos = {
    "id": 58,
    "nombre":"edificio2",
    "consumo":500
}

#se declara una lista = arreglo
clientesAsociados = [
    clienteUno, 
    clienteDos
]


# y ahora que hago cn esta lista?
# mi objetivo sera obtener la informacion de la lista
# recorrer una lista o arreglo
#print(clientesAsociados)

'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''

#programemos un FOREACH, 
#que es un for especializado en arreglos (listas)
for cliente in clientesAsociados: 
    print(cliente["id"],'->',cliente["consumo"],'KWH')
    print(f"{cliente["id"]} ->{cliente["consumo"]} KWH")