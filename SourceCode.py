fraza = "Lorem Ipsum este pur şi simplu o macheta pentru text a industriei tipografice."
lista_de_inlocuit = [[17, 30, 'cu siguranta'], [34, 40, 'emblema'], [67, 77, 'informatice']]
# am observat ca indicele 63 este gresit; 67 este corect pentru ca textul de la iesire sa fie egal cu "output"
# output: Lorem Ipsum este cu siguranta o emblema pentru text a industriei informatice.

def replace_words(fraza, lista_de_inlocuit):
    output = ""
    if len(lista_de_inlocuit) > 0:
        for index in range(0, len(lista_de_inlocuit)):
            if lista_de_inlocuit[index][0] < len(fraza) and lista_de_inlocuit[index][1] < len(fraza):
                if index == 0:
                    output = fraza[0 : lista_de_inlocuit[index][0]] + lista_de_inlocuit[index][2]
                elif index == len(lista_de_inlocuit) - 1:
                    output += fraza[lista_de_inlocuit[index-1][1] : lista_de_inlocuit[index][0] - 1] + lista_de_inlocuit[index][2] + fraza[lista_de_inlocuit[index][1]:]
                else:
                    output += fraza[lista_de_inlocuit[index-1][1] : lista_de_inlocuit[index][0] - 1] + lista_de_inlocuit[index][2]
    return output

print(replace_words(fraza, lista_de_inlocuit))

def checkCNP(cnp):

    if len(cnp) == 13:

        # intregul sir de caractere trebuie sa fie format din cifre
        if cnp.isdigit() is False:
            return "CNP invalid"

        # S - sexul si secolul
        if int(cnp[0]) > 0 and int(cnp[0]) < 10:
            pass
        else:
            return "CNP invalid"

        # AA - anul nasterii
        # cod redundant - este acoperit de primul IF
        if int(cnp[1:3]) >= 0 and int(cnp[1:3]) <= 99:
            pass
        else:
            return "CNP invalid"

        #LL - luna nasterii
        if not (int(cnp[3:5]) > 0 and int(cnp[3:5]) < 13):
            return "CNP invvalid"

        # ZZ - ziua nasterii
        luni_31_zile = ["01", "03", "05", "07" , "08", "10", "12"]
        luni_30_zile = ["04", "06", "09", "11"]

        if cnp[0] == "1" or cnp[0] == "2" or cnp[0] == "7" or cnp[0] == "8" or cnp[0] == "9":
            year = "19" + cnp[1:3]
        elif cnp[0] == "3" or cnp[0] == "4":
            year = "18" + cnp[1:3]
        elif cnp[0] == "5" or cnp[0] == "6":
            year = "20" + cnp[1:3]

        #verificam daca anul este biesct sau nu, pentru ZZ februarie
        leap_year = False #valoarea False este pentru an obisnuit, True pentru an bisect
        if (int(year) % 4) == 0:
            if (int(year) % 100) == 0:
                if (int(year) % 400) == 0:
                    leap_year = True
                else:
                    leap_year = False
            else:
                leap_year = True
        else:
            leap_year = False

        if int(cnp[5:7]) > 0 and int(cnp[5:7]) < 32 and cnp[3:5] in luni_31_zile:
            pass
        elif int(cnp[5:7]) > 0 and int(cnp[5:7]) < 31 and cnp[3:5] in luni_30_zile:
            pass
        elif leap_year is False and int(cnp[5:7]) > 0 and int(cnp[5:7]) < 29 and int(cnp[3:5]) == 2:
            pass
        elif leap_year is True and int(cnp[5:7]) > 0 and int(cnp[5:7]) < 30 and int(cnp[3:5]) == 2:
            pass
        else:
            return "CNP invalid"

        # JJ - cod judet
        if (int(cnp[7:9]) > 0 and int(cnp[7:9]) < 47) or (int(cnp[7:9]) > 50 and int(cnp[7:9]) < 53):
            pass
        else:
            return "CNP invalid"

        # NNN - redundant
        if int(cnp[9:12]) > 0 and int(cnp[9:12]) < 1000:
            pass
        else:
            return "CNP invalid"

        # C - control
        nr_control = "279146358279"
        sum = 0
        for index in range(0, len(cnp) - 1):
            sum += int(cnp[index]) * int(nr_control[index])

        if sum%11 == 10 and cnp[-1] == "1":
            pass
        elif sum%11 == int(cnp[-1]):
            pass
        else:
            return "CNP invalid"

        return "CNP VALID"

    else:
        print("CNP invalid!")

print(checkCNP("3000228300018"))