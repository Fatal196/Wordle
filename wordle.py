import random
import colorama # Für eine fabrliche print-Ausgabe notwendig: pip install colorama


# Abgabe Kurs: Einführung ins Programmieren mit Python
# Aufgabenstellung: Python Implementierung des Spiels Wordle

def worte_schreiben():
    """Liest eine existierende Wörterliste ein und extrahiert alle Wörter, welche genau 5 Buchstaben lang sind und schreibt diese
    in eine neue Datei namens Worte5.txt"""
    with open('Worte.txt', 'r') as datei_worte, open('Worte5.txt', 'w', encoding='utf-8') as datei_worte5:
        for zeile in datei_worte:
            #print(zeile.strip())
            zeile = zeile.strip().upper()
            if len(zeile) == 5:
                    datei_worte5.write(zeile + '\n')

def worte_einlesen():
    """Liest eine Wortliste ein. Die Liste setzt voraus, dass jedes Wort auf einer separaten Zeile stehen muss. 
    Die Funktion gibt die Worte der Liste als Tuple zurück."""
    with open('Worte5.txt', 'r', encoding='utf-8') as Worte5:
        return tuple(Worte5.readlines())

def wort_wordle(wortliste):
    """Die Funktion wählt ein zufälliges Wort aus der "wortliste" aus und gibt dieses zurück."""
    max_rand = len(wortliste)
    return wortliste[random.randint(0, max_rand - 1)]

def wordle_spielen(wordle_wort):
    """Funktion führt die Logik für das Spiel Wordle aus und gibt Antwort zurück"""
    index = 0

    while index <= 5:
        spieler_wort = str(input(f'{index + 1}. Versuch: ')).upper()
        index_update = spieler_pruefen(spieler_wort)

        # Prüfen, ob Spieler das Wort erraten hat
        if spieler_wort == wordle_wort[0:5]:
            print('Du hast das Wort erraten. Herzlichen Glückwunsch!')
            break

        if index_update == 1:
            # Wordle Wort prüfen und Rückmeldung an Spieler
            ergebnis = ergebnis_wordle(wordle_wort, spieler_wort)
            print(ergebnis)
        else:
            print('Wort erneut eingeben.')

        index = index + index_update

    if index > 5:
        print(f'Das Wort wurde nicht erraten. \nDie Lösung lautet: {wordle_wort}')

def spieler_pruefen(spieler_wort):
    """Überprüft das durch den Spieler eingegeben Wort auf Korrektheit: 
    1. Nur Buchstaben erlaubt
    2. Eingabe muss genau 5 Zeichen lang sein"""
    # Ist die Spieleriengabe nicht korrekt, wird dies die Funktion zurückgeben und den Spieler in der FUnktion 
    # wordle_spielen erneut um eine Eingabe bitten, ohne die letzte Eingabe zu werten. 

    index_incr = -1

    # Prüfen, ob die Länge des Wortes ok ist
    if len(spieler_wort) == 5:
        index_incr = 1
    else:
        print('Das Wort muss aus genau 5 Buchstaben bestehen')
        index_incr = 0

    # Prüfen, ob das Wort nur aus Buchstaben besteht
    for zeichen in spieler_wort:
        if not zeichen.isalpha():
            print('Es sind nur Buchstaben erlaubt!')
            index_incr = 0
            break

    return index_incr

def ergebnis_wordle(wordle, spieler):
    liste_gruen = [] # beinhaltet die Indizes der korrekten Buchstaben an der korrekten Position
    liste_gelb = [] # beinhaltet die Indizes der Buchstaben, welche vorhanden sind, aber nicht an der korrekten Position
    
    # Wenn zwei Mal derselbe Buchstabe geraten wird, dieser aber nur einmal vorkommt, werden trotzdem beide als "gefunden"
    # markiert. Keine Ahnung wie die Logik im Originalspiel ist, hier ist es absichtlich so umgesetzt, da
    # dies der Logik nicht widerspricht.  

    # Füllt die liste_gruen ein. Sollte der Buchstabe nicht an der korrekten Stelle stehen, wird eine
    # -1 eingetragen. Die Liste MUSS aus 5 Elementen bestehen
    for i in range(5):
        if spieler[i] == wordle[i]:
            liste_gruen.append(i)
        else:
            liste_gruen.append(-1)

    # Füllt die liste_gelb ein, sofern einer durch den Spieler eingegebenen Buchstabe im wordle_wort vorkommt,
    # ansonsten wird -1 eingetragen. Die Liste MUSS aus 5 Elementen bestehen. 

    # Zur besseren Übersicht ist diese Schleife von der oberen Schleife getrennt. 
    for i in range(5):
        liste_gelb.append(wordle.find(spieler[i]))

    # Ausgabe für Spieler erstellen inklusive korrekter Farbcodierung
    ausgabe = ''

    for i in range(5):
        if i == liste_gruen[i]:
            ausgabe += colorama.Fore.GREEN + spieler[i] + colorama.Fore.RESET
            # print(ausgabe) # print Befehl zu Testzwecken notwendig
        elif liste_gelb[i] >= 0:
            ausgabe += colorama.Fore.YELLOW + spieler[i] + colorama.Fore.RESET
            # print(ausgabe) # print Befehl zu Testzwecken notwendig
        else:
            ausgabe += colorama.Fore.LIGHTBLACK_EX + spieler[i] + colorama.Fore.RESET
            # print(ausgabe) # print Befehl zu Testzwecken notwendig

    return ausgabe


# Hauptprogramm
worte_schreiben()
wordle_wort = wort_wordle(worte_einlesen())
# print(wordle_wort) # Zu Testzwecken notwenidg gewesen
wordle_spielen(wordle_wort)