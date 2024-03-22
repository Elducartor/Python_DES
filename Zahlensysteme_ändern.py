def dezimal_in_bits(string):
        Binaer = {
            "00": "0000",
            "01": "0001",
            "02": "0010",
            "03": "0011",
            "04": "0100",
            "05": "0101",
            "06": "0110",
            "07": "0111",
            "08": "1000",
            "09": "1001",
            "10": "1010",
            "11": "1011",
            "12": "1100",
            "13": "1101",
            "14": "1110",
            "15": "1111"}
        ausgabe_bits = ""
        for xx in range(0, len(string), 2):
            ausgabe_bits += (Binaer[string[xx]+string[xx+1]])
        return ausgabe_bits


def binzuHex(string):
    hexa_string = ""
    hexdazi = {
        "0000" : "0",
        "0001" : "1",
        "0010" : "2",
        "0011" : "3",
        "0100" : "4",
        "0101" : "5",
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "A",
        "1011" : "B",
        "1100" : "C",
        "1101" : "D",
        "1110" : "E",
        "1111" : "F"
    }

    for x in range(0,len(string),4):
        hexa_string += hexdazi[string[x:x+4]]

    return hexa_string

def hexZuBits(string):
    Binaer = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"}
    ausgabe_bits = ""
    for x in range(len(string)):
        ausgabe_bits += Binaer[string[x]]
    return ausgabe_bits
