from Zahlensysteme_ändern import hexZuBits, binzuHex
from DES_Permutationen import  Expansion, Eingangspermutation, Ausgangspermutation
from Rundenschluesselerstellen import  Rundenschluesselarray
from sbox_auslesen import  sboxen_auslesen

def Ausgabe(string1,string2):
    vor_permutation = string2+string1
    nach_permutation = ""
    for x in range(len(Ausgangspermutation)):
        nach_permutation += vor_permutation[Ausgangspermutation[x]]

    return binzuHex(nach_permutation)
def Eingabe_permutieren(string):
    nach_perm = ""
    for x in range(len(Eingangspermutation)):
        nach_perm += string[Eingangspermutation[x]]

    return nach_perm
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

Linkehaelfte = []
Rechtehaelfte = []

def Aufteilen(string,Array,Array1):
    Array.append(string[:32])
    Array1.append(string[32:])

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
    Linkehaelfte.clear()
    Rechtehaelfte.clear()
    return ergebnis
