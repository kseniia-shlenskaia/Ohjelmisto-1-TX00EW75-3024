import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='kseniia',
    password='1234',
    autocommit=True,
    collation="utf8mb4_unicode_ci"
)

kursori = yhteys.cursor()

ICAO_koodi_1 = input('Anna ensimmäinen ICAO-koodi: ').upper()
sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO_koodi_1}'"
kursori.execute(sql)
lentokentta_1 = kursori.fetchone()

ICAO_koodi_2 = input('Anna toinen ICAO-koodi: ').upper()
sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO_koodi_2}'"
kursori.execute(sql)
lentokentta_2 = kursori.fetchone()

if not lentokentta_1 or not lentokentta_2:
    print('Tuntematon arvo')
else:
    etaisyys = geodesic(lentokentta_1, lentokentta_2).kilometers
    print(f'Lentokenttien välinen etäisyys: {etaisyys:.2f} km')

kursori.close()
yhteys.close()
