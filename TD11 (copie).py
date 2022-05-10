import random
from rotation import*

def matrices(n):  # j'ai gardé juste pour les tests à virer
    t = []
    for j in range(n):
        h = []
        for i in range(n):
            h.append(0)
        t.append(h)
    return t


def comp(t, tour):
    global bouge  # cette variable est pour les prises multiples
    droit=[]      # liste des positions possibles
    devoir=[]     # liste des positions obligatoires
    p_pouvoir=[]  # pions deplaçables
    p_devoir=[]   # pions obligés de déplacer
    for i in range(len(t)):
        for j in range(len(t)):
            l = len(t)
            i2 = i-1
            j2 = [j-1,j+1]
            if t[i][j] != 0 and t[i][j] % 2 == tour:  # vérifie que le pion appartient au joueur dont c'est le tour
                if t[i][j] < 3:  # mouvement pour un pion classique
                    for e in j2: # e est la colonne
                        if (e>=0 and e<l):
                            if(i2>=0 and i2<l):
                                if t[i2][e] == 0:
                                    droit.append([i2,e])
                                    if not([i,j] in p_pouvoir):
                                        p_pouvoir.append([i,j])
                                elif t[i2][e] % 2 != tour:
                                    h = 2*e-j
                                    if (i2-1>=0 and i2-1<l):
                                        if (h>=0 and h<l):
                                            if t[i2-1][h] == 0:
                                                devoir.append([i2-1,h])
                                                if not([i,j] in p_devoir):
                                                    p_devoir.append([i,j])
                else:            # mouvement pour une dame
                    for g in range(-1,2,2):
                        for k in range(-1,2,2):
                            f = 0      # casser la boucle
                            e = j      # e est la colonne
                            i2 = i     # i2 est la ligne
                            while f == 0:
                                i2 += g
                                e += k
                                if (e>=0 and e<l):
                                    if(i2>=0 and i2<l):
                                        if t[i2][e] == 0:
                                            droit.append([i2,e])
                                            if not([i,j] in p_pouvoir):
                                                p_pouvoir.append([i,j])
                                        elif t[i2][e] % 2 != tour:
                                            h = e + k # regarder la case qui suit dans la diagonale
                                            if (i2+g>=0 and i2+g<l):
                                                if (h>=0 and h<l):
                                                    if t[i2+g][h] == 0:
                                                        devoir.append([i2+g,h])
                                                        if not([i,j] in p_devoir):
                                                            p_devoir.append([i,j])
                                                        f+=1
                                                    else:
                                                        f+=1
                                                else:
                                                    f+=1
                                            else:
                                                f+=1
                                        elif t[i2][e] % 2 == tour:
                                            f += 1
                                    else:
                                        f+=1
                                else:
                                    f+=1
                                    
    if c == 0:   # pas de prise multiples
        if devoir != []:
            d = devoir.copy()
            pions = p_devoir.copy()
        elif droit != []:
            d = droit.copy()
            pions = p_pouvoir.copy()
        else:    # le joueur est bloqué la partie prend fin
            d = "too bad ;)"
            pions = "fin de partie"
    else:        # prise multiples
        if devoir != [] and bouge in p_devoir: 
            d = devoir.copy()
            pions = [bouge]
        else:
            d = "np"
            pions = "np"
        
    return d, pions


def jouer(t, tour):
    global c    # definit les coups multiples
    global bouge # pion avec lequel on vient de manger
    global gg  # gg termine la partie
    global p1m # pion1 mangé
    global p2m # pion2 mangé
    x,y = [-1,-1]
    xd, yd = [-1, -1]
    coups, mobile = comp(t, tour) 
    print(coups,mobile)
    if coups == "too bad ;)":
        print(f'la partie est finie, le joueur {tour+1} a gagné')
        gg += 1
    elif coups == "np":   # reset des coups multiples
        c = 0
    else:
        while not ([x,y] in mobile):
            x,y = map(int, input("coordonnées du pion à déplacer, sous la forme x,y: ").split(','))
        #id = mobile.index([x,y])
        while not ([xd,yd] in coups):       #while not ([xd,yd] in coups[id]):
            xd, yd = map(int, input("coordonnées où aller, sous la forme x,y: ").split(','))
        bouge = [xd,yd]
        if xd == 0 and t[x][y] < 3: # création de dames
            t[xd][yd] = t[x][y]+2
        else:
            t[xd][yd] = t[x][y]
        t[x][y] = 0
        if abs(x-xd) > 1:   # gere la bouffe
            if tour == 1:
                p2m += 1
            else:
                p1m += 1
            c = 1
            if (x-xd) > 0:
                if (y-yd) > 0:
                    t[xd+1][yd+1] = 0
                else:
                    t[xd+1][yd-1] = 0
            else:
                if (y-yd) > 0:
                    t[xd-1][yd+1] = 0
                else:
                    t[xd-1][yd-1] = 0
            if p1m == 10 or p2m == 10:
                gg += 1
                if p1m == 10:
                    print('joueur 2 a gagné')
                else:
                    print("joueur 1 a gagné")


damier = plateau(8,0)

p1m = 0
p2m = 0

gg = 0
c = 0
i = 1
bouge = []
while gg == 0:
    tour = i%2
    for e in damier:
        print(e)
    jouer(damier, tour)
    while c == 1:
        for e in damier:
            print(e)
        jouer(damier, tour)
    damier = retournement_de_matrice(damier)
    i += 1

