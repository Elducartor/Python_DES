import tkinter as tk
from DES_Sboxen import sbox1,sbox2,sbox3,sbox4,sbox5,sbox6,sbox7,sbox8
from DES_Permutationen import Expansion,Eingangspermutation,P_permutation,Ausgangspermutation,PC_1,PC_2
from Zahlensysteme_ändern import dezimal_in_bits,binzuHex,hexZuBits
root = tk.Tk()
root.geometry("1200x800")
root.title("DES Verschlüsselung")
"""DES verschlüsselung, kein Betriebsmodi bisher. Nur verschlüsselung."""
def clear_error_message():
    fehlerhafteeingabe.config(text="")
def Key_Eingabe():
    key = Schlüsseleingabe_wert.get()
    if len(key) == 16:
        key = hexZuBits(key)
        Rundenschluesselerstellen(key)
        button_für_Einagbe2.config(state="normal")
        button_für_Schlüsselfahrplan.config(state="normal")
    elif len(key) == 64:
        Rundenschluesselerstellen(key)
        button_für_Einagbe2.config(state="normal")
        button_für_Schlüsselfahrplan.config(state="normal")
    elif len(key) != 16 and len(key) != 64:
        fehlerhafteeingabe.config(text=f"Fehler: falsche Anzahl an Bits. Entweder 16 Hexadezimalzahlen oder 64 Bits eingeben \n sie haben {len(key)} stellen eingeben")
        root.after(2000,clear_error_message)
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


def Eingangsbits_Eingabe():
    Eingabe = Eingangs_daten_wert.get()
    if len(Eingabe) == 16 or len(Eingabe) == 64:
        Entschlüsselung(Eingabe)
        Verschlüsselung(Eingabe)
    if len(Eingabe) != 16 and len(Eingabe) != 64:
        fehlerhafteeingabe.config(text=f"Fehler: falsche Anzahl an Bits. Entweder 16 Hexadezimalzahlen oder 64 Bitseingeben \n sie haben {len(Eingabe)} stellen eingeben")
        root.after(2000,clear_error_message)

Rundenschluesselarray = []
def Eingabe_permutieren(string):
    nach_perm = ""
    for x in range(len(Eingangspermutation)):
        nach_perm += string[Eingangspermutation[x]]

    return nach_perm

Linkehaelfte = []
Rechtehaelfte = []
Rechtehaelfte_entschlüsselung = []
Linkehaelfte_entschlüsselung = []
def Aufteilen(string,Array,Array1):
    Array.append(string[:32])
    Array1.append(string[32:])
zweistellenschiebe_runde = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
einstellenschiebe_runde = [0, 1, 8, 15]

def Rundenschluesselerstellen(Schluessel):
    C_abschnitt = []
    D_abschnitt = []
    Schluessel_nach_PC_1 = ""
    for x in range(len(PC_1)):
        Schluessel_nach_PC_1 += Schluessel[PC_1[x]]
        # Schlüssel aufteilen und in C und D abschnitt einfügen.
    C = Schluessel_nach_PC_1[0:28]
    D = Schluessel_nach_PC_1[28:]
    C_abschnitt.append(C)
    D_abschnitt.append(D)
    #alle Rundenschlüssel erstelln
    for x in range(17):
        if x in zweistellenschiebe_runde:
                c_rotieren = C_abschnitt[x][2:] + C_abschnitt[x][:2]
                d_rotieren = D_abschnitt[x][2:] + D_abschnitt[x][:2]
                C_abschnitt.append(c_rotieren)
                D_abschnitt.append(d_rotieren)

        if x in einstellenschiebe_runde:
                c_rotieren = C_abschnitt[x][1:] + C_abschnitt[x][:1]
                d_rotieren = D_abschnitt[x][1:] + D_abschnitt[x][:1]
                C_abschnitt.append(c_rotieren)
                D_abschnitt.append(d_rotieren)

        # +1 ,weil ich bei Runde 0 den ersten Index in C_abschnitt und D_abschnitt anspreche möchte
        Rundenschluessel_vor_perm = str(C_abschnitt[x]) + str(D_abschnitt[x])
        Rundenschluessel = ""
        for index in range(len(PC_2)):
            Rundenschluessel += Rundenschluessel_vor_perm[PC_2[index]]

        Rundenschluesselarray.append(Rundenschluessel)
def expandieren(string):
    R_nach_expand = ""
    for x in range(len(Expansion)):
        R_nach_expand += string[Expansion[x]]
    return R_nach_expand
def xor_verrechnen(string1,string2):
    if len(string1) != len(string2):
        return "fehler!"
    Rx_xor_Key = ""
    for x in range(len(string1)):
        bit = int(string1[x]) ^ int(string2[x])
        Rx_xor_Key += str(bit)

    return Rx_xor_Key

