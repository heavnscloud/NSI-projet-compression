# ======================================== #
# Fichier principal (et unique) du projet) #
# ======================================== #

def main():
    pass


def code():
    pass


def compte():
    pass


class Arbre:
    def __init__(self, gauche, droit, lettre = None, poid = 0):
        self.gauche = gauche
        self.droit = droit
        self.lettre = lettre
        if self.gauche:
            poid += self.gauche.poid
        if self.droit:
            poid += self.droit.poid
        self.poid = poid

    def __str__(self):
        print("("+str(self.poid),end="")
        if self.lettre:
            print(self.lettre,end="")
        else:
            self.gauche.__str__()
            self.droit.__str__()
        print(")",end="")

    def __repr__(self):
        self.__str__()
        return ""

    def afficher_bis(self):
        strings = {}
        self.ajouter_au_afficher(0, 0, strings)
        current = 0
        while current in strings:
            print(strings[current])
            current += 1

    def ajouter_au_afficher(self, floor, decalage, strings):
        if self.gauche is not None:
            decalage = self.gauche.ajouter_au_afficher(floor + 1, decalage, strings)
        strings[floor] = ((strings[floor] + " " * (decalage-len(strings[floor]))) if (floor in strings) else " " * decalage) + str(self.poid) + (str(self.lettre) if self.lettre else "")
        decalage += len(str(self.poid) + (str(self.lettre) if self.lettre else ""))
        if self.droit is not None:
            decalage = self.droit.ajouter_au_afficher(floor + 1, decalage, strings)
        return decalage


def creer_arbre(dictionnaire_lettres):
    arbres = []
    for item in dictionnaire_lettres.items():
        arbres.append(Arbre(None, None, lettre=item[0], poid=item[1]))

    def poid(arbre):
        return arbre.poid

    arbres.sort(key=poid)
    while len(arbres) > 1:
        a0 = arbres.pop(0)
        a1 = arbres.pop(0)

        nouveau_arbre = Arbre(a0, a1)

        index = 0
        while index < len(arbres) and nouveau_arbre.poid > arbres[index].poid:
            index += 1

        if index == len(arbres):
            arbres.append(nouveau_arbre)
        else:
            arbres.insert(index, nouveau_arbre)

    return arbres[0]


def creer_table(arbre):
    dico1 = creer_table_auxiliaire(arbre.gauche, "0")
    dico2.update(creer_table_auxiliaire(arbre.droit, "1"))
    return dico1

def creer_table_auxiliaire(arbre, cle):
    if arbre.lettre:
        return {cle: arbre.lettre}
    else:
        dico1 = creer_table_auxiliaire(arbre.gauche, cle + "0")
        dico2.update(creer_table_auxiliaire(arbre.droit, cle + "1"))
        return dico1


def decode():
    pass
