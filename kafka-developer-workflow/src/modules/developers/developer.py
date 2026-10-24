class Developer:
    def __init__(self, developer_id, name):
        self.developer_id = developer_id
        self.name = name
        self.available = True

    def toggle_availability(self):
        self.available = not self.available