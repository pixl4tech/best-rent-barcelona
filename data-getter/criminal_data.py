import requests
import time

DATA_CRIMINAL_SERVICE_URL_PATH = \
    "https://a.gusc.cartocdn.com/vangdata/api/v1/map/ce952d952fa6f8e9534a1ba3cf0dcc1c:1523525347990/0/attributes"
AREA_COUNT = 60
DISTRICT_LIST = [
    "Ciutat Vella",
    "Eixample",
    "Sants-Montjuïc",
    "Les Corts",
    "Sarrià-Sant Gervasi",
    "Gràcia",
    "Horta-Guinardó",
    "Nou Barris",
    "Sant Andreu",
    "Sant Martí",
    "el Prat de Llobregat",
    "Sant Boi de Llobregat",
    "Gavà",
    "Santa Coloma de Gramenet",
    "Badalona",
    "Premià de Mar",
]

# parsed from DATA_CRIMINAL_SERVICE_URL_PATH (it's cache,
# if you need get data online, change CRIMINAL_DATA_STORE value to None)
CRIMINAL_DATA_STORE = [{'name_district': 'Segarra - Urgell', 'name_district_2': 'Segarra - Urgell', 'population': 58173, 'criminal_rate': 2.75, 'criminal_count': 1600}, {'name_district': 'Esplugues de Llobregat', 'name_district_2': 'Esplugues de Llobregat', 'population': 62660, 'criminal_rate': 4.24, 'criminal_count': 2655}, {'name_district': 'Osona', 'name_district_2': 'Osona', 'population': 153471, 'criminal_rate': 3.38, 'criminal_count': 5189}, {'name_district': 'Alt Urgell', 'name_district_2': 'Alt Urgell', 'population': 20428, 'criminal_rate': 2.38, 'criminal_count': 486}, {'name_district': 'Sant Boi de Llobregat', 'name_district_2': 'Sant Boi de Llobregat', 'population': 94499, 'criminal_rate': 3.86, 'criminal_count': 3644}, {'name_district': 'Horta-Guinardó', 'name_district_2': 'Horta-Guinardó', 'population': 167268, 'criminal_rate': 4.6, 'criminal_count': 7701}, {'name_district': 'Montsià', 'name_district_2': 'Montsià', 'population': 67918, 'criminal_rate': 4.28, 'criminal_count': 2904}, {'name_district': 'Sarrià-Sant Gervasi', 'name_district_2': 'Sarrià-Sant Gervasi', 'population': 148026, 'criminal_rate': 6.11, 'criminal_count': 9042}, {'name_district': 'Selva Litoral', 'name_district_2': 'Selva Litoral', 'population': 81600, 'criminal_rate': 9.17, 'criminal_count': 7486}, {'name_district': 'Bages', 'name_district_2': 'Bages', 'population': 173143, 'criminal_rate': 3.29, 'criminal_count': 5690}, {'name_district': 'Solsonès', 'name_district_2': 'Solsonès', 'population': 13391, 'criminal_rate': 2.88, 'criminal_count': 385}, {'name_district': 'Mataró', 'name_district_2': 'Mataró', 'population': 167588, 'criminal_rate': 5.56, 'criminal_count': 9314}, {'name_district': 'Baix Camp - Priorat', 'name_district_2': 'Baix Camp - Priorat', 'population': 198163, 'criminal_rate': 6.07, 'criminal_count': 12021}, {'name_district': 'Sant Feliu de Llobregat', 'name_district_2': 'Sant Feliu de Llobregat', 'population': 219969, 'criminal_rate': 2.38, 'criminal_count': 5243}, {'name_district': 'Gavà', 'name_district_2': 'Gavà', 'population': 183673, 'criminal_rate': 5.19, 'criminal_count': 9541}, {'name_district': 'Alt Penedès', 'name_district_2': 'Alt Penedès', 'population': 105705, 'criminal_rate': 4.87, 'criminal_count': 5146}, {'name_district': "Gironès - Pla de l'Estany", 'name_district_2': "Gironès - Pla de l'Estany", 'population': 213038, 'criminal_rate': 5.59, 'criminal_count': 11912}, {'name_district': 'Alt Empordà - Figueres', 'name_district_2': 'Alt Empordà - Figueres', 'population': 84952, 'criminal_rate': 6.48, 'criminal_count': 5506}, {'name_district': "Segrià - Garrigues - Pla d'Urgell", 'name_district_2': "Segrià - Garrigues - Pla d'Urgell", 'population': 255095, 'criminal_rate': 5.4, 'criminal_count': 13773}, {'name_district': 'La Noguera', 'name_district_2': 'La Noguera', 'population': 38955, 'criminal_rate': 2.54, 'criminal_count': 989}, {'name_district': "Vall d'Aran - Alta Ribagorça", 'name_district_2': "Vall d'Aran - Alta Ribagorça", 'population': 13635, 'criminal_rate': 3.35, 'criminal_count': 457}, {'name_district': 'Alt Empordà - Roses', 'name_district_2': 'Alt Empordà - Roses', 'population': 55166, 'criminal_rate': 7.1, 'criminal_count': 3915}, {'name_district': 'Alt Camp - Conca de Barberà', 'name_district_2': 'Alt Camp - Conca de Barberà', 'population': 64269, 'criminal_rate': 4.12, 'criminal_count': 2645}, {'name_district': 'Baix Empordà - La Bisbal', 'name_district_2': 'Baix Empordà - La Bisbal', 'population': 84434, 'criminal_rate': 4.87, 'criminal_count': 4115}, {'name_district': 'Martorell', 'name_district_2': 'Martorell', 'population': 126553, 'criminal_rate': 3.77, 'criminal_count': 4771}, {'name_district': 'Sants-Montjuïc', 'name_district_2': 'Sants-Montjuïc', 'population': 180997, 'criminal_rate': 10.49, 'criminal_count': 18984}, {'name_district': 'Sabadell', 'name_district_2': 'Sabadell', 'population': 311155, 'criminal_rate': 4.44, 'criminal_count': 13815}, {'name_district': 'Garrotxa', 'name_district_2': 'Garrotxa', 'population': 54875, 'criminal_rate': 3.14, 'criminal_count': 1723}, {'name_district': 'Garraf', 'name_district_2': 'Garraf', 'population': 144451, 'criminal_rate': 6.88, 'criminal_count': 9938}, {'name_district': 'Cerdanya', 'name_district_2': 'Cerdanya', 'population': 17719, 'criminal_rate': 3.55, 'criminal_count': 629}, {'name_district': 'Tarragonès', 'name_district_2': 'Tarragonès', 'population': 249689, 'criminal_rate': 7.86, 'criminal_count': 19622}, {'name_district': 'Granollers', 'name_district_2': 'Granollers', 'population': 298536, 'criminal_rate': 4.75, 'criminal_count': 14192}, {'name_district': 'Baix Ebre', 'name_district_2': 'Baix Ebre', 'population': 78378, 'criminal_rate': 4.54, 'criminal_count': 3557}, {'name_district': 'Badalona', 'name_district_2': 'Badalona', 'population': 252130, 'criminal_rate': 6.06, 'criminal_count': 15269}, {'name_district': 'Sant Martí', 'name_district_2': 'Sant Martí', 'population': 233928, 'criminal_rate': 8.72, 'criminal_count': 20409}, {'name_district': 'Pallars Jussà - Pallars Sobirà', 'name_district_2': 'Pallars Jussà - Pallars Sobirà', 'population': 20091, 'criminal_rate': 2.34, 'criminal_count': 470}, {'name_district': 'Terrassa', 'name_district_2': 'Terrassa', 'population': 240413, 'criminal_rate': 4.15, 'criminal_count': 9977}, {'name_district': 'Anoia', 'name_district_2': 'Anoia', 'population': 117361, 'criminal_rate': 3.36, 'criminal_count': 3944}, {'name_district': 'Baix Empordà - Sant Feliu', 'name_district_2': 'Baix Empordà - Sant Feliu', 'population': 48164, 'criminal_rate': 8.95, 'criminal_count': 4310}, {'name_district': "Terra Alta - Ribera d'Ebre", 'name_district_2': "Terra Alta - Ribera d'Ebre", 'population': 33703, 'criminal_rate': 2.56, 'criminal_count': 863}, {'name_district': 'el Prat de Llobregat', 'name_district_2': 'el Prat de Llobregat', 'population': 63080, 'criminal_rate': 10.61, 'criminal_count': 6690}, {'name_district': 'Cerdanyola', 'name_district_2': 'Cerdanyola', 'population': 176307, 'criminal_rate': 4.53, 'criminal_count': 7978}, {'name_district': 'Berguedà', 'name_district_2': 'Berguedà', 'population': 38972, 'criminal_rate': 2.12, 'criminal_count': 825}, {'name_district': 'Selva Interior', 'name_district_2': 'Selva Interior', 'population': 86094, 'criminal_rate': 4.46, 'criminal_count': 3842}, {'name_district': "l'Hospitalet de Llobregat", 'name_district_2': "l'Hospitalet de Llobregat", 'population': 252114, 'criminal_rate': 6.34, 'criminal_count': 15987}, {'name_district': 'Premià de Mar', 'name_district_2': 'Premià de Mar', 'population': 134409, 'criminal_rate': 4.09, 'criminal_count': 5491}, {'name_district': 'Arenys de Mar', 'name_district_2': 'Arenys de Mar', 'population': 139508, 'criminal_rate': 6.57, 'criminal_count': 9163}, {'name_district': 'Gràcia', 'name_district_2': 'Gràcia', 'population': 120918, 'criminal_rate': 5.96, 'criminal_count': 7205}, {'name_district': 'Cornellà de Llobregat', 'name_district_2': 'Cornellà de Llobregat', 'population': 85080, 'criminal_rate': 6.87, 'criminal_count': 5842}, {'name_district': 'Les Corts', 'name_district_2': 'Les Corts', 'population': 81642, 'criminal_rate': 8.87, 'criminal_count': 7244}, {'name_district': 'Ciutat Vella', 'name_district_2': 'Ciutat Vella', 'population': 100070, 'criminal_rate': 40.79, 'criminal_count': 40822}, {'name_district': 'Sant Andreu', 'name_district_2': 'Sant Andreu', 'population': 146731, 'criminal_rate': 6.58, 'criminal_count': 9652}, {'name_district': 'Eixample', 'name_district_2': 'Eixample', 'population': 264305, 'criminal_rate': 15.79, 'criminal_count': 41726}, {'name_district': 'Mollet del Vallès', 'name_district_2': 'Mollet del Vallès', 'population': 106595, 'criminal_rate': 4.41, 'criminal_count': 4697}, {'name_district': 'Nou Barris', 'name_district_2': 'Nou Barris', 'population': 164881, 'criminal_rate': 5.16, 'criminal_count': 8512}, {'name_district': 'Santa Coloma de Gramenet', 'name_district_2': 'Santa Coloma de Gramenet', 'population': 113822, 'criminal_rate': 4.43, 'criminal_count': 5043}, {'name_district': 'Rubí', 'name_district_2': 'Rubí', 'population': 176365, 'criminal_rate': 4.79, 'criminal_count': 8453}, {'name_district': 'Ripollès', 'name_district_2': 'Ripollès', 'population': 25017, 'criminal_rate': 2.32, 'criminal_count': 581}, {'name_district': 'El Baix Penedès', 'name_district_2': 'Baix Penedès', 'population': 99123, 'criminal_rate': 6.75, 'criminal_count': 6692}]


criminal_data = []
if CRIMINAL_DATA_STORE is None:
    for i in range(1, 61):
        criminal_dict = {}
        r = requests.get(f"{DATA_CRIMINAL_SERVICE_URL_PATH}/{i}")
        res = r.json()
        if res.get('errors'):
            continue
        criminal_dict['name_district'] = res['abp']
        criminal_dict['population'] = res['poblacion']
        criminal_dict['criminal_rate'] = res['porcentaje']
        criminal_dict['criminal_count'] = res['suma_total']
        criminal_data.append(criminal_dict)
        time.sleep(1)
else:
    criminal_data = CRIMINAL_DATA_STORE

research_list = []
for district_data in criminal_data:
    if district_data["name_district"] in DISTRICT_LIST:
        research_list.append(district_data)

print(research_list)


