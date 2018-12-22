import variable
from generator import VariablesGenerator

class If_Parameter(variable.Base):
    def __init__(self):
        super(variable.Base, self).__init__()
        self._if = False
        self.condition = ''
        self._else = False
        self.variable = False
        self.variableGenerator = VariablesGenerator()

class I_If(If_Parameter):
    def generate(self):
        pass

class If(I_If):
    def __init__(self):
        super(I_if, self).__init__()
    def generate(self):
        pass


class Elif_Parameter(variable.Base):
    def __init__(self):
        super(variable.Base, self).__init__()
        self._elif = False
        self._elifList = []
        self.conditionList = []
        self.variable = False
        self.variableGenerator = VariablesGenerator()

class I_Elif(Elif_Parameter):
    def generate(self):
        pass

class Elif(I_Elif):
    def __init__(self):
        super(I_if, self).__init__()
    def generate(self):
        pass

class Else_Parameter(variable.Base):
    def __init__(self):
        super(variable.Base, self).__init__()
        self._if = False
        self.condition = ''
        self._else = False
        self.variable = False
        self.variableGenerator = VariablesGenerator()

class I_Else(Else_Parameter):
    def generate(self):
        pass

class Else(I_Else):
    def __init__(self):
        super(I_if, self).__init__()
    def generate(self):
        pass
