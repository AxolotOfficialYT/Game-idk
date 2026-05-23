import msvcrt
import os
import random
import time

zdarzenia = []

def reset():
    global swiat, kroki, skarby, zabici, zasieg, głód, zasieg
    global currx, curry, prevx, prevy, ostatnikrok
    global czytrwa, iletrwa, wpróżni, zdarzenia
    
    zdarzenia = []
    swiat = {}
    kroki = 0
    skarby = 0
    zabici = 0
    zasieg = 2
    głód = 100
    czytrwa = False
    iletrwa = 0
    wpróżni = False
    ostatnikrok = "Nieznany"
    prevx = "Nieznany"
    prevy = "Nieznany"

# Główna pętla programu, pozwala na resetowanie gry bez konieczności ponownego uruchamiania programu
while True:
    reset()
    #jakaś def co później używam
    def ObiektyObok(x, y):
        count = 0
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                if y1 == y and x1 == x:
                    continue
                if swiat.get((x1, y1), 'empty') != 'empty' and swiat.get((x1, y1), 'empty') != 'V' and swiat.get((x1, y1), 'empty') != '.':
                    count += 1
        return count

    print(""" \nWitaj w Explorer!

Jesteś bohaterem eksplorującym tajemniczy świat.
Twoim celem jest zebranie 5 skarbów rozsianych po mapie.

Granice świata: od -100 do 100 na osi x i y.
Wyjście poza granice grozi śmiercią.

Twój bohater zaczyna z wybraną przez ciebie ilością punktów zdrowia (50-150). Utrata wszystkich punktów zdrowia oznacza śmierć.
Na swojej drodze napotkasz przeszkody, przeciwników i skarby. Walcz z przeciwnikami, unikaj przeszkód i zbieraj skarby, aby osiągnąć swój cel.
Pamiętaj, że głód jest realnym zagrożeniem - musisz znaleźć jedzenie, aby go zaspokoić, lub stopniowo będziesz tracić zdrowie.
        
Zacznijmy od ustawienia parametrów wyprawy.\n""")
    time.sleep(3)

    while True:
        imie = input("Jak chcesz się nazywać? ")
        time.sleep(0.5)
        print(f"\nCzy na pewno chcesz nazywać się {imie}? (tak/nie)")

        odpowiedz = input().lower()
        if odpowiedz == "tak":
            break
        elif odpowiedz == "nie":
            print("\nDobrze, wybierz inne imię.")
            time.sleep(1)
        else:
            print("\nNie rozumiem odpowiedzi, proszę wpisać 'tak' lub 'nie'.")
            time.sleep(1)
            
    nazwa_wyprawy = input("\nPodaj nazwę swojej wyprawy: ")

    print(f"\nWitaj, {imie}! Przygotuj się do wyprawy!\n")
    time.sleep(1)

    while True:
        try:
            zdrowie = int(input("Proszę wprowadzić ilość punktów zdrowia, z jaką chcesz rozpocząć grę (można podać od 50 do 150, rekomendowane 100): "))
            if zdrowie <= 150 and zdrowie >= 50:
                break
            print("\nBłąd, wartość poza zakresem.\n")
        except ValueError:
            print("\nBłąd, proszę wpisać liczbę całkowitą.\n")

    #początkowa pozycja
    while True:
        try:
            currx = int(input("\nProszę wprowadzić początkowe kordynaty x \nna którym postać ma wystartować (można podać od -100 do 100): "))
            if currx <= 100 and currx >= -100:
                break
            print("\nBłąd, wartość poza zakresem.\n")
        except ValueError:
            print("\nBłąd, proszę wpisać liczbę całkowitą.\n")

    #początkowa pozycja
    while True:  
        try:
            curry = int(input("\nProszę wprowadzić początkowe kordynaty y \nna którym postać ma wystartować (można podać od -100 do 100): "))
            if curry <= 100 and curry >= -100:
                break
            print("\nBłąd, wartość poza zakresem.\n")
        except ValueError:
            print("\nBłąd, proszę wpisać liczbę całkowitą.\n")
            
    startx = currx
    starty = curry
    starthp = zdrowie

    #początkowa generacja otoczenia (żeby ktoś nie pojawił sie w czyms albo cos)
    swiat = {}
    for y in range(curry - 2, curry + 3):
        for x in range(currx - 2, currx + 3):
            if x > 100 or x < -100 or y > 100 or y < -100:
                swiat[(x,y)] = 'V'
            else:
                swiat[(x,y)] = '.'



    #Generacja świata GŁÓWNA
    listapol = []

    for x2 in range(-100, 101):
        for y2 in range(-100, 101): 
            listapol.append((x2, y2))

    ileskarbow = 0
    #Kloc generacji świata, pewnie można to było zrobić lepiej, ale nie chciało mi się już tego poprawiać, a działa więc jest ok
    while True:
        print("Generuję świat, proszę czekać...")
        random.shuffle(listapol)
        for (x, y) in listapol:
            if swiat.get((x, y), 'empty') == 'empty':
                
                stuff = ObiektyObok(x, y)
                chance = 0.15
                if stuff == 1:
                    chance += 0.07
                elif stuff == 2:
                    chance += 0.101
                elif stuff == 3:
                    chance += 0.23
                elif stuff == 4:
                    chance += 0.32
                elif stuff == 5:
                    chance += 0.40
                elif stuff == 6:
                    chance += 0.20 
                elif stuff == 7:
                    chance += 0.10
                elif stuff == 8:
                    chance = 0
                if random.random() < chance:
                    swiat[(x, y)] = 'X'
                else:
                    chance = 0.01
                    if stuff == 1:
                        chance += 0.02
                    elif stuff == 2:
                        chance += 0.03
                    elif stuff == 3:
                        chance += 0.05
                    elif stuff == 4:
                        chance += 0.06
                    elif stuff == 5:
                        chance += 0.03
                    elif stuff == 6:
                        chance += 0.02
                    elif stuff == 7:
                        chance += 0.01
                    elif stuff == 8:
                        chance = 0
                    if random.random() < chance:
                        swiat[(x, y)] = '!'
                    else:
                        chance = 0.001
                        if stuff == 1:
                            chance += 0.005
                        elif stuff == 2:
                            chance += 0.016
                        elif stuff == 3:
                            chance += 0.025
                        elif stuff == 4:
                            chance += 0.030
                        elif stuff == 5:
                            chance += 0.080
                        elif stuff == 6:
                            chance += 0.045
                        elif stuff == 7:
                            chance += 0.020
                        elif stuff == 8:
                            chance += 0.002
                        if random.random() < chance:
                            swiat[(x, y)] = 'T'
                            ileskarbow += 1
                        else:
                            if random.random() < 0.05:
                                swiat[(x, y)] = 'J'
                            else:
                                swiat[(x, y)] = '.'
        if ileskarbow >= 30:
            break
        else:
            swiat.clear()
            
    #ooo bedzie granko
    print("Świat został wygenerowany, można zaczynać grę!")
    time.sleep(2)

    #wyświetlanie świata, pokazuje na dany zasięg wokół gracza, reszta jest niewidoczna, ale istnieje, można tam iść i wtedy się pokaże
    def display(zasieg):
        
        for y in range(curry + zasieg, curry - zasieg - 1, -1):
            wiersz = ''
            for x in range(currx - zasieg, currx + zasieg + 1):
                if (x, y) == (currx, curry):
                    wiersz += ' @'
                else:
                    wiersz += (' ') + swiat.get((x, y), 'V')
            print(wiersz)
        print("\nLegenda: \n@ - gracz\n. - puste pole\nX - przeszkoda\n! - przeciwnik\nJ - jedzenie\nT - skarb\nV - próżnia (poza światem, śmiertelne)\n Aktualne kordynaty: x =", currx, "y =", curry, "\n")

    skarby = 0
    zabici = 0
    zasieg = 2

    os.system('cls')


    #horrory z tym miałem 
    def testhim(min_czas):
        while True:
            print("\nNaciśnij dowolny klawisz jak najszybciej po sygnale.")
            time.sleep(2)
            print("Czekaj...")
            
            czekaj = random.uniform(1, 3)
            start_czekaj = time.time()
            kliknięto_za_wczesnie = False
            
            while time.time() - start_czekaj < czekaj:
                if msvcrt.kbhit():
                    msvcrt.getch()
                    kliknięto_za_wczesnie = True
                    break
                time.sleep(0.05)
            
            if kliknięto_za_wczesnie:
                print("Za wcześnie! Spróbuj ponownie.")
                time.sleep(1)
                continue  # retry
            
            while msvcrt.kbhit():
                msvcrt.getch()
            
            print("TERAZ!")
            start = time.time()
            while True:
                if msvcrt.kbhit():
                    msvcrt.getch()
                    reakcja = time.time() - start
                    print(f"Czas reakcji: {reakcja:.3f}s")
                    time.sleep(1)
                    return reakcja <= min_czas
            
    ostatnikrok = ("Nieznany")
    czytrwa = False
    głód = 100
    kroki = 0
    prevx = ("Nieznany")
    prevy = ("Nieznany")

    print(f"""
    === WYPRAWA ROZPOCZĘTA ===
    Bohater: {imie}
    Pozycja startowa: ({currx}, {curry})
    HP: {zdrowie}
    Głód: 100
    Cel: Zebrać 5 skarbów
    Granice świata: -100 do 100
    ==========================
    """)
    time.sleep(3)

    wpróżni = False

    # Główna pętla gry
    while True:
        # ruch wszystkich przeciwników, nie fajnie sie to robiło
        for (x, y) in list(swiat.keys()):
            if swiat.get((x, y)) == '!':

                if random.random() < 0.35:

                    kierunki = [(0,1),(0,-1),(1,0),(-1,0)]
                    random.shuffle(kierunki)

                    for dx, dy in kierunki:

                        nx, ny = x + dx, y + dy #fancy ahh
                        if swiat.get((nx, ny)) == '.':

                            swiat[(x, y)] = '.'
                            swiat[(nx, ny)] = '!'
                            break
        
        display(zasieg)
        print("\n Ostatni krok:", ostatnikrok,", Ostatnia pozycja: x =", prevx, "y =", prevy)
        print(f"\nZdrowie: {zdrowie}\nSkarby: {skarby}\nPokonani przeciwnicy: {zabici}\nGłód: {głód}{' !! <-----' if głód <= 0 else ' <-----' if głód < 30 else ''}\nImię: {imie}\nKroki: {kroki}")
        movdirec = input("Wprowadź kierunek ruchu (w, a, s, d): ")
        moved = 0
        prevx = currx
        prevy = curry
        if movdirec == 'w':
            curry += 1
            moved = ("w")
            kroki += 1
            ostatnikrok = ("Do góry")

        elif movdirec == 's':
            curry -= 1
            moved = ("s")
            kroki += 1
            ostatnikrok = ("W dół")

        elif movdirec == 'a':
            currx -= 1
            moved = ("a")     
            kroki += 1  
            ostatnikrok = ("W lewo")

        elif movdirec == 'd':
            currx += 1
            moved = ("d")
            kroki += 1
            ostatnikrok = ("W prawo")
        os.system('cls')

        if swiat.get((currx, curry), 'empty') == 'X':
            zdrowie -= 10
            print("\nUderzyłeś w przeszkodę! Straciłeś 10 zdrowia.")
            zdarzenia.append(f"Tura {kroki}: Uderzenie w przeszkodę, -10 HP")
            time.sleep(1)
            if moved == 'w':
                curry -= 1
                kroki += 1
            elif moved == 's':
                curry += 1 
                kroki += 1
            elif moved == 'a':
                currx += 1
                kroki += 1
            elif moved == 'd':
                currx -= 1
                kroki += 1
        elif swiat.get((currx, curry), 'V') == 'V':
            print("Wpadłeś w próżnię! Spróbuj się wydostać!")
            time.sleep(1.5)
            if testhim(0.5) == True:
                print("Udało ci się wydostać z próżni!")
                zdarzenia.append(f"Tura {kroki}: Wpadnięcie w próżnię, ale wydostanie się z niej!")
                time.sleep(2)
            else:
                zdrowie -= 80
                if zdrowie <= 0:
                    wpróżni = True
                    break
                print("\nPróżnia ciebe prawie pochłoneła! Straciłeś 80 zdrowia.")
                zdarzenia.append(f"Tura {kroki}: Wpadnięcie w próżnię, stracenie 80 HP")
            time.sleep(2)
            if moved == 'w':
                curry -= 1
            elif moved == 's':
                curry += 1 
            elif moved == 'a':
                currx += 1
            elif moved == 'd':
                currx -= 1

            
        elif swiat.get((currx, curry), 'empty') == '!':
            print("\nNatknąłeś się na przeciwnika! Walczysz!")
            time.sleep(1)
            print("\nRunda 1/3")
            time.sleep(1)
            if testhim(1) == True:
                print("Udało ci się uderzyć przeciwnika!")
                print("\nRunda 2/3")
                time.sleep(1)
                if testhim(0.75) == True:
                    print("Udało ci się uderzyć przeciwnika!")
                    print("\nRunda 3/3")
                    time.sleep(1)
                    if testhim(0.5) == True:
                        print("Udało ci się uderzyć przeciwnika! Pokonałeś go perfekcyjnie!")
                        zdarzenia.append(f"Tura {kroki}: Pokonanie przeciwnika perfekcyjnie!")
                        zabici += 1
                    else:
                        print("\nPokonałeś przeciwnika, ale zostałeś lekko zraniony! Straciłeś 20 zdrowia.")
                        zdrowie -= 20
                        zdarzenia.append(f"Tura {kroki}: Pokonanie przeciwnika, ale zranienie, -20 HP")
                        zabici += 1
                else:
                    print("Pokonałeś przeciwnika, ale zostałeś zraniony! Straciłeś 40 zdrowia.")
                    zdrowie -= 40
                    zdarzenia.append(f"Tura {kroki}: Pokonanie przeciwnika, ale zranienie, -40 HP")
                    zabici += 1
            else:
                print("Pokonałeś przeciwnika, ale zostałeś poważnie zraniony! Straciłeś 60 zdrowia.")
                zdarzenia.append(f"Tura {kroki}: Pokonanie przeciwnika, ale zranienie, -60 HP")
                zdrowie -= 60
            swiat[(currx, curry)] = '.'
            time.sleep(1.5)
        elif swiat.get((currx, curry), 'empty') == 'T':
            print("\nZnalazłeś skarb! Zdobywasz 1 skarb!")
            zdarzenia.append(f"Tura {kroki}: Znalezienie skarbu, +1 skarb")
            skarby += 1
            swiat[(currx, curry)] = '.'
            time.sleep(1.5)

        if skarby >= 5 or zdrowie <= 0:
            break

        if random.random() < 0.03 and czytrwa == False:
            zdarzenie = random.choice(['mgla', 'pogoda', 'regeneracja'])
            if zdarzenie == 'mgla':
                zasieg = 1
                iletrwa = 11
                czytrwa = True
                print(f"\nMgła! Widoczność ograniczona do {zasieg} pola na 10 tur.")
                zdarzenia.append(f"Tura {kroki}: Mgła, widoczność ograniczona na 10 tur")
            elif zdarzenie == 'pogoda':
                zasieg = 3
                czytrwa = True
                iletrwa = 16
                print(f"\nCzysta pogoda! Widoczność zwiększona do {zasieg} pól na 15 tur.")
                zdarzenia.append(f"Tura {kroki}: Czysta pogoda, widoczność zwiększona na 15 tur")
            
            elif zdarzenie == 'regeneracja':
                heal = random.randint(5, 45)
                if zdrowie < 150:
                    zdarzenia.append(f"Tura {kroki}: Długa podróż zahartowała cię, +{heal} HP")
                    print(f"\nDługa podróż zahartowała cię! +{heal} HP.")
                    zdrowie += heal
                else:
                    print(f"\nDługa podróż zahartowała cię, ale jesteś już na szczycie formy!")
                    zdarzenia.append(f"Tura {kroki}: Długa podróż zahartowała cię, ale jesteś już na szczycie formy!")
                    zdrowie = 150


        if czytrwa == True:
            iletrwa -= 1
            if iletrwa == 0:
                zasieg = 2
                czytrwa = False
                print("\nZdarzenie minęło, widoczność wróciła do normy.")
        
        if swiat.get((currx, curry), 'empty') == 'J':
            print("\nZnalazłeś jedzenie! Zaspokajasz głód!")
            głód += random.randint(25, 55)
            swiat[(currx, curry)] = '.'
            time.sleep(0.3)
            if głód > 100:
                głód = 100

        głód -= random.randint(2, 5)
        if głód <= 0:
            głód = 0
            print("\nZ głodu powoli umierasz! Znajdź coś do jedzenia. -5 HP.")
            zdrowie -= 5


    if skarby >= 5:
        os.system('cls')
        for i in range(5):
            print(". ", end='', flush=True)
            time.sleep(0.5)
        print(f"""=== WYPRAWA ZAKOŃCZONA ===

        Zebrałeś wszystkie 5 skarbów, {imie}!
        Twoja legenda przejdzie przez wieki.""")
        print("\nWyprawa zakończona sukcesem! Gratulacje!")

    elif zdrowie <= 0:
        os.system('cls')
        for i in range(5):
            print(". ", end='', flush=True)
            time.sleep(0.5)
        print(f"""=== WYPRAWA ZAKOŃCZONA ===

        Niestety, {imie}, twoja wyprawa zakończyła się tragicznie.
        Twoje imię zostanie zapamiętane jako przestroga dla przyszłych poszukiwaczy przygód.""")
        print("\nWyprawa zakończona porażką. Powodzenia następnym razem!")

    elif wpróżni == True:
        os.system('cls')
        for i in range(5):
            print(". ", end='', flush=True)
            time.sleep(0.5)
        print(f"""\n=== WYPRAWA ZAKOŃCZONA ===

        Niestety, {imie}, twoja wyprawa zakończyła się tragicznie. Próżnia cię pochłonęła.
        Twoje imię zaginie w otchłani, a twoja historia będzie zapomniana.""")
        print("\nWyprawa zakończona porażką. Powodzenia następnym razem!\n")


    print(f"""\n========== RAPORT KOŃCOWY ==========
          
    Nazwa wyprawy: {nazwa_wyprawy}
    Bohater: {imie}

    --- Parametry startowe ---
    Pozycja startowa: ({startx}, {starty})
    Początkowe HP: {starthp}

    --- Wyniki ---
    Końcowa pozycja: ({currx}, {curry})
    Liczba kroków: {kroki}
    Pozostałe HP: {zdrowie}
    Pozostały głód: {głód}
    Zebrane skarby: {skarby}/5
    Pokonani przeciwnicy: {zabici}

            ------ Zakończenie ------
    Przyczyna: {"Sukces - zebrano 5 skarbów" if skarby >= 5 else "Porażka - śmierć" if zdrowie <= 0 else "Zaginięcie w próżni"}
    Wynik: {skarby * 100 + zabici * 50 + kroki * 1.6}
            ------ Zdarzenia ------
    """)
    for z in zdarzenia:
        print(f"  {z}")
    print(f"""
    =====================================
    """)

    input("\nNaciśnij jakikolwiek klawisz, aby rozpocząć nową wyprawę...")