from text_test import TextTest

class Show():
    __shows_list = [('game_of_thrones', 7)]

    @staticmethod
    def initializeShows():
        print "initializing show objects"
        shows = {}
        for (show_name, seasons) in Show.__shows_list:
            shows[show_name] = (Show(show_name, seasons))
        return shows


    def __init__(self, name, seasons):
        self.name = name
        self.text_tester = TextTest(name, seasons)
    