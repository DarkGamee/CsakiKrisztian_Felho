# A keszit_diagram_sort függvény csinál egy sort a diagramhoz egy adott nap hőmérséklete alapján
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)  # A hőmérsékletet egész számra alakitjuk
    csillagok = '*' * csillagok_szama   # A hőmérséklet számának megfelelő számú csillagot generálunk
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"  # Létrehozzuk a sort: nap száma, csillagok, hőmérséklet
    return sor  # Visszatérünk a kész sorral

# A rajzolj_diagram függvény megjeleníti az egész diagramot a hőmérsékletekkel
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")  # Diagram cimének kiírása
    print("-" * 40)  #  40 karakter hosszú vonal hogy elválassza a címét a diagram többi részétől

    for i in range(len(homersekletek)):  # Végigiterálunk a hőmérsékleteken
        nap = i + 1  # ciklus indexéből 1-et adunk hozzá
        sor = keszit_diagram_sort(nap, homersekletek[i])  # Létrehozzuk az adott nap diagram sorát
        print(sor)  # Kiirjuk a sort a képernyőre

# A napi átlaghőmérsékletek egy listában vannak tárolva
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# Meghívjuk a rajzolj_diagram függvényt, hogy megjelenítse a diagramot
rajzolj_diagram(napi_atlaghomersekletek)


