from .generator import Generator

class GeneratorVariable(object):
    def __init__(self):
        super().__init__()
    def addList(self, List):
        for name, datatype, value in List:
            self.variable = self.f.setVariable()
            self.variable.name = name
            self.variable.datatype = datatype
            self.variable.value = value
            self.add(self.variable)