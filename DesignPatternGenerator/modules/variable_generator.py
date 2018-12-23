from .variable import VariableFactory
from .generator import Generator


class DataTypeGenerator(Generator):
    def __init__(self):
        super(Generator,self).__init__()
        self.f = VariableFactory()
        self.variable = None

class VariableGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, datatype, value in List:
            self.variable = self.f.setVariable()
            self.variable.name = name
            self.variable.datatype = datatype
            self.variable.value = value
            self.add(self.variable)

class IntGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setInt()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class StrGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setStr()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class ListGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setList()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class DictGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setDict()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class SetGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, alue in List:
            self.variable = self.f.setSet()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class TupleGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setTuple()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)

class OtherGenerator(DataTypeGenerator):
    def __init__(self):
        super(DataTypeGenerator,self).__init__()
    def addList(self, List):
        for name, value in List:
            self.variable = self.f.setOther()
            self.variable.name = name
            self.variable.value = value
            self.add(self.variable)