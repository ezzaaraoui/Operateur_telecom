def cout(durre):
    offres = [
        [200, float("inf"), 0],
        [100, 120, 0.5],
        [50, 60, 1],
        [20, 30, 1.5],
        [0, 0, 2],
    ]

    couts = []
    for offre in offres:
        cout = offre[0]
        minutes = offre[1]
        tarif = offre[2]
        if durre > minutes:
            cout += (durre - minutes) * tarif
        couts.append(cout)
    return couts


while True:
    o = input("ecrire o pour afficher la list ou n pour quitter : ").lower().strip(" ")
    if o == "o":
        print("1 - Saisir la durée de communication")
        print("2 - Afficher la liste du côut mensuelle par offre")
        print("3 - Afficher l’offre la plus intéressante")
        print("4 - Quitter le programme")

        n = int(input("donner votre choix : "))

        if n == 1:
            durre = int(input("donner la durée de communication : "))
        elif n == 2:
            o = [200, 100, 50, 20, 0]
            i = 0
            for cout in cout(durre):
                print(f"{i+1} - offre de {o[i]} DH : {cout} DH")
                i += 1
        elif n == 3:
            minp = min(cout(durre))
            offres = [
            [200, float("inf"), 0],
            [100, 120, 0.5],
            [50, 60, 1],
            [20, 30, 1.5],
            [0, 0, 2],
            ]
            for offre in offres:
                if offre[0]==minp-(durre-offre[1])*offre[2]:
                    of=offre[0]
            print(f"l’offre la plus intéressante est : {of}DH")
        elif n == 4:
            print("au revoir")
            break
        else:
            print("donner un nombre entre 1 et 4")
    elif o=="n":
        print("au revoir")
        break
    else :
        raise Exception (f"vous avez saisi un element autre que o et n")
   