def sboxen_auslesen(string,Runde,Array,Array1):
    if len(string) != 48:
        return "Fehler!"
    auslese_array = []
    sbox_ausgabe = ""
    new_R = ""
    new_L = ""
    for x in range(0,len(string),6):
        auslese_array.append(string[x:x+6])
    for y in range(len(auslese_array)):
        #sbox-reihe gibt an welches innere Array angesprochen werden soll
        #sbox_index gibt  an welcher index von 0-15 angesprochen werden soll
        sbox_reihe = int(auslese_array[y][0])*2 + int(auslese_array[y][5])
        sbox_index = int(auslese_array[y][1])*8 + int(auslese_array[y][2])*4 + int(auslese_array[y][3])*2 + int(auslese_array[y][4])
        if y == 0:
            wert = sbox1[sbox_reihe][sbox_index]
        if y == 1:
            wert = sbox2[sbox_reihe][sbox_index]
        if y == 2:
            wert = sbox3[sbox_reihe][sbox_index]
        if y == 3:
            wert = sbox4[sbox_reihe][sbox_index]
        if y == 4:
            wert = sbox5[sbox_reihe][sbox_index]
        if y == 5:
            wert = sbox6[sbox_reihe][sbox_index]
        if y == 6:
            wert = sbox7[sbox_reihe][sbox_index]
        if y == 7:
            wert = sbox8[sbox_reihe][sbox_index]
        sbox_ausgabe += wert
    sbox_ausgabe_bits = dezimal_in_bits(sbox_ausgabe)
    for z in range(len(P_permutation)):
        new_R += sbox_ausgabe_bits[P_permutation[z]]
    old_L = Array[Runde]
    # new_L means the left side after xor with f(R)
    for bits in range(len(old_L)):
        bit = int(old_L[bits]) ^ int(new_R[bits])
        new_L += str(bit)

    Array.append(Array1[-1])
    Array1.append(new_L)


def Ausgabe(string1,string2):
    vor_permutation = string2+string1
    nach_permutation = ""
    for x in range(len(Ausgangspermutation)):
        nach_permutation += vor_permutation[Ausgangspermutation[x]]

    return binzuHex(nach_permutation)

Schlüsseleingabe_wert = tk.StringVar()
Schlüsseleingabe = tk.Entry(root,textvariable=Schlüsseleingabe_wert,width=50)
Schlüsseleingabe.insert(0,"Bitte 64 Schlüsselbits (8Hexadezimalzahlen) eingeben.")
Schlüsseleingabe.place(x=10,y=100)

Eingangs_daten_wert = tk.StringVar()
Eingangs_daten = tk.Entry(root,textvariable=Eingangs_daten_wert,width=50)
Eingangs_daten.insert(0,"Bitte 64 Eingansbits (8Hexadezimalzahlen) eingeben.")
Eingangs_daten.place(x=10,y=140)
button_für_Einagbe = tk.Button(root,text="Schlüsseleingabe bestätigen.", command=Key_Eingabe)
button_für_Einagbe.place(x=430,y=100)
button_für_Einagbe2 = tk.Button(root,text="Datenbit Eingabe bestätigen.", command=Eingangsbits_Eingabe,state="disabled")
button_für_Einagbe2.place(x=430,y=140)
fehlerhafteeingabe = tk.Label(root,fg="red")
fehlerhafteeingabe.place(x=430,y=400)

def zum_Schlüsselfahplan_switchen():
    root.withdraw()
    open_Schlüsselfahrplan()
def open_Schlüsselfahrplan():
    global Schlüsselfahrplan
    Schlüsselfahrplan = tk.Toplevel()
    Schlüsselfahrplan.title("Hier werden die Schlüssel 1 bis 16 aufgelistet.")
    Schlüsselfahrplan.geometry("1200x800")
    Rundenschluesselarray2 = []
    for x in range(1,len(Rundenschluesselarray)):
        Rundenschluesselarray2.append("key nummer" + str(x) + "\n" + Rundenschluesselarray[x])
    Rundenschlüssel = "\n".join(Rundenschluesselarray2)
    Rundenschlüssel_label = tk.Label(Schlüsselfahrplan,text=Rundenschlüssel)
    Rundenschlüssel_label.pack()
    button_zurück_zum_Hauptbildschirm = tk.Button(Schlüsselfahrplan, text="Zurück zum Hauptbildschirm", command=zurück_zum_Hauptbildschirm)
    button_zurück_zum_Hauptbildschirm.place(x=10,y=10)



def zurück_zum_Hauptbildschirm():
    Schlüsselfahrplan.withdraw()
    root.deiconify()
button_für_Schlüsselfahrplan = tk.Button(root,text="Schlüsselfahrplan anschauen",command=zum_Schlüsselfahplan_switchen,state="disabled")
button_für_Schlüsselfahrplan.place(x=670,y=100)


root.mainloop()
