from Process import Process
from Debt import Debt
import datetime
from Transaction import Transaction


class Person(Process):
    _counter = 0

    def __new__(cls, *args, **kwargs):
        cls._counter += 1
        return object.__new__(cls)

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.name = "Person " + str(self.__class__._counter)
        self._able.update({'NEW_DEBT': self.new_debt, 'CHANGE_NAME': self.change_name})

    def new_debt(self, _, date: float, init: bool):
        self.add_transaction(Transaction(date, f'NEW_DEBT {date} from {self._me}', True), init)
        process = Debt((date, self._me))
        process.add_transaction(Transaction(date, f'INFO New debt: {date} from {self._me}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)
        return process

    def change_name(self, text, date: float, init: bool):
        new_name = text.split(' ')[1]
        self.add_transaction(Transaction(date, f'CHANGE_NAME {new_name} from {self.name}', True), init)
        self.name = new_name

    def get_button_name(self):
        return self.name
