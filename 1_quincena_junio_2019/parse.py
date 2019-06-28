import pymysql, os, json, codecs

# read JSON file which is in the next parent folder


# Estatus de los usuarios 1 = Vigente, 2= Movimientos 3= Baja
# SCRIPT PARA MODIFICAR LAS ALTAS

print("//////////////////////////////////////////////////")
print("SCRIPT PARA LAS MODIFICACIONES QUE SE SUBIRAN A REUS")
print("//////////////////////////////////////////////////")
print("**************************************************")                    

input("Teclea para continuar")

json_obj = json.load(codecs.open('Modificaciones.json', 'r', 'utf-8-sig'))

# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

for i, item in enumerate(json_obj['usuarios']['fila']):
	#print(item.get('nombres'))
    if i == 0:
        id = validate_string(item.get("id", None))
        estado = validate_string(item.get('estado', None))
        nombre = validate_string(item.get('nombres', None))
        paterno = validate_string(item.get('paterno', None))
        materno = validate_string(item.get('materno', None))
        rfc = validate_string(item.get('rfc', None))
        telefono_fijo = validate_string(item.get('telefono_fijo', None))
        extension = telefono_fijo.get('_ext') #Aqui voy a acceder al subdirectorio para poder acceder a LADA, esto por es un JSON ANIDADO
        lada = telefono_fijo.get('_lada') #Aquí estoy accediendo al elemento anidado
        telefono_movil = validate_string(item.get('telefono_movil', None))
        lada_movil = telefono_movil.get('_lada')
        correo_particular = validate_string(item.get('correo_particular', None))
        correo_oficina = validate_string(item.get('correo_oficina', None))
        fecha_inicio_vigencia = validate_string(item.get('fecha_inicio_vigencia', None))
        fecha_termino_vigencia = validate_string(item.get('fecha_termino_vigencia', None))
        fecha_registro = validate_string(item.get('fecha_registro', None))
        status = validate_string(item.get('status', None))



	

    
	

    #print(i,item.get('person'))
    #if item.get('person') == 'Jeff':
    
	#print(item.get('person'))
print(id)
print(estado)
print(nombre)
print(paterno)
print(rfc)
print(lada)
print(lada_movil)
print(correo_particular)
print(correo_oficina)
print(correo_oficina)
print(fecha_inicio_vigencia)
print(fecha_termino_vigencia)
print(fecha_registro)
print(status)
