class Card :
    def __init__(self, cardId, title):
        self.cardId = cardId
        self.title = title
        self.assignee = None

    def display(self):
        print(f"Card ID: {self.cardId}, Title: {self.title}, Assignee: {self.assignee}")

    def assign(self, developerId):
        self.assignee = developerId