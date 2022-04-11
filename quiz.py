c=0
def question_1():
    print(" Question 1:\n De l'oeuvre de quel écrivain est tirée la célèbre question << Que sais-je ? >> ?")
    print(' 1.Etienne de la Boétie \n 2.Voltaire \n 3.Diderot \n 4.Montaigne')
    res=int(input(" Votre réponse :"))
    if res == 4:
        global c
        c = c+1
        print (' Vrai\n')
    elif res >4:
        print(" Il n'y a que 4 réponses, RECOMMENCEZ !")
        return question_1()
    else:
        print (' La réponse était Montaigne\n')
    return question_2()

def question_2():
    print(" Question 2:\n Quel célèbre dictateur dirigea l'URSS du milieu des années 1920 à 1953 ?")
    print(' 1.Lénine \n 2.Staline \n 3.Trotski \n 4.Molotov')
    res=int(input(" Votre réponse :"))
    if res == 2:
        global c
        c=c+1
        print(' Vrai\n')
    elif res >4:
        print(" Il n'y a que 4 réponses, RECOMMENCEZ !")
        return question_2()
    else: 
        print (' La réponse était Staline\n')
    return question_3()

def question_3():
    print(" Question 3:\n Parmi les animaux suivants, lequel peut se déplacer le plus rapidement ?")
    print(' 1.La tortue \n 2.Le springbok \n 3.Le léopard \n 4.Le chevreuil')
    res=int(input(" Votre réponse :"))
    if res == 2:
        global c
        c=c+1
        print(' Vrai\n')
    elif res >4:
        print(" Il n'y a que 4 réponses, RECOMMENCEZ !")
        return question_3()
    else:
        print (' La réponse était Le springbok\n')
    return question_4()

def question_4():
    print(" Question 4:\n Qui était le dieu de la guerre dans la mythologie grecque ?")
    print(' 1.Hadès \n 2.Apollon \n 3.Arès \n 4.Hermès')
    res=int(input(" Votre réponse :"))
    if res == 3:
        global c
        c=c+1
        print(' Vrai\n')
    elif res >4:
        print(" Il n'y a que 4 réponses, RECOMMENCEZ !")
        return question_4()
    else:
        print (' La réponse était Arès\n')
    return question_5()

def question_5():
    print(" Question 5:\n Quel état des Etats-Unis a pour capital Montgomery ?")
    print(" 1.La Californie \n 2.L'Alabama \n 3.L'Ohio \n 4.Le Nouveau-Mexique")
    res=int(input(" Votre réponse :"))
    if res == 2:
        global c
        c=c+1
        print(' Vrai\n')
    elif res >4:
        print(" Il n'y a que 4 réponses, RECOMMENCEZ !")
        return question_5()
    else:
        print (" La réponse était L'Alabama\n")
    return resultat()

def resultat():
    global c
    return 'Votre score:' + str(c) + '/5'

print(' Bienvenue dans ce quizz.\n Vous devrez répondre par le numéro de la réponse')
print (question_1())