# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Liste = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
def plateau_vide(r):
    plateau = []
    for i in range(r):
        liste = []
        for y in range(r):
            liste.append(0)
        plateau.append(liste)
    return plateau


def plateau(r):
    Plateau = plateau_vide(r)
    for y in range(len(Plateau)):
        if y >= 6:
            if y % 2 == 0:
                x = 1
            else :
                x = 0
            for i in range(x,len(Plateau[1]),2):
                Plateau[y][i] = 1
        elif y < 4:
            if y % 2 == 0:
                x = 1
            else :
                x = 0
            for i in range(x,len(Plateau[1]),2):
                Plateau[y][i] = 2
        else:
            for i in range(len(Plateau[1])):
                Plateau[y][i] = 0
    return Plateau
           
"""
création du plateau
et pion
"""
def retournement_de_matrice(matrice):
    Matrice= []
    for y in range(len(matrice)):   
        liste = []
        for i in range(len(matrice[1])):
            liste.append(matrice[len(matrice)-(1+y)][len(matrice[1])-(1+i)])
        Matrice.append(liste)
    return Matrice

"""
y = colonne
i = ligne
on inverse les valeurs de la ligne que l'on met dans une liste 
qui devient alors une matrice 
"""
            
def option_decor(skin1,skin2,skin3,r):
    if r == 1:
        skin = skin1 
    if r == 2:
        skin = skin2
    if r == 3:
        skin = skin3
    elif r != 1 and r !=2 and r !=3:
        print("décor non disponible")
    return skin
"""
choix du decor 
"""
def analyse_jeu(pionx,piony,matrice):
    if matrice[piony-1][pionx-1] == 0 and matrice[piony-1][pionx+1] == 0:
        p = 0
    elif matrice[piony-1][pionx-1] == 0:
        p = 1
    elif matrice[piony-1][pionx+1] == 0:
        p = 2
    if matrice[piony-1][pionx-1] == 1 and matrice[piony-1][pionx+1] == 1:
        if matrice[piony-2][pionx-2] == 0 and matrice[piony-2][pionx+2] == 0:
            m = 0
    elif matrice[piony-1][pionx-1] == 1 and matrice[piony-2][pionx-2] == 0:
        m = 1
    elif matrice[piony-1][pionx+1] == 1 and matrice[piony-2][pionx+2] == 0:
        m = 2
    return p,m

"""
analyse des possibilités à la fois de déplacements et de gain de pièces
"""


    