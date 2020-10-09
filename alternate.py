class Zeitschrift():
    def __init__(self):
        self.alle_artikel = {"sport": news("sport-news", "sport"), "politik": news("politik-news", "politik")}
    def subscribe(self, reader, news):
        for artikel in news:
            self.alle_artikel.get(artikel).addObserver(reader)
class Leser():
    def __init__(self, name):
        self.name = name
        self.aktuellste_artikel = {}
    def update(self, neuer_artikel, news_rubrik):
        self.aktuellste_artikel[news_rubrik] = neuer_artikel
        print(self.name, "liest einen neuen", news_rubrik, "Artikel mit content:", neuer_artikel)
class news():
    def __init__(self, text, rubrik):
        self.rubrik = rubrik
        self.content = text
        self.reader = []
    def addObserver(self, leser):
        self.reader += [leser]
    def removeObserver(self, leser):
        self.reader -= [leser]
    def notify_observers(self, new_content):
        for leser in self.reader:
            leser.update(new_content, self.rubrik)
    def setContent(self, new_content):
        self.content = new_content
        self.notify_observers(new_content)
zeitung = Zeitschrift()
marc = Leser("marc")
meyer = Leser("meyer")
zeitung.subscribe(marc, ["sport"])
zeitung.alle_artikel.get("sport").setContent("FUßball")
zeitung.subscribe(meyer, ["sport", "politik"])
zeitung.alle_artikel.get("politik").setContent("Merkelraute")
zeitung.alle_artikel.get("sport").setContent("Schach")