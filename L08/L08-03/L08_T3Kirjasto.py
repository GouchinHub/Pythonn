# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 31.10.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

def Celsius_Fahrenheit(Lampotila):
    M = Lampotila * (9/5) + 32
    return M

def Kelvin_Fahrenheit(Lampotila):
    M = Lampotila * (9/5) - 459.67
    return M

def Kelvin_Celsius(Lampotila):
    M = Lampotila - 273.15
    return M

def Celsius_Kelvin(Lampotila):
    M = Lampotila + 273.15
    return M

def Fahrenheit_Kelvin(Lampotila):
    M = (Lampotila + 459.67) * (5/9)
    return M

def Fahrenheit_Celsius(Lampotila):
    M = ((Lampotila -32) * 5) / 9
    return M

versio = 1.0
