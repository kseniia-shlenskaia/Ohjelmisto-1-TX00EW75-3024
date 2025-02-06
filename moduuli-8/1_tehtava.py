import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='kseniia',
    password='1234',
    autocommit=True,
    collation="utf8mb4_unicode_ci"
)

ICAO_koodi = input('Anna ICAO-koodi: ').upper()

sql = f"SELECT name, municipality FROM airport WHERE ident = '{ICAO_koodi}'"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchone()

if tulos:
    print(f'Lentoaseman nimi on {tulos[0]}, lentoaseman sijaintikunta on {tulos[1]}')
else:
    print('Lentoasemaa ei löydy')

kursori.close()
yhteys.close()