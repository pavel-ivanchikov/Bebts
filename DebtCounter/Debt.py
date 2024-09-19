from Process import Process


class Debt(Process):

    def __init__(self, identifier: tuple[float, float]):
        super().__init__(identifier)
        self.amount = 0

    def get_button_name(self):
        return self.related_processes[0].name + ' should give back ' + str(self.amount)
