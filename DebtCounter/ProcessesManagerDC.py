import os
from ProcessesManager import ProcessesManager
from MyLife import MyLife
from Person import Person
from Debt import Debt


class ProcessesManagerDC(ProcessesManager):
    def __init__(self, path: str):
        super().__init__(path)
        self.new_process_tags = ('SPLIT', 'NEW_PERSON', 'NEW_DEBT')
        self.ables_dict = {}
        self.previous_action_result = 'Wellcome!'

    def _controller(self):
        for process in self.main_dict.values():
            if isinstance(process, MyLife):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())
            elif isinstance(process, Person):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())
            elif isinstance(process, Debt):
                self.ables_dict[process.get_process_name()] = 'CROSS, ' + ', '.join(process.additional_ables.keys())

    def get_main_process(self):
        return MyLife.create_first_process(int(self.first_process_name) / 10 ** 6)

    def deserialization(self):
        super().deserialization()
        self._controller()
