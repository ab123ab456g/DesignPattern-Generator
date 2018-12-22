import variable
from generator import VariablesGenerator

class If_Parameter(variable.Base):
    def __init__(self):
        super(variable.Base, self).__init__()
        self._if = False
        self._elif = False
        self._elifList = []
        self._else = False
        self.variableGenerator = VariablesGenerator()

class I_if(If_Parameter):
    def generate(self):
        pass

class If(I_if):
    def __init__(self):
        super(I_if, self).__init__()
    def generate(self):
        pass
