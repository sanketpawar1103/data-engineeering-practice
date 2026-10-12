class Workflow:
    def __init__(self, jira, developers):
        self.jira = jira
        self.developers = developers

    def assign_card_to_developer(self, card_id):
        card = self.jira.find_card(card_id)

        if card is None:
            print(f"Card with ID {card_id} not found.")
            return
        
        for developer in self.developers.list_developers():
            if developer.available:
                card.assign(developer.developer_id)
                developer.available = False
                print(f"Assigned card {card_id} to developer {developer.name}.")
                return


        print(f"No available developers to assign card {card_id}.")