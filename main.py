class Observer():
    def __str__(self):
        return str(self.__class__)
    def __init__(self):
        self.news = []
    def update(self, news_container):
        self.news = news_container.news
        print(self, "received some news of Type:", news_container.__class__,"\n", "The News contains this:", news_container.news)

class NewsObservable():
    def __init__(self):
        self.news = []
        self.observers = []

    def notifyObservers(self):
        for obs in self.observers:
            obs.update(self)
    def addObserver(self, obs):
        self.observers+=[obs]
    def update_news(self, new_news):
        self.news = new_news
        self.notifyObservers()
class sport_infos(NewsObservable):
    pass


class wirtschafts_news(NewsObservable):
    pass


class stellen_anzeigen(NewsObservable):
    pass


class politik_news(NewsObservable):
    pass


class nachrichtendienst():
    def __init__(self):
        self.news_sender = [sport_infos(), wirtschafts_news(),
                   stellen_anzeigen(), politik_news()]
    def notifyAllForAll(self):
        for sender in self.news_sender:
            sender.notifyObservers()
    pass


class Marc(Observer):
    pass


class Aktifry(Observer):
    pass


class FrauMeyer(Observer):
    pass

dienst = nachrichtendienst()
marc = Marc()
meyer = FrauMeyer()
for sender in dienst.news_sender:
    sender.addObserver(meyer)
print(dienst.news_sender[0].news)
dienst.news_sender[0].update_news(["ronaldo lutscht"])
dienst.news_sender[0].addObserver(marc)
dienst.news_sender[0].update_news(["ronadlo lutscht", "messi auch"])
