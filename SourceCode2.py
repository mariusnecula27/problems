import datetime

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
        if cnp[0] == "0":
            return "CNP invalid"

        # AA LL ZZ - verificare
        if cnp[0] == "1" or cnp[0] == "2" or cnp[0] == "7" or cnp[0] == "8" or cnp[0] == "9":
            year = "19" + cnp[1:3]
        elif cnp[0] == "3" or cnp[0] == "4":
            year = "18" + cnp[1:3]
        elif cnp[0] == "5" or cnp[0] == "6":
            year = "20" + cnp[1:3]

        try:
            data_nasterii = datetime.date(int(year), int(cnp[3:5]), int(cnp[5:7]))
        except ValueError:
            return "CNP invalid"

        # JJ - cod judet
        if (int(cnp[7:9]) > 0 and int(cnp[7:9]) < 47) or (int(cnp[7:9]) > 50 and int(cnp[7:9]) < 53):
            pass
        else:
            return "CNP invalid"

        # NNN
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
print(checkCNP("5120229420016"))