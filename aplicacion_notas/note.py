from datetime import datetime

class Note:
    def __init__(self, id, title, content, deadline):
        self.id = id
        self.title = title
        self.content = content
        self.deadline = datetime.strptime(deadline, '%d-%m-%Y %H:%M') if deadline else None
