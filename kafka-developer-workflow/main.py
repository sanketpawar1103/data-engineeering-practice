
from src.modules.jira.card import Card
from src.modules.jira.jira import Jira
from src.modules.developers.developer import Developer
from src.modules.developers.developers import Developers

# jira = Jira()
# card1 = Card("KDW-100", "Guided tour for Kafka Developer Workflow")
# jira.add_card(card1)
# developer1 = Developer("dev-001", "Sanket Pawar")
# card1.assign(developer1)
# jira.display_cards()

developers = Developers()
developers.add_developer("Sanket Pawar")
developers.add_developer("John Doe")

print("Developer with ID 100:", developers.find_developer(100).name)
print("All Developers:", [dev.name for dev in developers.list_developers()])