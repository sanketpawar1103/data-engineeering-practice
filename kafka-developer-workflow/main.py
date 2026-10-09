
from src.modules.jira.card import Card
from src.modules.jira.jira import Jira
from src.modules.developers import developer

jira = Jira()
card1 = Card("KDW-100", "Guided tour for Kafka Developer Workflow")
jira.add_card(card1)
developer1 = developer.Developer("dev-001", "Sanket Pawar")
card1.assign(developer1)
jira.display_cards()