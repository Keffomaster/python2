#Skriv in Mata in tal 1:
#Ta emot detta tal i en variabel
#Skriv in Mata in tal 2:
#Ta emot värdet på detta tal
#Nu ska ni göra massa beräkningar på dessa tal. OBS: lägg resultat i en variabel innan ni skriver ut resultat = tal1 * tal2

#räkna tal1 upphöjd till tal 2 och skriv ut
#räkna tal1 gånger tal 2 och skriv ut
#räkna tal1 delat med tal 2 och skriv ut  (OBS!!! Kolla datatypen på resultat)
#räkna tal1 plus tal 2 och skriv ut
#räkna tal1 minus tal 2 och skriv ut
#räkna tal1  heltalsdividerat (%)  tal 2 och skriv ut
#räkna ut resten från heltalsdivision (//) mellan tal1 och  tal 2 och skriv ut  

import fileinput


tal1 = input ("Mata in tal 1: ")
tal2 = input ("Mata in tal 2: ")

print (int(tal1) - int(tal2))
print (int(tal1) * int(tal2))
print (int(tal1) + int(tal2))
print (int(tal1) / int(tal2))

