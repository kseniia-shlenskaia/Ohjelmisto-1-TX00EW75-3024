# hedelmät = ("Appelsiini", "Banaani", "Omena")
# (eka, toka, kolmas) = hedelmät
# print ({eka})

# hedelmät2 = ["Appelsiini", "Banaani", "Omena"]
# eka1, toka1, dskjdsc1 = hedelmät2
# print (eka1)

# import random
#
# def heitä():
#     eka, toka = random.randint(1,6), random.randint(1,6)
#     return eka, toka
#
# noppa1, noppa2 = heitä()
# print(f"Nopista tuli {noppa1} ja {noppa2}.")

# pelit = {"Monopoli", "Shakki", "Cluedo", "Shakki", "Cluedo"}
# pelit2 = {"Monopoli", "Shakki2", "Cluedo", "Shakki4", "Cluedo5"}
#
# print(pelit.intersection(pelit2))

def get_avain():
    return 'qqq'

numerot = {"Viivi":"050-1234567"}
key = 'Viivi'
numerot[key] = get_avain()

print(numerot['Viivi'])
print(type(numerot['Viivi']))

# for key in numerot:
#     print(numerot[key])
#
# print("Viivi" in numerot)
# print("Mike" in numerot)
