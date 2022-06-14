import csv

class Stop:
    def __init__(self, id, name, desc, lat, lon):
        self.id = id
        self.name = name
        self.desc = desc
        self.lat = lat
        self.lon = lon
    
    def to_string(self):
        print("Para el valor " + self.id)
        print("---------------------------------------")
        print("resultado de to_string-> " + str(self.id) + " " + str(self.name) + " " + str(self.desc) + " " + str(self.lat) + " "+ str(self.lon) + " ")

def crear_diccionario():
    diccionario = {
    '1020': {'description': 'PSEG ALAMEDA 14 (DAVANT JARDÍ VIA CENTRAL) - VALÈNCIA',
             'id': '1020',
             'lat': '4372694.493',
             'lon': '726668.229',
             'name': 'Albereda'},
    '1021': {'description': 'PSEG ALAMEDA 1(DAVANT JARDÍ VIA CENTRAL) - VALÈNCIA',
             'id': '1021',
             'lat': '4372960.453',
             'lon': '726489.285',
             'name': 'Pla del Reial'},
    '1026': {'description': 'CAMI RIBAS DAVANT  ADOR - CASTELLAR-OLIVERAL',
             'id': '1026',
             'lat': '4368090.933',
             'lon': '727158.752',
             'name': 'Ribàs (imparell) - Ador'},
    '1027': {'description': 'C  18 - VALÈNCIA',
             'id': '1027',
             'lat': '4368085.738',
             'lon': '726986.867',
             'name': 'Principal - El Caroig'},
    '1028': {'description': 'PL VIRGEN DE LEPANTO 7 - CASTELLAR-OLIVERAL',
             'id': '1028',
             'lat': '4367757.724',
             'lon': '726913.853',
             'name': 'Mare de Déu de Lepant (imparell) - Esc. F. Siurana'},
    '1029': {'description': 'C VICENTE PUCHOL 72 - CASTELLAR-OLIVERAL',
             'id': '1029',
             'lat': '4367435.072',
             'lon': '726877.702',
             'name': 'Vicent Puchol - Font de Bonet'},
    '1030': {'description': 'C CRISTO DEL REFUGIO 60 - CASTELLAR-OLIVERAL',
             'id': '1030',
             'lat': '4367200.126',
             'lon': '726906.174',
             'name': 'Crist del Refugi - Davant Sant Agustí'},
    '1032': {'description': 'C TIRIG 4 - VALÈNCIA',
             'id': '1032',
             'lat': '4373621.9',
             'lon': '727134.007',
             'name': 'Tírig - Guàrdia Civil'},
    '1035': {'description': 'AV ARAGÓN 22 (DAVANT INSTITUT) - VALÈNCIA',
             'id': '1035',
             'lat': '4372357.349',
             'lon': '727211.626',
             'name': 'Aragó - Finlàndia'},
    '1036': {'description': 'C URUGUAY 38 - VALÈNCIA',
             'id': '1036',
             'lat': '4370588.712',
             'lon': '724814.13',
             'name': 'Uruguai - Veneçuela'},
    '1038': {'description': 'C ARCHIDUQUE CARLOS 63 - VALÈNCIA',
             'id': '1038',
             'lat': '4371443.232',
             'lon': '723984.759',
             'name': 'Arxiduc Carles (imparell) - Tres Forques'},
    '1039': {'description': 'C ERNESTO FERRER 1 - VALÈNCIA',
             'id': '1039',
             'lat': '4372531.034',
             'lon': '727350.354',
             'name': 'Ernest Ferrer - Aragó'},
    '1041': {'description': 'GV RAMON Y CAJAL 25 - VALÈNCIA',
             'id': '1041',
             'lat': '4371764.019',
             'lon': '725195.021',
             'name': "Plaça d'Espanya"},
    '1042': {'description': 'AV REGNE DE VALENCIA 73 - VALÈNCIA',
             'id': '1042',
             'lat': '4371461.031',
             'lon': '726851.35',
             'name': 'Regne de València - Ciscar'},
    '1044': {'description': 'AV VICENTE ANDRES ESTELLES POLIESPORTIU - BURJASSOT',
             'id': '1044',
             'lat': '4376308.866',
             'lon': '722135.007',
             'name': 'Poliesportiu de Burjassot'},
    '1050': {'description': 'C MEDITERRANEO 4 - VALÈNCIA',
             'id': '1050',
             'lat': '4372087.375',
             'lon': '729539.815',
             'name': 'Mediterránia - Vicent Brull'},
    '1052': {'description': 'C EUGENIA VIÑES 109 (DAVANT BALNEARI) - VALÈNCIA',
             'id': '1052',
             'lat': '4372004.909',
             'lon': '730090.35',
             'name': 'Eugènia Viñes - Mare de Déu del Sufragi'},
    '1054': {'description': 'AV ARAGÓN 4 - VALÈNCIA',
             'id': '1054',
             'lat': '4372112.402',
             'lon': '727104.081',
             'name': 'Aragó - Saragossa'},
    '1055': {'description': 'AV ARAGÓN 34 - VALÈNCIA',
             'id': '1055',
             'lat': '4372582.617',
             'lon': '727355.834',
             'name': 'Aragó - Ernest Ferrer'},
    '1057': {'description': 'AV ARAGÓN 42 (ACCÉS) - VALÈNCIA',
             'id': '1057',
             'lat': '4372834.922',
             'lon': '727444.367',
             'name': 'Estadi de Mestalla'},
    '1060': {'description': 'C PEDRO CABANES 10 - VALÈNCIA',
             'id': '1060',
             'lat': '4375052.103',
             'lon': '725915.428',
             'name': 'Pere Cabanes - Mont Carmel'},
    '1061': {'description': 'C PEDRO CABANES 58 - VALÈNCIA',
             'id': '1061',
             'lat': '4374997.078',
             'lon': '725698.115',
             'name': 'Pere Cabanes - Sant Doménec Savio'},
    '1062': {'description': 'C PEDRO CABANES 88 - VALÈNCIA',
             'id': '1062',
             'lat': '4374905.938',
             'lon': '725403.439',
             'name': 'Pere Cabanes - Bisbe Laguarda'},
    '1067': {'description': 'AV ECUADOR  EL 93 (DAVANT) - VALÈNCIA',
             'id': '1067',
             'lat': '4375074.905',
             'lon': '724193.889',
             'name': 'Equador - Pintor Matarana'},
    '1080': {'description': 'C SAN VICENTE DE PAUL 15 - VALÈNCIA',
             'id': '1080',
             'lat': '4374553.414',
             'lon': '726119.689',
             'name': 'Sant Vicent de Paül - Peníscola'},
    '1083': {'description': 'AV ARAGÓN 25 - VALÈNCIA',
             'id': '1083',
             'lat': '4372578.4',
             'lon': '727276.222',
             'name': 'Aragó'},
    '1085': {'description': 'AV ARAGÓN 16 - VALÈNCIA',
             'id': '1085',
             'lat': '4372285.722',
             'lon': '727244.328',
             'name': 'Aragó - Xile'},
    '1087': {'description': 'AV SAN ANTONIO 140 (DAVANT) - MISLATA',
             'id': '1087',
             'lat': '4372858.716',
             'lon': '721698.011',
             'name': 'Sant Antoni - Pizarro'},
    '1091': {'description': 'CTRA MALILLA 60 - VALÈNCIA',
             'id': '1091',
             'lat': '4370047.781',
             'lon': '725499.184',
             'name': 'Malilla (parell) - Bernat Descoll'},
    '1096': {'description': 'C RAMON LLULL 31 (DAVANT) - VALÈNCIA',
             'id': '1096',
             'lat': '4373073.313',
             'lon': '728257.03',
             'name': 'Ramon Llull - Bernat Fenollar'}
    }
    return diccionario
    
