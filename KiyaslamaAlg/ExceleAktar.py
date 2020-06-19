from  openpyxl import *

def Excel(question,alg1,alg2,alg3):
    kitap = load_workbook("dosya.xlsx")
    sheet = kitap.active

    liste = []

    liste.append(question)

    if alg1 != []:
        liste.append(alg1[0][0])
        liste.append(alg1[0][1])

        liste.append(alg1[1][0])
        liste.append(alg1[1][1])

    if alg2 != []:
        liste.append(alg2[0][0])
        liste.append(alg2[0][1])

        liste.append(alg2[1][0])
        liste.append(alg2[1][1])

    if alg3 != []:
        liste.append(alg3[0][0])
        liste.append(alg3[0][1])

        liste.append(alg3[1][0])
        liste.append(alg3[1][1])


    sheet.append(liste)

    kitap.save("dosya.xlsx")
    kitap.close()