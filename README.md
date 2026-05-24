# Explorer

Symulator wyprawy po dwuwymiarowym świecie. Wcielasz się w bohatera eksplorującego losowo generowaną mapę 200×200 pól. Twoim celem jest zebranie 5 skarbów zanim skończy ci się zdrowie lub głód.

## Wymagania

- Python 3.11
- System operacyjny: **Windows** (program korzysta z modułu `msvcrt` ze standardowej biblioteki Pythona, dostępnego wyłącznie na Windows)
- Żadnych dodatkowych bibliotek — tylko standardowa biblioteka Pythona

## Uruchomienie

```
python main.py
```

## Jak grać

Na początku program poprosi o podanie:
- imienia bohatera
- nazwy wyprawy
- liczby punktów zdrowia (50–150)
- pozycji startowej (x, y) w zakresie od -100 do 100

Ruch odbywa się klawiszami `w` `a` `s` `d`. Po każdym kroku terminal pokazuje mapę okolicy, stan zasobów i ostatnie zdarzenia.

## Elementy świata

| Symbol | Znaczenie |
|--------|-----------|
| `@` | gracz |
| `.` | puste pole |
| `X` | przeszkoda (-10 HP przy wejściu) |
| `!` | przeciwnik (walka na czas) |
| `J` | jedzenie (+25–55 głodu) |
| `T` | skarb (+1 skarb) |
| `V` | próżnia — poza granicami świata |

Mapa jest generowana losowo przy każdej wyprawie. Elementy świata grupują się w klastry — obszary gęste w obiekty mają więcej jedzenia i skarbów, otwarte pustkowia są niebezpieczne.

## Zasoby

- **Zdrowie** — zaczyna od wartości wybranej przez gracza (50–150). Spada przy uderzeniu w przeszkody, walce i głodzie. Śmierć przy 0.
- **Głód** — zaczyna od 100, spada o 2–5 punktów per tura. Przy 0 gracz traci 5 HP co turę. Uzupełniany przez jedzenie (`J`).

## Walka

Spotkanie z przeciwnikiem (`!`) uruchamia minigrę reakcji — 3 rundy, za każdym razem należy nacisnąć klawisz jak najszybciej po sygnale "TERAZ!". Kliknięcie przed sygnałem cofa rundę. Im lepsza reakcja, tym mniej obrażeń:

| Wynik rundy | Obrażenia |
|-------------|-----------|
| Wszystkie 3 rundy w czasie | 0 HP |
| Runda 3 za wolno | -20 HP |
| Runda 2 za wolno | -40 HP |
| Runda 1 za wolno | -60 HP |

## Próżnia

Wyjście poza granice świata (-100 do 100) uruchamia minigrę reakcji. Przy zdaniu testu gracz wraca na mapę bez obrażeń. Przy niezdaniu traci 80 HP i wraca.

## Zdarzenia losowe

Co turę jest 3% szansa na wystąpienie jednego z trzech zdarzeń (tylko jeśli żadne inne nie jest aktywne):

| Zdarzenie | Efekt | Czas trwania |
|-----------|-------|--------------|
| **Mgła** | Widoczność zmniejszona z 2 do 1 pola | 10 tur |
| **Czysta pogoda** | Widoczność zwiększona z 2 do 3 pól | 15 tur |
| **Zahartowanie** | Losowy heal +5 do +45 HP (max 150) | jednorazowe |

## Warunki zakończenia

- **Sukces** — zebranie 5 skarbów
- **Porażka** — śmierć (zdrowie ≤ 0), w tym przez głód lub próżnię

Po zakończeniu wyświetlany jest raport z przebiegu wyprawy wraz z listą wszystkich zdarzeń i wynikiem punktowym. Program pozwala uruchomić nową wyprawę bez ponownego uruchamiania.

## Wynik końcowy

```
skarby × 100 + pokonani przeciwnicy × 50 + kroki × 0.2
```

## Wskazówki

- Trzymaj się obszarów z większą ilością obiektów — tam częściej pojawia się jedzenie
- Otwarte pustkowia są niebezpieczne przy niskim głodzie
- Przy 150 HP startowego masz około 30 tur buforu bez jedzenia
- Przeciwnicy mają szanse poruszyć się co turę — mogą blokować przejście lub się odsunąć
