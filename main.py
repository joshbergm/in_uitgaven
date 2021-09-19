# Variables - inkomsten per maand
inkomsten1 = 00.00
inkomsten2 = 00.00
inkomsten3 = 00.00
inkomsten4 = 00.00

# Variables - uitgaven per maand
uitgaven1 = 00.00
uitgaven2 = 00.00
uitgaven3 = 00.00
uitgaven4 = 00.00
uitgaven5 = 00.00
uitgaven6 = 00.00
uitgaven7 = 00.00
uitgaven8 = 00.00
uitgaven9 = 00.00
uitgaven10 = 00.00
uitgaven11 = 00.00
uitgaven12 = 00.00
uitgaven13 = 00.00
uitgaven14 = 00.00

sparen = 00.00 # Per maand

boodschappen1 = 00.00 # Week 1
boodschappen2 = 00.00 # Week 2
boodschappen3 = 00.00 # Week 3
boodschappen4 = 00.00 # Week 4

inkomsten = inkomsten1 + inkomsten2 + inkomsten3
uitgaven = uitgaven1 + uitgaven2 + uitgaven3 + uitgaven4 + uitgaven5 + uitgaven6 + uitgaven7 + uitgaven8 + uitgaven9 + uitgaven10 + uitgaven11 + uitgaven12 + uitgaven13 + uitgaven14
boodschappen = boodschappen1 + boodschappen2 + boodschappen3 + boodschappen4

totaal = inkomsten - uitgaven - sparen - boodschappen
sparen_jaar = sparen * 12

print("Je hebt deze maand als inkomsten: €" + str(round(inkomsten, 2)))
print("Je hebt deze maand als uitgaven: €" + str(round(uitgaven, 2)))
print("Je geeft deze maand €" + str(round(boodschappen, 2)) + " uit aan boodschappen")
print("Je hebt na een jaar gespaard: €" + str(round(sparen_jaar, 2)))
print("---------------------------------------")
print("Je houd aan het eind van de maand over: €" + str(round(totaal, 2)))
