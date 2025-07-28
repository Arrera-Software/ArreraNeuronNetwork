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
