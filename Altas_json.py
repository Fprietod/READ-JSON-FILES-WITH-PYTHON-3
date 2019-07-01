import pymysql, os, json, codecs
import pymysql.cursors
import datetime
import logging

#sCRIPT PARA PODER METER LOS DATOS DE LAS BAJAS A LA TABLA
# Estatus de los usuarios 1 = Vigente, 2= Movimientos 3= Baja

print("**************************************************")
print("//////////////////////////////////////////////////")
print("SCRIPT PARA SUBIR CONTENIDO DE UN JSON ANIDADO A UNA BASE DE DATOS")
print("//////////////////////////////////////////////////")
print("**************************************************")                    

input("Presiona cualquier tecla para continuar")


def conexion():
    connection = pymysql.connect(host='',
                             user='',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection
   


def insert_table(array_rows):
      connection = conexion()
      try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT
                        INTO KONFIO.REUS
                    (
                        id, 
                        state, 
                        name, 
                        paternal_last_name, 
                        maternal_last_name, 
                        rfc, 
                        ext, 
                        lada, 
                        house_phone_number, 
                        personal_email, 
                        office_email, 
                        register_date, 
                        unregister_date, 
                        effective_date, 
                        status
                    )
                    VALUES (
                        %s, 
                        %s, 
                        %s, 
                        %s,
                        %s, 
                        %s, 
                        %s,
                        %s,
                        %s,
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s
                    );
                """
                cursor.executemany(sql,array_rows)
                connection.commit()
                logging.info(
                    "Record inserted successfully into REUS") 
               
      finally:
            connection.close()



json_obj = json.load(codecs.open('Tu arhivo.json', 'r', 'utf-8-sig'))                



# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

array_rows = []
for i, item in enumerate(json_obj['usuarios']['fila']):
      id = validate_string(item.get('id', None))
      estado = validate_string(item.get('estado', None))
      nombre = validate_string(item.get('nombres',None))
      paterno = validate_string(item.get('paterno'))
      rfc = validate_string(item.get('rfc',None))
      telefono_fijo = validate_string(item.get('telefono_fijo', None)) #Aquí es de tipo diccionario por lo tanto el get si puede tomar solo un elemento
      materno = item.get('materno')
      if type(telefono_fijo) == dict:
            extension_telefono_fijo_dict = validate_string(telefono_fijo.get('_ext'))
            lada_telefono_fijo_dict = telefono_fijo.get('_lada')
            texto_fijo_dict = telefono_fijo.get('__text')
            #print(type(extension_telefono_fijo_dict))
      else:
            #print(type(telefono_fijo))
            for item in telefono_fijo:
                  extension_telefono_fijo = validate_string(item.get('_ext'))
                  lada_telefono_fijo = validate_string(item.get('_lada'))
                  texto_fijo = validate_string(item.get('__text'))
                  #print(type(extension_telefono_fijo))
                   #Porque list es un arreglo es necesario recorrerlo en un arreglo
      
      

      
      
      
      

       
      

      

    
    



                                    

      


      correo_particular = validate_string(item.get('correo_particular', None))
      correo_oficina = validate_string(item.get('correo_oficina'))
      
      fecha_inicio_vigencia = validate_string(item.get('fecha_inicio_vigencia')).split("/") if item.get('fecha_inicio_vigencia') else None #Hacemos split y comprobamos que
      #Podamos separarlo en dado caso donde un objeto sea nulo
      fecha_inicio_vigencia = datetime.datetime(int(fecha_inicio_vigencia[2]),int(fecha_inicio_vigencia[1]),int(fecha_inicio_vigencia[0])) if fecha_inicio_vigencia  else None
      #Aquí ya le damos el formato que necesitamos, dependiendo nuestra posición para anexarlo a la fecha.
      fecha_termino_vigencia = validate_string(item.get('fecha_termino_vigencia')).split("/") if item.get('fecha_termino_vigencia') else None
      #Aquì ya estamos transformando nuestra variable
      fecha_termino_vigencia = datetime.datetime(int(fecha_termino_vigencia[2]), int(fecha_termino_vigencia[1]), int(fecha_termino_vigencia[0])) if fecha_termino_vigencia else None
    ################################################################################################################
      fecha_registro = validate_string(item.get('fecha_registro')).split("/") if item.get('fecha_registro')else None
      fecha_registro = datetime.datetime(int(fecha_registro[2]), int(fecha_registro[1]), int(fecha_registro[0])) if fecha_registro else None
      status = validate_string(item.get('status', None))
      
      t = (id,estado,nombre,paterno,materno,rfc,extension_telefono_fijo_dict, lada_telefono_fijo_dict,texto_fijo_dict,correo_particular,correo_oficina,fecha_inicio_vigencia,
        fecha_termino_vigencia,fecha_registro,status)
      array_rows.append(t)
     

insert_table(array_rows)




