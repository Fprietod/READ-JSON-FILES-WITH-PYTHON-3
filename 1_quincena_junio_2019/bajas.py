import pymysql, os, json, codecs
import pymysql.cursors

#sCRIPT PARA PODER METER LOS DATOS DE LAS BAJAS A LA TABLA
# Estatus de los usuarios 1 = Vigente, 2= Movimientos 3= Baja

print("**************************************************")
print("//////////////////////////////////////////////////")
print("SCRIPT PARA SUBIR LAS BAJAS A LA TABLA DE REUS")
print("//////////////////////////////////////////////////")
print("**************************************************")                    

input("Teclea para continuar")



json_obj = json.load(codecs.open('bajas.json', 'r', 'utf-8-sig'))


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
	id = validate_string(item.get('id', None))
	estado = validate_string(item.get('estado', None))
	nombre = validate_string(item.get('nombres',None))
	paterno = validate_string(item.get('paterno'))
	rfc = validate_string(item.get('rfc',None))
	telefono_fijo = validate_string(item.get('telefono_fijo', None)) #Aquí es de tipo diccionario por lo tanto el get si puede tomar solo un elemento
	if type(telefono_fijo) == dict:
		print(telefono_fijo.get('@ext'))
	else:
		#print(type(telefono_fijo))
		for item in telefono_fijo:
			print("{} - {} - {}".format(item.get('@ext'),item.get('@lada'),item.get('#text'))) #Porque list es un arreglo es necesario recorrerlo en un arreglo
	#print(type(telefono_fijo))
	#ext = telefono_fijo.get('@ext')
	
	telefono_movil = validate_string(item.get('telefono_movil', None))
	correo_particular = validate_string(item.get('correo_particular', None))
	correo_oficina = validate_string(item.get('correo_oficina'))

	fecha_inicio_vigencia = validate_string(item.get('fecha_inicio_vigencia', None))
	fecha_termino_vigencia = validate_string(item.get('fecha_termino_vigencia', None))
	fecha_registro = validate_string(item.get('fecha_registro', None))
	status = validate_string(item.get('status', None))

  






	

    
	
	
	 
		