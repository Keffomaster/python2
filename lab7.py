# Be användaren att mata in hur många paket mjölk som finns kvar. 
# Är det mindre än 10 skriv- Beställ 30 paket. 
# Är det mellan 10 och 20 skriv- Beställ 20 paket. 
# Annars skriv - Du behöver inte beställa någon mjölk.

mjölk = input ("Hur många mjölkpaket har du kvar?   ")

if int(mjölk) < 10:
    print ("Beställ 30 paket")
elif int(mjölk) == 11:
    print ("Beställ 20 paket")
elif int(mjölk) == 12:
    print ("Beställ 20 paket")
elif int(mjölk) == 13:
    print ("Beställ 20 paket")
elif int(mjölk) == 14:
    print ("Beställ 20 paket")    
elif int(mjölk) == 15:
    print ("Beställ 20 paket")
elif int(mjölk) == 16:
    print ("Beställ 20 paket")
elif int(mjölk) == 17:
    print ("Beställ 20 paket")
elif int(mjölk) == 18:
    print ("Beställ 20 paket")    
elif int(mjölk) == 19:
    print ("Beställ 20 paket")
elif int(mjölk) == 20:
    print ("Beställ 20 paket")       
else:
    print ("Du behöver inte beställa någon mjölk.")



