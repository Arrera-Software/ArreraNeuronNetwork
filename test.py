"""
from meteofrance_api import MeteoFranceClient

# Initialiser le client
client = MeteoFranceClient()

# Chercher la localisation pour une ville (exemple : Paris)
places = client.search_places("Paris")
paris = places[0]  # On prend le premier résultat qui correspond à Paris

# Obtenir la météo actuelle
weather = client.get_forecast_for_place(paris)

# Afficher quelques informations
print("Ville :",weather.current_forecast)


from meteofrance_api import MeteoFranceClient

# Initialiser le client
client = MeteoFranceClient()
dictWarning = client.get_warning_dictionary("fr")

# Spécifier le lieu (par exemple, latitude et longitude pour Paris)
latitude = 48.8566
longitude = 2.3522

# Obtenir les alertes pour le lieu spécifié
alertes = client.get_warning_current_phenomenons("62").phenomenons_max_colors

for alerte in alertes:
    print(dictWarning.get_phenomenon_by_id(int(alerte['phenomenon_id']))['name']+
          " : "+ dictWarning.get_color_by_id(alerte['phenomenon_max_color_id'])['name'])

# Afficher les alertes
print(alertes)
print(type(alertes))
# Donne toutes les clés utiles !


import requests

url = f"https://geo.api.gouv.fr/communes?nom=ajaccio&fields=departement&format=json"
result = requests.get(url).json()
if result:
    print(result[0]['departement']['code'])

from pyradios import RadioBrowser
import vlc
import time

rb = RadioBrowser()

# Recherche France Inter
stations = rb.search(name="Radio 6", country="France")
if stations:
    print("Nom:", stations[0]['name'])
    print("URL du flux:", stations[0]['url'])

    player = vlc.MediaPlayer(stations[0]['url'])
    player.play()
    # Laisse le script ouvert assez longtemps pour écouter
    time.sleep(60)  # Écoute pendant 60 secondes
    player.stop()
else:
    print("Aucune station trouvée.")

"""
from spellchecker import SpellChecker

# Crée un correcteur pour le français
spell = SpellChecker(language='fr')

# Ton texte à corriger
texte = "Le chient cour tres vitte dan la rue. Il a ateind le parc en avans les enfants."

# Découpe le texte en mots (simplement, voir ci-dessous pour améliorations)
mots = texte.split()

# Trouve les mots mal orthographiés
mots_incorrects = spell.unknown(mots)

print("Mots incorrects trouvés :", mots_incorrects)

# Corrige chaque mot incorrect dans le texte
mots_corriges = [spell.correction(mot) if mot in mots_incorrects else mot for mot in mots]
texte_corrige = ' '.join(mots_corriges)

print("Texte corrigé :", texte_corrige)

