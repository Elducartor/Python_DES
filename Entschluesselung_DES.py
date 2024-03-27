def Entschlüsselung(Eingabe):
    if len(Eingabe) == 16:
        Eingabex = hexZuBits(Eingabe)
    if len(Eingabe) == 64:
        Eingabex = Eingabe
    # braucht seine eignen Rechehälfte und Linkehälfte Array
    Aufteilen(Eingabe_permutieren(Eingabex), Linkehaelfte_entschlüsselung, Rechtehaelfte_entschlüsselung)
    for Runde in range(16):
        aktuelles_R = expandieren(Rechtehaelfte_entschlüsselung[Runde])
        sboxen_auslesen(xor_verrechnen(aktuelles_R, Rundenschluesselarray[16-Runde]), Runde, Linkehaelfte_entschlüsselung, Rechtehaelfte_entschlüsselung)
    ergebnis = Ausgabe(Linkehaelfte_entschlüsselung[-1], Rechtehaelfte_entschlüsselung[-1])
    Ausgabe_labe2 = tk.Label(root, text=f"das Ergebnis ist in Hexadezimal:{ergebnis}")
    Ausgabe_labe2.place(x=100, y=600)
    print(Rechtehaelfte_entschlüsselung)
