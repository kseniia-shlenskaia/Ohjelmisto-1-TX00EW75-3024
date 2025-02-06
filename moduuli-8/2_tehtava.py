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

maakoodi = input('Anna maakoodi: ').upper()

sql = f"SELECT type FROM airport WHERE iso_country = '{maakoodi}'"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

typit = {}

for rivi in tulos:
    if rivi[0] not in typit:
        typit[rivi[0]] = 0

    typit[rivi[0]] += 1

for avain in typit:
    print(f'{avain.capitalize()}: {typit[avain]}')

kursori.close()
yhteys.close()
