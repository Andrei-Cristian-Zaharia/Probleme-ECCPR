from sys import stdin

judete = ["AB", "AR", "AG", "B", "BC", "BH", "BN", "BT", "BV", "BR", "BZ", "CS",
          "CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL",
          "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV",
          "TR", "TM", "TL", "VS", "VL", "VN"]

def verifica_nr(nr_inmatriculare) -> bool:
    if judete.__contains__(nr_inmatriculare[0]) == False:
        return False

    if len(nr_inmatriculare[1]) < 2 or len(nr_inmatriculare[1]) > 3 or not nr_inmatriculare[1].isnumeric():
        return False

    if len(nr_inmatriculare[2]) != 3 or not nr_inmatriculare[2].isalpha():
        return False

    print(nr_inmatriculare[0], nr_inmatriculare[1], nr_inmatriculare[2])
    return True

for line in stdin:
    verifica_nr(nr_inmatriculare=list(map(str, line.split())))
