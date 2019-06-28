# SCRIPTS DE PYTHON PARA PODER LEER JSON

En este repositorio tenemos scripts con los cuales vamos a poder leer JSON
Y manipularnos como nosotros deseemos, debemos recordar que cuando estamos trabajando con un
JSON anidado a veces tendremos que identificar de que tipo de dato es para que sepamos.
Una forma de identificarlo, sería la siguiente:
```python
print(type("tu json que quieres probar"))
```
De igual manera, si se desea poder recorrer los elementos porque debemos tomarlos como un arreglo sería así:
```python
if type(telefono_fijo) == dict:
		print(telefono_fijo.get('@ext'))
	else:
		#print(type(telefono_fijo))
		for item in telefono_fijo:
```
Si nosotros queremos concatenar nuestros tipos de archivos, lo que vamos a hacer es lo siguiente:
```python
print("{} - {} - {}".format(item.get('@ext'),item.get('@lada'),item.get('#text')))
```
