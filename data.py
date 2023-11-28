import json

def parse_json(ruta, clave_principal):
    with open (ruta, "r") as archivo:
        diccionario_json = json.load(archivo)
    return diccionario_json[clave_principal]

diccionario_niveles = parse_json("data_niveles.json", "niveles")
#print(diccionario_niveles)

diccionario_set_up = parse_json("data_set_up.json", "set_up")
#print(diccionario_set_up)

ELEMENTO_PANTALLA = 0

ANCHO_VENTANA = diccionario_set_up[ELEMENTO_PANTALLA]["ANCHO_VENTANA"]
LARGO_VENTANA = diccionario_set_up[ELEMENTO_PANTALLA]["ALTO_VENTANA"]

FUENTES = 2
FUENTE_1 = diccionario_set_up[FUENTES]["1"]