def read_data(file):
    dic ={

    }
    """with open(f1, 'r') as file1:
        with open(f2,'r') as file2:
            reader1 = csv.reader(file1)
            reader2 = csv.reader(file2)
            for row in reader1:
                dic[row[0]] = {"description":row[3],
                                "id":"",
                                "lat":"",
                                "lon":"",
                                "name":row[2]}
    """
    return dic

def convert_to_object(clave, dic):
    elemento = dic.get(clave)
    s =  Stop(elemento["id"], elemento["name"], elemento["description"], elemento["lat"], elemento["lon"])
    return s

def get_name_description(clave, dic):
    print("Para la clave "+clave+":")
    print("---------------------")
    if dic.get(clave) == None: raise ValueError("No existe")
    print(dic.get(clave)["name"])
    print(dic.get(clave)["description"]) 
    return dic.get(clave)["name"], dic.get(clave)["description"]

def search_by_lon(lon, dic):
    clave = -1
    print("Para la longitud " + str(lon))
    print("-------------------")
    if type(lon)!=float: raise ValueError("No es de tipo float")
    for i in dic:
        if(float(dic.get(i)["lon"])==lon):
            clave = i
    if clave == -1: raise ValueError("No existe")
    
    return clave

def get_min(k, d):
    lista = []
    print("Para el valor " + k)
    print("------------")
    for i in d:
        dic={
            'description': d.get(i)['description'],
            'name': d.get(i)['name']
        }
        if i<k:
            lista.append(dic)

    if lista == []: raise ValueError("No hay elementos")

    return lista  


