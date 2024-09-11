import datetime


class Transaction:
    def __init__(self, date: float, text: str, official=False):
        self.date = date
        self.text = text
        self.official = official

    def __repr__(self):
        date = datetime.datetime.fromtimestamp(self.date)
        return f'{date.strftime("%Y-%m-%d %H:%M:%S")}{" +" if self.official else ""}\n{self.text}'
