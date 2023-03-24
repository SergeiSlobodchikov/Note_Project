from datetime import datetime


class Note:
    def __init__(self, id, title, body, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __str__(self):
        return f"Note #{self.id}: {self.title}\n{self.body}\nCreated: {self.created_at}\nLast updated: {self.updated_at}"

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()