if __name__ == "__main__":
    f1 = "stops.csv"
    f2 = "stops_data.csv"
    diccionario = crear_diccionario()
    ###############ejercicio 3##################
    print("*********************************")
    print("EJERCICIO 3")
    print("*********************************")
    #1 para 1080 que sí existe
    try:
        nombre, descripcion = get_name_description('1080',diccionario)
    except ValueError as e:
        print("Ha saltado el error: " + str(e))
    #2 para 10 que no existe
    try:
        nombre, descripcion = get_name_description('10',diccionario)
    except ValueError as e:
        print("Ha saltado el error: " + str(e))

    print("*********************************")
    print("EJERCICIO 4")
    print("*********************************")
    #1 para una longitud buena
    try:
        clave = search_by_lon(728257.03, diccionario)
        print(clave)
    except ValueError as e:
        if str(e)=="No existe": print ("Error de clave: " + str(e))
        else: print ("Error de tipo: " + str(e))
    #2 para una longitud que no existe
    try:
        clave = search_by_lon(7282.03, diccionario)
        print(clave)
    except ValueError as e:
        if str(e)=="No existe": print ("Error de clave: " + str(e))
        else: print ("Error de tipo: " + str(e))
    #3 para longitud que no es float, en este caso se lo pasamos como string
    try:
        clave = search_by_lon("728257.03", diccionario)
        print(clave)
    except ValueError as e:
        if str(e)=="No existe": print ("Error de clave: " + str(e))
        else: print ("Error de tipo: " + str(e))

    print("*********************************")
    print("EJERCICIO 5")
    print("*********************************")
    #1 elemento que cumple la condicion
    try:
        lista = get_min('1023', diccionario)
        print(lista)
    except ValueError as e:
        print("Ha saltado el error: " + str(e))
    #2 elemento que no cumple la condicion
    try:
        lista = get_min('100', diccionario)
        print(lista)
    except ValueError as e:
        print("Ha saltado el error: " + str(e))
    print("*********************************")
    print("EJERCICIO 7")
    print("*********************************")
    s = convert_to_object("1080", diccionario)
    s.to_string()
    
    
    #diccionario = read_data(file)
