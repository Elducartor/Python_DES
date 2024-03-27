import tkinter as tk
from tkinter import filedialog

from Zahlensysteme_ändern import hexZuBits
import Rundenschluesselerstellen
import Entschluesselung_DES
import Verschluesselung_DES
root = tk.Tk()
root.geometry("1200x800")
root.title("DES Ent und -Verschlüsselung")


def clear_error_message():
    fehlerhafteeingabe.config(text="")


def Key_Eingabe():
    key = Schlüsseleingabe_wert.get()
    if len(key) == 16:
        key = hexZuBits(key)
        Rundenschluesselerstellen.Rundenschluesselerstellen(key)
        button_für_Einagbe2.config(state="normal")
        button_für_Schlüsselfahrplan.config(state="normal")
        button_für_datei.config(state="normal")
    elif len(key) == 64:
        Rundenschluesselerstellen.Rundenschluesselerstellen(key)
        button_für_Einagbe2.config(state="normal")
        button_für_Schlüsselfahrplan.config(state="normal")
        button_für_datei.config(state="normal")
    elif len(key) != 16 and len(key) != 64:
        fehlerhafteeingabe.config(text="Fehler: falsche Anzahl an Bits. Entweder 16 Hexadezimalzahlen oder" +
                                        f"64 Bits eingeben \n sie haben {len(key)} stellen eingeben")
        root.after(2000,clear_error_message)

def Eingangsbits_Eingabe():
    Eingabe = Eingangs_daten_wert.get()
    if len(Eingabe) == 16 or len(Eingabe) == 64:
        Entschluesselung_button = tk.Button(root, text="Entschlüsselung von 64 Bit", command=lambda: Entschluesselungs_funktion(Eingabe))
        Entschluesselung_button.place(x=100, y=300)
        Verschluesselungs_button = tk.Button(root, text="Verschlüsselung von 64 Bit", command=lambda: Verschluesselungs_funktion(Eingabe))
        Verschluesselungs_button.place(x=600, y=300)
    if len(Eingabe) != 16 and len(Eingabe) != 64:
        fehlerhafteeingabe.config(text=f"Fehler: falsche Anzahl an Bits. Entweder 16 Hexadezimalzahlen oder 64 Bitseingeben \n sie haben {len(Eingabe)} stellen eingeben")
        root.after(2000,clear_error_message)
def Entschluesselungs_funktion(Eingabe):
    Entschluesselung_DES.Entschlüsselung(Eingabe)
    Ausgabe_labe2 = tk.Label(root,
    text=f"das Ergebnis der Entschluesselung ist in  Hexadezimal:{Entschluesselung_DES.Entschlüsselung(Eingabe)}")
    Ausgabe_labe2.place(x=50, y=400)

def Verschluesselungs_funktion(Eingabe):
    Verschluesselung_DES.Verschlüsselung(Eingabe)
    Ausgabe_labe = tk.Label(root,
    text=f"das Ergebnis der Verschluesselung ist in Hexadezimal:{Verschluesselung_DES.Verschlüsselung(Eingabe)}")
    Ausgabe_labe.place(x=600, y=400)

Schlüsseleingabe_wert = tk.StringVar()
Schlüsseleingabe = tk.Entry(root,textvariable=Schlüsseleingabe_wert,width=50)
Schlüsseleingabe.insert(0,"Bitte 64 Schlüsselbits (8Hexadezimalzahlen) eingeben.")
Schlüsseleingabe.place(x=10, y=100)

Eingangs_daten_wert = tk.StringVar()
Eingangs_daten = tk.Entry(root, textvariable=Eingangs_daten_wert,width=50)
Eingangs_daten.insert(0, "Bitte 64 Eingansbits (8Hexadezimalzahlen) eingeben.")
Eingangs_daten.place(x=10, y=140)
button_für_Einagbe = tk.Button(root,text="Schlüsseleingabe bestätigen.", command=Key_Eingabe)
button_für_Einagbe.place(x=430, y=100)
button_für_Einagbe2 = tk.Button(root, text="Datenbit Eingabe bestätigen.", command=Eingangsbits_Eingabe, state="disabled")
button_für_Einagbe2.place(x=430, y=140)
fehlerhafteeingabe = tk.Label(root, fg="red")
fehlerhafteeingabe.place(x=430, y=400)

def zum_Schlüsselfahplan_switchen():
    root.withdraw()
    open_Schlüsselfahrplan()
def open_Schlüsselfahrplan():
    global Schlüsselfahrplan
    Schlüsselfahrplan = tk.Toplevel()
    Schlüsselfahrplan.title("Hier werden die Schlüssel 1 bis 16 aufgelistet.")
    Schlüsselfahrplan.geometry("1200x800")
    Rundenschluesselarray2 = []
    for x in range(1,len(Rundenschluesselerstellen.Rundenschluesselarray)):
        Rundenschluesselarray2.append("key nummer" + str(x) + "\n" + Rundenschluesselerstellen.Rundenschluesselarray[x])
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

def Datei_verschlüsselung():
    dateiname = filedialog.askopenfilename()
    verschlüsselter_bitstring = ""
    if dateiname:
        with open(dateiname, "rb") as datei:
            datei_inhalt = datei.read()
            bit_string = ''.join(format(byte, '08b') for byte in datei_inhalt)
            padding_bits = 64 - (len(bit_string) % 64) # Paddingbits anwenden.
            if len(datei_inhalt) % 64 != 0:
                bit_string += "0" * padding_bits
    Block_groeße = 64
    for index in range(0,len(bit_string),Block_groeße):
        block = bit_string[index:index+Block_groeße]
        verschlüsselter_bitstring += Verschluesselung_DES.Verschlüsselung(block)

    with open("verschlüsselung im format","wb") as datei2:
        datei2.write(verschlüsselter_bitstring.encode("utf-8"))
button_für_datei = tk.Button(root,text="Datei verschlüsseln", command=Datei_verschlüsselung, state="disabled")
button_für_datei.place(x=100,y=200)
root.mainloop()