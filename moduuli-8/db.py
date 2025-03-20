import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1', # localhost
    port=3306,
    database='flight_game',
    user='kseniia',
    password='1234',
    autocommit=True,
    collation="utf8mb4_unicode_ci"
)

# sql = "SELECT ident, name, iso_country FROM airport LIMIT 10 OFFSET 10"
sql = "SELECT ident, name, iso_country FROM airport LIMIT 10"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(sql)
print(tulos)
print(tulos[0])
print(tulos[:3])
print(tulos[1:3])
print(tulos[0][1])

for rivi in tulos:
    print(rivi)
    for alkio in rivi:
        print(alkio)


# print(SELECT * FROM flight_game;)

# def hello():
#     print(f"SELECT * FROM flight_game")

kursori.close()
yhteys.close()