from fnc.fncBase import fncBase,gestionnaire
import requests
import webbrowser
import urllib.parse
import platform

if platform.system() == "Darwin":
    import objc
    from CoreLocation import CLLocationManager, NSObject
    from Foundation import NSRunLoop, NSDate

    class ArreraLocationDelegate(NSObject):
        def __init__(self):
            self.__error = None
            self.__done = None
            self.__location = None

        def locationManager_didUpdateLocations_(self, manager, locations):
            self.__location = locations[-1]
            manager.stopUpdatingLocation()
            self.__done = True

        def locationManager_didFailWithError_(self, manager, error):
            self.__error = error
            self.__done = True

        def locationManager_didChangeAuthorizationStatus_(self, manager, status):
            # 2 = Denied, 3 = AuthorizedAlways, 4 = AuthorizedWhenInUse
            if status == 2:
                self.__error = "Denied"
                self.__done = True
            elif status == 3 or status == 4:
                manager.startUpdatingLocation()

class fncGPS(fncBase):
    def __init__(self,gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        self.__os_name = platform.system()
        self.__latitude = None
        self.__longitude = None
        self.__region = None
        self.__town = None
        
        # Demande l'autorisation native sur macOS dès l'initialisation du brain
        if self.__os_name == "Darwin":
            self.__request_mac_auth()

    def __request_mac_auth(self):
        try:
            self.__auth_manager = CLLocationManager.alloc().init()
            self.__auth_manager.requestWhenInUseAuthorization()
        except Exception:
            pass

    def locate(self):
        if self.__latitude is not None and self.__longitude is not None:
            return True

        natif = False
        if self.__os_name == "Windows":
            natif = self.__get_windows_location()
        elif self.__os_name == "Linux":
            natif = self.__get_linux_location()
        elif self.__os_name == "Darwin":  # Darwin est le noyau de macOS
            natif = self.__get_mac_location()

        if natif:
            return True
        else :
            return self.__get_locate_with_ip()

    def __get_windows_location(self):
        """Implémentation pour Windows 10/11 via winsdk."""
        import asyncio
        from winsdk.windows.devices.geolocation import Geolocator, GeolocationAccessStatus

        async def fetch_location():
            locator = Geolocator()
            status = await Geolocator.request_access_async()

            if status == GeolocationAccessStatus.ALLOWED:
                pos = await locator.get_geoposition_async()
                self.__latitude = pos.coordinate.latitude
                self.__longitude = pos.coordinate.longitude
                return True
            else:
                return False

        # Exécute la fonction asynchrone native dans un thread synchrone
        return False

    def __get_linux_location(self):
        import pydbus
        import time

        bus = pydbus.SystemBus()
        try:
            # Récupère le gestionnaire GeoClue2
            manager = bus.get('org.freedesktop.GeoClue2', '/org/freedesktop/GeoClue2/Manager')
            client_path = manager.GetClient()
            client = bus.get('org.freedesktop.GeoClue2', client_path)

            # Identifiant requis par GeoClue
            client.DesktopId = "Assistant_Meteo"
            client.Start()

            # On laisse quelques secondes au matériel (Wi-Fi/GPS) pour fixer la position
            time.sleep(2)

            loc_path = client.Location
            if loc_path != '/':
                loc = bus.get('org.freedesktop.GeoClue2', loc_path)
                lat, lon = loc.Latitude, loc.Longitude
                client.Stop()
                self.__latitude = lat
                self.__longitude = lon
                return True
            else:
                client.Stop()
                raise False

        except Exception as e:
            return False

    def __get_mac_location(self):
        """Implémentation pour macOS via CoreLocation."""
        delegate = ArreraLocationDelegate.alloc().init()
        delegate.__done = False
        delegate.__location = None
        delegate.__error = None

        manager = CLLocationManager.alloc().init()
        manager.setDelegate_(delegate)
        # Demande l'autorisation à macOS
        manager.requestWhenInUseAuthorization()
        
        # Sur macOS, il faut parfois forcer le démarrage même si on attend l'autorisation
        manager.startUpdatingLocation()

        import time
        start_time = time.time()

        # Boucle d'attente native macOS avec cooldown de 5 secondes
        while not delegate.__done:
            if time.time() - start_time > 5.0:
                break
            NSRunLoop.currentRunLoop().runMode_beforeDate_(
                "NSDefaultRunLoopMode", NSDate.dateWithTimeIntervalSinceNow_(0.1)
            )

        if delegate.__error:
            #print(delegate.error)
            return False

        if delegate.__location:
            coord = delegate.__location.coordinate()
            self.__latitude = coord.latitude
            self.__longitude = coord.longitude
            return True

        #print("Autre")
        return False

    def __get_locate_with_ip(self):
        api_url = 'https://ipinfo.io/json'
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            try:
                response = requests.get(api_url, timeout=5)
                response.raise_for_status()
                data = response.json()
                loc = tuple(map(float, data['loc'].split(',')))
                self.__region = self.__getDepartementWithPostalCode(data['postal'])
                self.__latitude = loc[0]
                self.__longitude = loc[1]
                return True
            except Exception as e:
                return False
        else:
            return False

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getRegion(self):
        return self.__region

    def getTown(self):
        if self.__town is not None:
            return self.__town

        try:
            url = 'https://nominatim.openstreetmap.org/reverse'
            params = {
                'lat': str(self.__latitude),
                'lon': str(self.__longitude),
                'format': 'json',
                'zoom': 10,  # Niveau de détail (10 = ville)
                'addressdetails': 1,
            }
            headers = {
                'User-Agent': 'my-geocoder'
            }
            response = requests.get(url, params=params, headers=headers, timeout=5)
            data = response.json()
            city = data.get('address', {}).get('city') \
                   or data.get('address', {}).get('town') \
                   or data.get('address', {}).get('village')
            self.__town = city
            return city
        except Exception:
            return None

    def launchGoogleMapItinerary(self, depart: str, arrivee: str):
        if depart != "" and arrivee != "":
            base_url = "https://www.google.com/maps/dir/?api=1"
            params = {
                "origin": depart,
                "destination": arrivee
            }

            # Encoder les paramètres pour les inclure dans l'URL
            url_params = urllib.parse.urlencode(params)
            full_url = f"{base_url}&{url_params}"

            # Ouvrir l'URL dans le navigateur par défaut
            return webbrowser.open(full_url)
        else:
            return False

    def getTownWithLatitudeAndLongitude(self,latitude:str,longitude:str):
        if self._gestionnaire.getNetworkObjet().getEtatInternet() :
            url = 'https://nominatim.openstreetmap.org/reverse'
            params = {
                'lat': str(latitude),
                'lon': str(longitude),
                'format': 'json',
                'zoom': 10,  # Niveau de détail (10 = ville)
                'addressdetails': 1,
            }
            headers = {
                'User-Agent': 'my-geocoder'
            }
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            city = data.get('address', {}).get('city') \
                   or data.get('address', {}).get('town') \
                   or data.get('address', {}).get('village')
            return city
        else :
            return None

    def __getDepartementWithPostalCode(self, postal_code):
        # Code postal en string pour éviter les erreurs avec les zéros
        str_code = str(postal_code)
        # Les 2 premiers chiffres du code postal correspondent au département (sauf exceptions)
        if str_code[:2] == "20":
            # La Corse a deux départements : 2A et 2B.
            if int(str_code) < 20200:
                return "2A"
            else:
                return "2B"
        if str_code[:2] in ["97", "98"]:
            # Outre-mer: retournez les 3 premiers chiffres
            return str_code[:3]
        return str_code[:2]

    def getFrenchDepartementWithTown(self,town:str):
        url = f"https://geo.api.gouv.fr/communes?nom={town.lower()}&fields=departement&format=json"
        result = requests.get(url).json()
        if result:
            return result[0]['departement']['code']
        else:
            return None