from . import base
from . import basic
from . import Operator


class Structure(base.Base):
    def __init__(self):
        super().__init__()
        self.contentlist = []
    def addContent(self, content):
        self.contentlist.append(content)
    def isSetValue(obj):
        if obj.name != '' and obj.condition != '' :
            return True
        else:
            return False
    def isSameType(structure):
        if issubclass(type(structure), Structure):
            return True
        else:
            return False

class If(Structure):
    def __init__(self, condition=None):
        super().__init__()
        self.name = 'if'
        if condition == None:
            self.condition = self.createOperator()
        else:
            self.condition = condition
    def addCondition(self, condition=None):
        if issubclass(type(condition), Operator.Operator):
            if Operator.Operator.isSetValue(condition):
                self.condition = condition
    def createOperator(self):
        O = Operator.Eq()
        O.str1 = 'var1'
        O.str2 = 'var2'
        return O
    def isSetValue(condition):
        if condition.condition != '':
            return True
        else:
            return False

class Elif(If):
    def __init__(self, condition=None):
        self.conditionlist = []
        super().__init__()
        self.name = 'elif'
        if condition != None:
            self.condition.append(condition)
        del self.condition
    def addCondition(self, condition=None):
        if issubclass(type(condition), Operator.Operator):
            if Operator.Operator.isSetValue(condition):
                self.conditionlist.append(condition)
            else:
                self.addEqToConditionList()
        else:
            self.addEqToConditionList()
    def addEqToConditionList(self, condition=None):
        if condition == None:
            self.conditionlist.append(self.createOperator())
    def isSetValue(condition):
        if len(condition.conditionlist) != 0:
            return True
        else:
            return False

class Else(Structure):
    def __init__(self):
        super().__init__()
        self.name = 'else'
