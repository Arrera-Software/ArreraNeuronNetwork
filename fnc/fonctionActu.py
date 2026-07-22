import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import feedparser
import random
from fnc.fncBase import fncBase,gestionnaire

USER_AGENTS = [
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    # macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
]

class fncActualiter(fncBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__source = [
            # Generaliste
            ("https://www.francetvinfo.fr/titres.rss", "france-info", "Generaliste"),
            ("https://www.lemonde.fr/rss/une.xml", "le monde", "Generaliste"),
            ("https://www.lefigaro.fr/rss/figaro_actualites.xml", "le figaro", "Generaliste"),
            ("https://www.20minutes.fr/feeds/rss-france.xml", "20 minutes", "Generaliste"),
            # Tech
            ("https://korben.info/feed", "koben", "Tech"),
            ("http://feeds2.feedburner.com/Frandroid", "frandroid", "Tech"),
            # Science
            ("https://www.futura-sciences.com/rss/actualites.xml", "futura-science", "Science"),
            ("https://www.sciencesetavenir.fr/rss.xml", "science et avenir", "Science"),
            ("https://reporterre.net/spip.php?page=backend", "reporterre", "Science"),
            # Sport
            ("https://www.francetvinfo.fr/sports.rss", "france-info", "Sports"),
            ("https://www.lefigaro.fr/rss/figaro_sport.xml", "le figaro", "Sports"),
            # Culture
            ("https://www.lemonde.fr/culture/rss_full.xml", "le monde", "Culture"),
            ("https://www.francetvinfo.fr/culture.rss", "france-info", "Culture"),
            ("https://www.lefigaro.fr/rss/figaro_culture.xml", "le figaro", "Culture"),
            ("https://www.telerama.fr/rss/cinema.xml", "telerama", "Culture"),
        ]

        self.__limit_for_flux = 3

        self.__articles = []

    def __parse_flux(self, url: str, source: str, cathegorie: str):
        try:
            out = []
            user_agent = random.choice(USER_AGENTS)
            headers = {'User-Agent': user_agent}

            # Utilisation de requests pour contourner les blocages de certificats SSL
            # fréquents avec urllib/feedparser par défaut sous macOS / Windows
            try:
                response = requests.get(url, headers=headers, timeout=10)
            except requests.exceptions.SSLError:
                response = requests.get(url, headers=headers, timeout=10, verify=False)

            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                for entry in feed.entries[:self.__limit_for_flux]:
                    titre = getattr(entry, 'title', 'Sans titre')
                    lien = getattr(entry, 'link', '')

                    out.append({
                        "source": source,
                        "titre": titre,
                        "lien": lien,
                        "cathegorie": cathegorie
                    })
            return cathegorie, url, out
        except Exception as e:
            return cathegorie, url, []

    def setActu(self, limit: int = 3, *args, **kwargs) -> bool:
        self.__limit_for_flux = limit
        self.__articles = []
        try:
            with ThreadPoolExecutor(max_workers=8) as executor:
                futures = [
                    executor.submit(self.__parse_flux, url, source, cathegorie)
                    for url, source, cathegorie in self.__source
                ]

                for future in as_completed(futures):
                    try:
                        cathegorie, url, resultats = future.result()
                        if resultats:
                            self.__articles.extend(resultats)
                    except Exception as e:
                        pass

            return len(self.__articles) > 0
        except Exception as e:
            return False

    def clear_articles(self):
        self.__articles = self._gestionnaire.getGestIA().deduplicate_actu(self.__articles)

    def getActu(self):
        return self.__articles