from enum import Enum, auto

class news_magazin():
    def add_reader_to_rubric(self, reader, *rubrics):
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

    def addReader(self, name):
        self.reader_list+=[name]
    def notify_readers(self):
        for reader in self.reader_list:
            print(reader)
news_magazin.add_reader_to_rubric("marc", news_rubrik.POLITIK, news_rubrik.SPORT)
news_rubrik.POLITIK.notify_readers()