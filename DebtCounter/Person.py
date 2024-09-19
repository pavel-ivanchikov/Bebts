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

    def split(self, _, date: float, init: bool):
        self.add_transaction(Transaction(date, f'SPLIT {date} from {self._me}', True), init)
        process = Debt((date, self._me))
        process.add_transaction(Transaction(date, f'INFO New: {date} from {self._me}', True), init)
        self.related_processes.append(process)
        process.related_processes.append(self)
        return process

    def get_button_name(self):
        return self.name
