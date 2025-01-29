LITER_PER_GALLON = 3.785

def gallons_to_liters(gallons):
    return gallons * LITER_PER_GALLON

def show_gallons_in_liters():
    while True:
        gallons = float(input('Anna gallonamäärä litroiksi muunnettavaksi tai negatiivinen arvo lopettaaksesi: '))
        if gallons < 0:
            break
        print(f'Gallona-arvosi litroina on {gallons_to_liters(gallons)}')

show_gallons_in_liters()