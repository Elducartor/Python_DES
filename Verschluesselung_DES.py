def Verschlüsselung(Eingabe):
    if len(Eingabe) == 16:
        Eingabex = hexZuBits(Eingabe)
    if len(Eingabe) == 64:
        Eingabex = Eingabe
    #Eingabex = hexZuBits(Eingabe)
    Aufteilen(Eingabe_permutieren(Eingabex), Linkehaelfte, Rechtehaelfte)
    for Runde in range(16):
        aktuelles_R = expandieren(Rechtehaelfte[Runde])
        sboxen_auslesen(xor_verrechnen(aktuelles_R, Rundenschluesselarray[Runde + 1]), Runde, Linkehaelfte, Rechtehaelfte)
    ergebnis = Ausgabe(Linkehaelfte[-1], Rechtehaelfte[-1])
    Ausgabe_labe = tk.Label(root, text=f"das Ergebnis ist in Hexadezimal:{ergebnis}")
    Ausgabe_labe.place(x=100, y=400)
