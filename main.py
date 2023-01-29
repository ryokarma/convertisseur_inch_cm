error = False

# des cm vers pouces
def cm_inch():
    valeur = float(input("Quelle est la valeur que vous souhaitez convertir ?"))
    valeur_convertie = 0.394 * valeur
    print(f"{valeur} centimètres équivalent à {valeur_convertie} pouces.")


# des pouces vers cm
def inch_cm():
    valeur = float(input("Quelle est la valeur que vous souhaitez convertir ?"))
    valeur_convertie = 2.54 * valeur
    print(f"{valeur} pouces équivalent à {valeur_convertie} centimètres.")


while not error:
    choice_conv = input(
        "Tapez A pour convertir des pouces vers les centimètres.\nTapez B pour convertir des centimètres vers les "
        "pouces.\nTapez C pour mettre fin au programme.\nComment souhaitez vous convertir votre valeur ? ")
    if choice_conv == "A":
        inch_cm()
    elif choice_conv == "B":
        cm_inch()
    elif choice_conv == "C":
        error = True
        print("Au revoir !")
    else:
        print("Merci de taper A ou B uniquement.")
