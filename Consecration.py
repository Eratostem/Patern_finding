import os
import glob
from Ohio_algorythm.py import *

directory = input("path to data folder")

# Get a list of all text files in the directory
text_files = glob.glob(os.path.join(directory, "*.txt"))

ac = OhiO_Algorythm()
paternette = input("Enter first patern")
n = 2
while paternette != '':
  ac.ajouter_motif("paternette")
  paternette = input("Enter "+ n+ "th patern")
  n+=1
ac.construire_automate()

resultats = []
# Iterate over each text file 
for file_path in text_files:
    with open(file_path, "r") as file:
        # Perform operations on the file
        content = file.read()
        resultat = ac.chercher(content)
        if len(resultat) != 0:
          resultats.append((resultat,file_path))
for resultat, file_path in resultats:      
  for motif, debut, fin in resultat:
    print(f"Motif trouvé : {motif} | Position : {debut}-{fin} in  {file_path}")  
