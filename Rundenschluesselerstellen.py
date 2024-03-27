
from DES_Permutationen import PC_1, PC_2
zweistellenschiebe_runde = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
einstellenschiebe_runde = [0, 1, 8, 15]
Rundenschluesselarray = []

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
