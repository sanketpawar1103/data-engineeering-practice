class Jira:
    def __init__(self):
        self.cards = {}

    def add_card(self, card):
        self.cards[card.card_id] = card

    def preetify(self, card, asignee, status):
        print(f"""
        ╭──────────────────────────────────────────╮
        │ {card.card_id} │
        ├──────────────────────────────────────────┤
        │ Title    : {card.title}
        │ Assignee : {asignee}
        │ Status   : {status}
        ╰──────────────────────────────────────────╯
        """)

    def display_cards(self):
        for card in self.cards.values():
            assignee = "Unassigned"
            status = "Open"
            if card.assignee:
                assignee = card.assignee
                status = "Assigned"
        self.preetify(card, assignee, status)