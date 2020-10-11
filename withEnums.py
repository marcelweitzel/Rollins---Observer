from enum import Enum, auto

class Leser():
    def __init__(self):
        self.newest_articles = {}
    def update(self, new_article, rubrik):
        dict = {}
        dict["title"] = new_article["title"]
        dict["content"] = new_article["content"]
        self.newest_articles[rubrik] = dict
        print(self.newest_articles)

class news_magazin():
    @staticmethod
    def add_reader_to_rubric(reader, *rubrics):
        for rubric in rubrics:
            rubric.addReader(reader)

class news_rubrik(Enum):
    SPORT = auto()
    POLITIK = auto()
    STELLEN_ANZEIGEN = auto()
    WIRTSCHAFT = auto()

    def __init__(self, *args):
        super().__init__()
        self.reader_list = []
        self.article = {"title": "bread", "content": "mein content"}

    def addReader(self, name):
        self.reader_list+=[name]
    def notify_readers(self):
        for reader in self.reader_list:
            reader.update(self.article, self.name)
    def change_content(self, new_title, new_content):
        self.article = {"title": new_title, "content": new_content}
        self.notify_readers()

marc = Leser()
news_magazin.add_reader_to_rubric(marc, news_rubrik.POLITIK, news_rubrik.SPORT)
news_rubrik.POLITIK.change_content("MERKEL", "MERKEL TRITT AB")
news_rubrik.SPORT.change_content("MERKEL", "MERKEL WIRD FUßBALL MANAGER")
news_rubrik.WIRTSCHAFT.change_content("MERKEL", "WIRTSCHAFT bricht ein nach merkels abtritt")