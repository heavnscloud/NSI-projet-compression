# ======================================== #
# Fichier principal (et unique) du projet) #
# ======================================== #

def main():
    enco_deco = input("Voulez vous encoder ou decoder votre texte?")
    if enco_deco == "encoder":
        encode = input("Quel texte voulez vous encoder?")
        return code(encode)
    elif enco_deco == "decoder":
        decode = input("Quel texte voulez vous decoder?")
        return decoder(decode)


def code(texte):
    dic = compte(texte)
    arbre = creer_arbre(dic)
    table = creer_table(dic, arbre)
    return encoder_txt(table, texte)


def compte(texte):
    dic = {}
    for caractere in texte:
        if caractere in dic:
            dic[caractere] += 1
        else:
            dic[caractere] = 1
    return dic


def creer_arbre():
    pass


def creer_table():
    pass


def encoder_txt (tab,txt):
    liste = ''
    for c in txt:
        liste += tab[c]
    return liste


def decode():
    pass
