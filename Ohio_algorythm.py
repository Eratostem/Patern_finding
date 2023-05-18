class NoeudTrie:
    def __init__(self, caractere):
        self.caractere = caractere
        self.enfants = {}
        self.est_fin_mot = False
        self.lien_echec = None
        self.sortie = []

class OhiO_Algorythm:
    def __init__(self):
        self.racine = NoeudTrie(None)

    def ajouter_motif(self, motif):
        noeud = self.racine
        for caractere in motif:
            if caractere not in noeud.enfants:
                noeud.enfants[caractere] = NoeudTrie(caractere)
            noeud = noeud.enfants[caractere]
        noeud.est_fin_mot = True
        noeud.sortie.append(motif)

    def construire_automate(self):
        file_attente = []
        for enfant in self.racine.enfants.values():
            file_attente.append(enfant)
            enfant.lien_echec = self.racine

        while file_attente:
            noeud_actuel = file_attente.pop(0)
            for caractere, enfant_noeud in noeud_actuel.enfants.items():
                file_attente.append(enfant_noeud)
                noeud_lien_echec = noeud_actuel.lien_echec

                while noeud_lien_echec and caractere not in noeud_lien_echec.enfants:
                    noeud_lien_echec = noeud_lien_echec.lien_echec

                enfant_noeud.lien_echec = noeud_lien_echec.enfants[caractere] if noeud_lien_echec else self.racine
                enfant_noeud.sortie += enfant_noeud.lien_echec.sortie

    def chercher(self, texte):
        resultats = []
        noeud_actuel = self.racine
        for i, caractere in enumerate(texte):
            while noeud_actuel and caractere not in noeud_actuel.enfants:
                noeud_actuel = noeud_actuel.lien_echec
            if not noeud_actuel:
                noeud_actuel = self.racine
                continue
            noeud_actuel = noeud_actuel.enfants[caractere]
            for motif in noeud_actuel.sortie:
                index_debut = i - len(motif) + 1
                index_fin = i + 1
                resultats.append((motif, index_debut, index_fin))
        return resultats
      
      
ac = OhiO_Algorythm()
paternette = input("write un patern")
while paternette != '':
  ac.ajouter_motif("paternette")
  paternette = input("write un patern")
ac.ajouter_motif("Enzo") #just in case, cause that guy is realy dangerous (jax main and stuff ...)
ac.construire_automate()

texte = input("write da text ... if you want ... maybe ?")
resultats = ac.chercher(texte)

for motif, debut, fin in resultats:
    print(f"Motif trouvé : {motif} | Position : {debut}-{fin}")  
