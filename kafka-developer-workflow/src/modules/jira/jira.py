class Jira:
    def __init__(self):
        self.cards = {}

    def add_card(self, cardId, title):
        self.cards[cardId] = Card(cardId, title)