import os
from Transaction import Transaction
from MyLife import MyLife
from Person import Person
from Debt import Debt
from ProcessesManager import ProcessesManager


class ProcessesManagerDC(ProcessesManager):
    def __init__(self, path: str):
        # super().__init__(path)
        self.path = path
        self.first_process_name = min(os.listdir(path)).split('.')[0]
        self.main_dict = {}
        self.ables_dict = {}
        self.temp_message_dict = {}
        self.new_process_tags = ('SPLIT', 'NEW_PERSON', 'NEW_DEBT')
        self.previous_action_result = 'Wellcome!'
        first_process = MyLife.create_first_process(int(self.first_process_name) / 10 ** 6)
        self.main_dict[self.first_process_name] = first_process
        self._read(self.first_process_name)  # Тут происходит считывание транзакций всего дерева процессов.
        self._acting()  # Тут происходит десериализация
        self._controller()

    def _controller(self):
        for process in self.main_dict.values():
            if isinstance(process, MyLife):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())
            elif isinstance(process, Person):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())
            elif isinstance(process, Debt):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())
