def skaiciuok_palukanas(indelio_suma, metiniu_palukanu_procentas, menesiu_skaicius):
    vieno_men_palukanos = metiniu_palukanu_procentas / 12 / 100
    palukanu_suma = indelio_suma * vieno_men_palukanos * menesiu_skaicius
    indelio_su_palukanomis_suma = indelio_suma + palukanu_suma
    return indelio_su_palukanomis_suma


