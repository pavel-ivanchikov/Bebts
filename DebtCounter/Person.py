import datetime
from Transaction import Transaction
from Process import Process
from Debt import Debt


class Person(Process):
    _counter = 0

    def __new__(cls, *args, **kwargs):
        cls._counter += 1
        return object.__new__(cls)

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.debts = []
        self.name = "Person " + str(self.__class__._counter)
        self.additional_ables = {'NEW_DEBT': self.new_debt, 'CHANGE_NAME': self.change_name}
        self._able.update(self.additional_ables)

    def new_debt(self, _, date: float, init: bool):
        process = Debt((date, self._me))
        self.add_transaction(Transaction(date, f'NEW_DEBT {date} from {self._me}', True), init)
        process.add_transaction(Transaction(date, f'INFO New debt: {date} from {self._me}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)
        self.debts.append(process)
        return process

    def change_name(self, text, date: float, init: bool):
        new_name = text.split(' ')[1]
        self.add_transaction(Transaction(date, f'CHANGE_NAME {new_name} from {self.name}', True), init)
        self.name = new_name

    def get_all_transaction(self):
        ans = []
        for transaction in reversed(self.get_data()):
            if transaction.official:
                date = datetime.datetime.fromtimestamp(transaction.date)
                date_text = date.strftime("%Y-%m-%d %H:%M:%S")
                tag = transaction.text.split()[0]
                if tag == 'INFO':
                    tag2 = transaction.text.split()[1]
                    if tag2 == 'New':
                        message = f'{date_text}\nThe process was created'
                    elif tag2 == 'CROSS':
                        message = f'{date_text}\nThe process was crossed'
                    else:
                        message = f'{date_text}\nSome another information'
                elif tag == 'CROSS':
                    message = f'{date_text}\nThe process was crossed'
                elif tag == 'NEW_DEBT':
                    message = f'{date_text}\nNew debt was created'
                elif tag == 'CHANGE_NAME':
                    message = f'{date_text}\nThe name was changed'
                else:
                    message = f'{date_text}\nUnknown tag'
                ans.append(message)
            else:
                ans.append(str(transaction))
        return f'\n' + '\n\n'.join(ans)
