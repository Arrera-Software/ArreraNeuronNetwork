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
"""

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
