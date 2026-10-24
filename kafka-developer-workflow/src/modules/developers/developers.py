from src.modules.developers.developer import Developer

class Developers:
    def __init__(self, producer):
        self.next_id = 100
        self.developers = {}
        self.producer = producer

    def add_developer(self, name):
        self.developers[self.next_id] = Developer(self.next_id, name)
        self.next_id += 1

    def find_developer(self, developer_id):
        return self.developers.get(developer_id)

    def list_developers(self):
        return list(self.developers.values())