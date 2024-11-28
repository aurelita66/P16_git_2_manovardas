def skaiciuok_palukanas(indelio_suma, metiniu_palukanu_procentas, menesiu_skaicius):
    vieno_men_palukanos = metiniu_palukanu_procentas / 12 / 100
    palukanu_suma = indelio_suma * vieno_men_palukanos * menesiu_skaicius
    indelio_su_palukanomis_suma = indelio_suma + palukanu_suma
    return indelio_su_palukanomis_suma

# užd 5
# Parašyti funkciją amortizuok -
# priima skaičių - daikto vertę, metų skaičių,
# procentą ir pradėdama nuo pradinės daikto vertės,
# kiekvieniems metams atima nurodytą vertės procentą.


def amortizuok(daikto_verte, metu_skaicius, procentas):
    for metai in range(metu_skaicius):
        daikto_verte = daikto_verte - (daikto_verte * procentas / 100)
    return daikto_verte

# užd 6
# Parašyti funkciją keisk_stringa, kuri priima stringą. Funkcija turi
# 2 loginius jungiklius - atbulai, didziosiomis.
# Priklausomai nuo jungiklių grąžina perdirbtą stringą.


def keisk_stringa(stringas, atbulai=False, didziosiomis=False):

    if atbulai:
        stringas = stringas[::-1]
    if didziosiomis:
        stringas = stringas.upper()
    return stringas