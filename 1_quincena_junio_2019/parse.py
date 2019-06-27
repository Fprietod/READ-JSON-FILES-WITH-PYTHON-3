import pymysql, os, json, codecs

# read JSON file which is in the next parent folder
file = os.path.abspath('test.json')
json_data=open(file).read()
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
	print(i)
	if i == 3455:
		print(item.get('nombres'))
    #print(i,item.get('person'))
    #if item.get('person') == 'Jeff':
    	#print(item.get('person'))
#     person = validate_string(item.get("person", None))
#     year = validate_string(item.get("year", None))
#     company = validate_string(item.get("company", None))
# print(person)
# print(year)
# print(company)