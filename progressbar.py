from time import sleep #importation du module Time
from tqdm import tqdm #importation du module tqdm

def progressbar(x): #creation de la fonction "progressbar"
    for i in tqdm(range(x)): #boucle pour que la barre se mette a jour
        sleep(3)

