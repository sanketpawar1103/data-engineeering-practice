class Card :
    def __init__(self, card_id, title):
        self.card_id = card_id
        self.title = title
        self.assignee = None

    def assign(self, developer_id):
        self.assignee = developer_id