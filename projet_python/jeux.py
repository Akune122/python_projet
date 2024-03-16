import random

#Plusieurs jeux sur Tkinter avec possibilité d'enregistrer le score dans un fichier .txt avec un nom
####################################################################################
#FONCTION#
####################################################################################

def deviner_lenombre(n,n1):
    rd = random.randint(0,n)
    for i in range(1,n1+1):
        print("\nEssai n°",i)
        res=int(input("Choisir un nombre :"))
        if res>rd:
            print("Trop élevé !")
        elif res<rd:
            print("Trop bas !")
        elif res==rd:
            print("Bravo vous avez reussi au",i,"ème essai !")
            return True
    print("Vous avez perdu !")
    return False

def papier_ciseaux(m):
    liste = ['pierre','feuille','ciseaux']
    score1=0
    score2=0
    while True == True:
        rd= random.choice(liste)
        print(liste)
        choix=input("Choisir dans la liste : ")
        if rd=='pierre' and choix=='feuille':
            score1 +=1
        elif rd=='feuille' and choix=='pierre':
            score2 +=1
        elif rd=='ciseaux' and choix=='feuille':
            score2 +=1
        elif rd=='feuille' and choix=='ciseaux':
            score1 +=1
        elif rd=='ciseaux' and choix=='pierre':
            score1 +=1
        elif rd=='pierre' and choix=='ciseaux':
            score2 +=1
        print("\nVotre choix : ",choix)
        print("Adversaire choix : ",rd)


        print("\nVotre score :",score1)
        print("Adversaire score :",score2)
        if score1==m:
            return True
        elif score2==m:
            return False
        
#print(deviner_lenombre())
#print(papier_ciseaux())
        
####################################################################################
#Menu#
####################################################################################
        
choix=""
choix2=""
var=""
score=0
nb_jeu=0
while choix != "Q":
    choix=""
    choix2=""
    print("      Menu de jeu :")
    print("      Score :",score)
    print("(D) --> Deviner le nombre")
    print("(P) --> Pierre Papier Ciseaux")
    print("(S) --> Sauvegarder")
    print("(Q) --> Quitter")
    choix=input("Votre choix : ")


    if choix =="D":
        nb_jeu+=1
        n=int(input("Choisir un nombre de numéro au total :"))
        n1=int(input("Choisir un nombre d'essai maximum :"))
        print("\n      Voulez-vous entendre les règles ? :")
        print("(O) --> Oui")
        print("(N) --> Non")
        choix2=input("Votre choix : ")
        if choix2=="O" or choix2=="Oui":
            print("\nVous devez deviner un nombre entre 0 et",n,",avec",n1,"essai !")
            if deviner_lenombre(n,n1)==True:
                score+=1
            else:
                print("Vous avez perdu !")
        elif choix2=="N" or choix2=="Non":
            if deviner_lenombre(n,n1)==True:
                score+=1
            else:
                print("Vous avez perdu !")




    elif choix =="P":
        nb_jeu+=1
        n=int(input("Choisir un nombre de manche gagnante pour le jeu :"))
        print("\n      Voulez-vous entendre les règles ? :")
        print("(O) --> Oui")
        print("(N) --> Non")
        choix2=input("Votre choix : ")
        if choix2=="O" or choix2=="Oui":
            print("\nVous allez jouer une partie de pierre/papier/ciseaux en",n,"manche gagnante !")
            if papier_ciseaux(n)==True:
                score+=1
            else:
                print("Vous avez perdu !")
        elif choix2=="N"or choix2=="Non":
            if papier_ciseaux(n)==True:
                score+=1
            else:
                print("Vous avez perdu !")
    elif choix =="S" or choix=="Sauvegarder":
        fichier = open("classement", "a")
        nom=input("\nVotre pseudo :")
        fichier.write(str(nom))
        fichier.write(" --> Score : ")
        fichier.write(str(score))
        fichier.write(" sur ")
        fichier.write(str(nb_jeu))
        fichier.write(" jeu")
        fichier.close()
    elif choix =="Q" or choix=="Quitter":
        break
        # var =input("Vous êtes sur de vouloir quitter ? (oui/non) \n")
        # if var=="oui" or var=="Oui":
        #     break
