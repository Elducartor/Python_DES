from DES_Sboxen import sbox1, sbox2, sbox3, sbox4, sbox5, sbox6, sbox7, sbox8
from Zahlensysteme_ändern import dezimal_in_bits
from DES_Permutationen import P_permutation
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


