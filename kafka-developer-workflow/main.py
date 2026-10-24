from src.modules.jira.card import Card
from src.modules.jira.jira import Jira
from src.modules.developers.developer import Developer
from src.modules.developers.developers import Developers
from src.modules.workflow import Workflow
from src.kafka.producer import EventProducer

jira = Jira()
card1 = Card("KDW-100", "Guided tour for Kafka Developer Workflow")
card2 = Card("KDW-101", "Juvenile age criteria")
jira.add_card(card1)
jira.add_card(card2)

developers = Developers()
developers.add_developer("Sanket Pawar")
developers.add_developer("John Doe")

producer = EventProducer(bootstrap_servers="localhost:29093")
workflow = Workflow(jira, developers, producer)
workflow.assign_card_to_developer("KDW-100")
developers.find_developer(100).available = True
workflow.assign_card_to_developer("KDW-101")

# print("Developer with ID 100:", developers.find_developer(100).name)
# print("All Developers:", [dev.name for dev in developers.list_developers()])