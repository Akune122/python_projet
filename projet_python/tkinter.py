import tkinter as tk
import random
from tkinter import ttk
from tkinter.messagebox import *

score=0
nb_jeu=0
res=""
resultat=False
nb=0
rd=0
var=0


def save():

    def getEntry():
        global res
        global score
        global nb_jeu
        res = text.get()
        fichier = open("classement", "a")
        fichier.write(str(res))
        fichier.write(" --> Score : ")
        fichier.write(str(score))
        fichier.write(" sur ")
        fichier.write(str(nb_jeu))
        fichier.write(" jeu")
        fichier.write("\n")
        fichier.close()
        print(res)
    
    fenetre1 = tk.Tk()
    fenetre1.geometry('1920x1680')
    fenetre1.configure(bg='white')
    
    name = tk.Label(fenetre1, text=("Votre nom :"),font=("Monocraft",10))
    name.configure(bg='white')
    name.pack()
    
    value = tk.StringVar()
    value.set("Pseudo")
    
    text=tk.Entry(fenetre1,font=("Arial",20),textvariable=value)
    text.configure(bg='grey')
    text.pack()

    boutonsave=tk.Button(fenetre1, text="Sauvgarder",font=("Monocraft",15), command=getEntry)
    boutonsave.pack()

    leave=tk.Button(fenetre1, text="Quitter", command=fenetre1.destroy,font=("Monocraft",15))
    leave.pack()
    
    fenetre1.mainloop()


def deviner_lenombre():
    global rd
    var=0
    rd = random.randint(0,100)
    def rules():
        fenetre3 = tk.Tk()
        fenetre3.geometry('500x100')
        fenetre3.configure(bg='white')
        l = tk.LabelFrame(fenetre3, text="Règles du jeu :", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="Vous devez deviner un nombre entre 0 et 100 avec 10 essais ").pack()
        fenetre3.mainloop()

    def choisir():
        global nb
        global var
        global rd
        global score
        nb=int(text1.get())
        print(nb)
        print(rd)
        suite.config(text=("Essai"))
        if nb>100:
            suite1.config(text=("Choisir un nombre en dessosu de 0"))
        elif nb>rd:
            suite1.config(text=("Trop élevé !"))
            var+=1
        elif nb<rd:
            suite1.config(text=("Trop bas !"))
            var+=1
        elif nb==rd:
            suite1.config(text=("Bravo vous avez reussi !"))
            score+=1
        return score

    def quitter():
        global nb_jeu
        global score
        PTS.config(text=("Votre score :",score))
        fenetre2.destroy()
        nb_jeu+=1
        nb_jeu1.config(text=("NB de jeu jouer",nb_jeu))
        return nb_jeu
        
     
    fenetre2 = tk.Tk()
    fenetre2.geometry('1920x1080')
    fenetre2.configure(bg='white')


    name = tk.Label(fenetre2, text="Devine nombre",font=("Monocraft",50))
    name.configure(bg='white')
    name.pack()

    bouton1=tk.Button(fenetre2, text="Règles",font=("Monocraft",10),command=rules)
    bouton1.pack()


    value1 = tk.StringVar()
    value1.set("Choix")

    text1=tk.Entry(fenetre2,font=("Arial",20),textvariable=value1)
    text1.configure(bg='grey')
    text1.pack()

    start=tk.Button(fenetre2, text="Proposez",font=("Monocraft",15),command=choisir)
    start.pack()

    suite = tk.Label(fenetre2, text="Début du jeu ",font=("Monocraft",30))
    suite.configure(bg='white')
    suite.pack()

    suite1 = tk.Label(fenetre2, text="En attente de votre proposition !",font=("Monocraft",30))
    suite1.configure(bg='white')
    suite1.pack()

    leave=tk.Button(fenetre2, text="Quitter", command=quitter,font=("Monocraft",15))
    leave.pack()
    fenetre2.mainloop()


fenetre = tk.Tk()
fenetre.geometry('1920x1080')
fenetre.configure(bg='white')

##bg = tk.PhotoImage(file = "tkinter.png")
##
##bgg = tk.Label(fenetre, image=bg)
##bgg.place(x = 0, y = 0) 

PTS = tk.Label(fenetre, text=("Votre score :",score),font=("Monocraft",10))
PTS.configure(bg='white')
PTS.pack()

nb_jeu1 = tk.Label(fenetre, text=("NB de jeu jouer",nb_jeu),font=("Monocraft",10))
nb_jeu1.configure(bg='white')
nb_jeu1.pack()

label1 = tk.Label(fenetre, text="Lolo's games",font=("Monocraft",50))
label1.configure(bg='white')
label1.pack()

bouton1=tk.Button(fenetre, text="Devine le nombre",font=("Monocraft",15), command=deviner_lenombre)
bouton1.pack()

bouton2=tk.Button(fenetre, text="Pierre,papier,ciseaux !", command=fenetre.quit,font=("Monocraft",15))
bouton2.pack()

bouton3=tk.Button(fenetre, text="Sauvgarder", command=save,font=("Monocraft",15))
bouton3.pack()

bouton4=tk.Button(fenetre, text="Quitter", command=fenetre.destroy,font=("Monocraft",15))
bouton4.pack()


fenetre.mainloop()
