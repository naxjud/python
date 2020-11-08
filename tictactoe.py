print('TIC-TAC-TOE')

zeichen = {
    0:"0",
    1:"x"
}

spieler = {
    0:"",
    1:""
}


"""
spiel_feld ={
    "00": "x|_|_|",
    "01": "_|_|_|",
    "02": "_|_|_|"
}
"""
feld = "_|"
gespielt = {
}

gewinner_felder = {
    123,
    456,
    789,
    159,
    357,
    369,
    147
}

def clear_gespielt(gespielt):
    zaehler=0
    for i in range(3):
        for j in range(3):
            zaehler += 1
            gespielt[zaehler] = ""


def zeichne_feld(gespielt):
    zaehler = 0
    for i in range(3):
        reihe = ""
        for j in range(3):
            zaehler += 1
            if gespielt[zaehler] == "":
                reihe += feld
            else:
                reihe += gespielt[zaehler]
        print(reihe)

def nochplatz(gespielt):
    for sf in gespielt:
        if gespielt[sf] == "":
            return True

    return False


# solange das spiel nicht beendet wird
while True:
    clear_gespielt(gespielt)
    # zeichne_feld(gespielt)
    # Namen der Spieler fragen
    spieler[1] = input("Spieler 1: ")
    spieler[0] = input("Spieler 2: ")
    print(f"Salam {spieler[1]} und {spieler[0]}")

    zaehler = 1

    # solange es leere felder gibt oder das spiel nicht gewonnen wurde
    while nochplatz(gespielt):
        # Zeichne das aktuelle Spielfeld
        zeichne_feld(gespielt)
        eingabe_falsch = True

        while eingabe_falsch:
            # spieler_1_zug nehmen
            zug = int(input(f"Dein Zug {spieler[zaehler%2]}: "))
            if gespielt[zug] != "":
                print("dieses Feld wurde schon gespielt")
                zug = int(input(f"Dein Zug:{spieler[zaehler%2]}: "))
            else:
                gespielt[zug] = zeichen[zaehler%2] +"|"
                zaehler += 1
                eingabe_falsch = False

    zeichne_feld(gespielt)
    spiel_neustarten = input("wieder spielen? (j)a (n)ein: ")
    if spiel_neustarten == 'n':
        break

print("Spiel beendet. Bis zum nächsten mal")
