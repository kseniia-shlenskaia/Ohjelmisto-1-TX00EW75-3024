leiviskatPerNaula = 20
luoditPerNaula = 32
grammatPerLuoti = 13.3
grammatPerKg = 1000

leiviskat = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

grammatPerLeiviska = leiviskatPerNaula * luoditPerNaula * grammatPerLuoti
grammatPerNaula = luoditPerNaula * grammatPerLuoti
yhteensaGrammat = (leiviskat * grammatPerLeiviska) + (naulat * grammatPerNaula) + (luodit * grammatPerLuoti)

kilogrammat = int(yhteensaGrammat // grammatPerKg)
grammat = float(yhteensaGrammat % grammatPerKg)

print(f'Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa')
