# ======================================== #
# Fichier principal (et unique) du projet) #
# ======================================== #

def main():
    pass


def code():
    pass


def compte():
    pass


def creer_arbre():
    pass


def creer_table():
    pass


def decode():
    pass

def saveFile(path, s):
    """
    sauvegarde une string (format ascii) dans un fichier, grâce au chemin fourni.
    paramètre path: chemin d'accès du fichier
    paramètre s: string à sauvegarder
    return: None
    """
    bytes = s.encode("ascii")
    with open(path,"wb") as f:
        f.write(bytes)
    return

def loadFile(path):
    """
    crèe un string (format ascii) en ouvrant un fichier, grâce au chemin fourni.
    paramètre path: chemin d'accès du fichier
    return: string représentant l'entièretée du fichier.
    """
    with open(path, "rb") as f:
        str = f.read().decode("ascii")
    return str

def bintoint(s):
    """
    Permet de convertir une chaine caractère (de taille infini) en un seul et unique grand nombre qui pourra être séparé en bytes ensuite. Python permet de stocker des nombres infinis
    """
    val = 0
    for i in range(len(s)):
        val += 2**i if s[len(s)-i-1] == "1" else 0
    return val

def saveFileEncode(path, table, encodeds):
    """
    sauvegarde la table et la chaine encodée dans le fichier spécifié
    format:
        header: 
            identifieur "HCS" (Huffman Compressing System)
            taille table (bytes)
            taille chaine compressée (bits)
        entrée de table:
            taille clé de table
            clé de table
            caractère ASCII
        chaine compressée:
            valeur binaire
            (optionel) padding

    paramètres:
    path: chemin d'accès vers le fichier dans lequel nous souhaitons sauvegarder notre compression
    table: notre table, qui encode nos différents caractères en chaines de bits
    encodeds: string contenant des 1 et des 0, donc les bits une fois notre texte encodé
    
    return: None
    """
    k = table.keys()
    bink = {}
    for el in k:
        bink[el] =  bintoint(el)
    
    encodedval = bintoint(encodeds)
    with open(path, "wb+") as f:
        #header:
        f.write(b"HCS")
        f.write((len(bink)*3).to_bytes(4,"little"))
        f.write(len(encodeds).to_bytes(4,"little"))

        #table:
        for el in k:
            print(len(el).to_bytes(1,"little"))
            print(bink[el].to_bytes(1,"little"))
            print(table[el].encode("ascii"))
            f.write(len(el).to_bytes(1,"little"))
            f.write(bink[el].to_bytes(1,"little"))
            f.write(table[el].encode("ascii"))
        
        #chaine:
        f.write(encodedval.to_bytes(len(encodeds)//8+1,"little"))
