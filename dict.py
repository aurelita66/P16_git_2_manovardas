miestai = {
    "didžiausi miestai": ["Vilnius", "Kaunas", "Klaipėda"],
    "mažesni miestai": ["Šiauliai", "Panevėžys", "Alytus"],
    "miesteliai": ["Prienai", "Kretinga"]
}


vartotojo_ivestas = input("Iveskite miesta: ")

for key, value in miestai.items():
    if vartotojo_ivestas in value:
        print(f"miestas priklauso {key}")
    else:
        print("Miestas nerastas!")
